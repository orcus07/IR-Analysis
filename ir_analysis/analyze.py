"""실적·컨콜 분석 파이프라인 (CLI).

사용 예:
  # 기본 케이스(config/config.yaml): SK하이닉스 마케터 관점 + 마이크론 + 경쟁사 비교
  python -m ir_analysis.analyze

  # 관점/대상/경쟁사를 바꿔서
  python -m ir_analysis.analyze --persona sk_hynix_marketer --target "NVIDIA" \\
      --competitors "AMD" "Intel"

  # 경쟁사 비교 끄기
  python -m ir_analysis.analyze --target "Micron Technology" --no-competitive

환경변수 ANTHROPIC_API_KEY 가 필요합니다.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import sys
from pathlib import Path

import yaml

try:
    import anthropic
except ImportError:  # pragma: no cover
    sys.exit("anthropic SDK가 필요합니다: pip install -r requirements.txt")

from ir_analysis.prompts import SYSTEM_PROMPT, build_user_prompt

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "config.yaml"
PERSONA_DIR = ROOT / "config" / "personas"
STYLE_GUIDE_PATH = ROOT / "config" / "style_guide.md"

# Opus 4.8/4.7/4.6 + Sonnet 4.6 의 동적 필터링 웹검색 변형
WEB_SEARCH_TOOL_TYPE = "web_search_20260209"


def _load_yaml(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_persona(persona_id: str) -> dict:
    # imported/ 는 다른 레포에서 동기화된 페르소나 (ir_analysis.sync_personas)
    for path in (PERSONA_DIR / f"{persona_id}.yaml",
                 PERSONA_DIR / "imported" / f"{persona_id}.yaml"):
        if path.exists():
            return _load_yaml(path)
    avail = ", ".join(sorted(p.stem for p in PERSONA_DIR.rglob("*.yaml")
                             if not p.stem.startswith("_")))
    sys.exit(f"페르소나 '{persona_id}' 를 찾을 수 없습니다. 사용 가능: {avail}")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    cfg = _load_yaml(CONFIG_PATH) if CONFIG_PATH.exists() else {}
    p = argparse.ArgumentParser(description="실적·컨콜 분석 + 관점별 임플리케이션")
    p.add_argument("--persona", default=cfg.get("persona", "sk_hynix_marketer"))
    p.add_argument("--custom-persona", default=None, metavar="설명",
                   help="페르소나를 YAML 없이 자유 서술로 지정 (--persona 무시)")
    p.add_argument("--persona-url", default=None, metavar="URL",
                   help="외부 저장소(raw URL)의 페르소나 YAML/텍스트를 가져와 사용")
    p.add_argument("--target", default=cfg.get("target", "Micron Technology"))
    comp = p.add_mutually_exclusive_group()
    comp.add_argument("--competitive", dest="competitive", action="store_true")
    comp.add_argument("--no-competitive", dest="competitive", action="store_false")
    p.set_defaults(competitive=cfg.get("competitive", True))
    p.add_argument("--competitors", nargs="*", default=cfg.get("competitors", []))
    p.add_argument("--scope", default=cfg.get("scope", "both"),
                   choices=["both", "earnings", "call"],
                   help="both=통합 / earnings=IR 실적 딥다이브 / call=어닝콜 딥다이브")
    p.add_argument("--no-history", dest="history", action="store_false",
                   help="같은 대상의 직전 보고서 주입(톤 델타 분석)을 끈다")
    p.set_defaults(history=cfg.get("history", True))
    p.add_argument("--model", default=cfg.get("model", "claude-opus-4-8"))
    p.add_argument("--effort", default=cfg.get("effort", "high"),
                   choices=["low", "medium", "high", "xhigh", "max"])
    p.add_argument("--max-tokens", type=int, default=cfg.get("max_tokens", 32000))
    p.add_argument("--max-search-uses", type=int, default=cfg.get("max_search_uses", 25))
    p.add_argument("--output-dir", default=cfg.get("output_dir", "analyses"))
    return p.parse_args(argv)


def _slug(text: str) -> str:
    s = re.sub(r"[^A-Za-z0-9가-힣]+", "-", text).strip("-").lower()
    return s[:40] or "report"


_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def find_previous_report(target: str, out_dir: Path) -> str | None:
    """같은 대상을 다룬 가장 최근 보고서 본문(출처 목록 제외)을 돌려준다."""
    tslug = _slug(target)
    best: Path | None = None
    for p in sorted(out_dir.glob("*.md")):  # 파일명이 날짜로 시작 → 정렬 = 시간순
        text_head = p.read_text(encoding="utf-8")[:2000]
        m = _FRONT_MATTER.match(text_head)
        fm_target = ""
        if m:
            fm_target = str((yaml.safe_load(m.group(1)) or {}).get("target", ""))
        if _slug(fm_target) == tslug or f"_{tslug}_" in p.name:
            best = p
    if best is None:
        return None
    text = best.read_text(encoding="utf-8")
    m = _FRONT_MATTER.match(text)
    if m:
        text = text[m.end():]
    # 출처 목록은 델타 분석에 불필요 — 잘라서 토큰을 아낀다.
    for marker in ("\n### 출처", "\n## 출처", "\n### Sources", "\n## Sources"):
        idx = text.find(marker)
        if idx != -1:
            text = text[:idx]
            break
    return f"(파일: {best.name})\n{text.strip()[:15000]}"


def load_persona_from_url(url: str) -> tuple[dict, str]:
    """외부 저장소의 페르소나를 가져온다. YAML(name/viewpoint)이면 그대로,
    아니면 전체 텍스트를 자유 서술 페르소나로 쓴다."""
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "ir-analysis"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read().decode("utf-8", "replace")
    data = None
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError:
        pass
    stem = _slug(url.rstrip("/").rsplit("/", 1)[-1].rsplit(".", 1)[0])[:24]
    if isinstance(data, dict) and data.get("viewpoint"):
        return data, "url-" + _slug(str(data.get("name", stem)))[:24]
    name = raw.strip().splitlines()[0][:40] if raw.strip() else stem
    return {"name": name, "viewpoint": raw.strip()[:6000]}, f"url-{stem}"


def run(args: argparse.Namespace) -> Path:
    if args.custom_persona:
        # 자유 서술 페르소나 — 첫 줄(또는 앞 40자)을 표시 이름으로 쓴다.
        desc = args.custom_persona.strip()
        persona = {"name": desc.splitlines()[0][:40], "viewpoint": desc}
        persona_id = "custom-" + _slug(persona["name"])[:24]
    elif args.persona_url:
        try:
            persona, persona_id = load_persona_from_url(args.persona_url)
        except Exception as e:
            sys.exit(f"페르소나 URL을 가져오지 못했습니다: {e}")
        print(f"🔗 외부 페르소나 로드: {persona.get('name')}", file=sys.stderr)
    else:
        persona = load_persona(args.persona)
        persona_id = args.persona

    out_dir = ROOT / args.output_dir
    previous_report = None
    if args.history and out_dir.exists():
        previous_report = find_previous_report(args.target, out_dir)
        if previous_report:
            print(f"↺ 직전 보고서 발견 → 톤 델타 분석 포함", file=sys.stderr)

    user_prompt = build_user_prompt(
        persona_name=persona.get("name", persona_id),
        persona_viewpoint=persona.get("viewpoint", ""),
        focus_lenses=persona.get("focus_lenses", []),
        industry_context=persona.get("industry_context", ""),
        target=args.target,
        competitive=args.competitive,
        competitors=args.competitors,
        scope=args.scope,
        previous_report=previous_report,
        output_language=persona.get("output_language", "한국어"),
    )

    system_prompt = SYSTEM_PROMPT
    if STYLE_GUIDE_PATH.exists():
        system_prompt += (
            "\n\n[우리말 작성 스타일 가이드 — 반드시 준수]\n"
            + STYLE_GUIDE_PATH.read_text(encoding="utf-8")
        )

    client = anthropic.Anthropic()
    tools = [{
        "type": WEB_SEARCH_TOOL_TYPE,
        "name": "web_search",
        "max_uses": args.max_search_uses,
    }]
    # 프롬프트 캐싱: 시스템(+스타일 가이드)과 사용자 프롬프트(직전 보고서 포함)가
    # 길고, pause_turn 마다 같은 접두가 재전송되므로 캐시 브레이크포인트를 건다.
    system_blocks = [{"type": "text", "text": system_prompt,
                      "cache_control": {"type": "ephemeral"}}]
    messages = [{"role": "user", "content": [
        {"type": "text", "text": user_prompt,
         "cache_control": {"type": "ephemeral"}},
    ]}]

    print(f"▶ 분석 시작: 대상={args.target} / 관점={persona.get('name')} / "
          f"경쟁분석={'ON' if args.competitive else 'OFF'}", file=sys.stderr)

    # Fable 5 / Mythos 5: 안전 분류기가 거부(stop_reason=refusal)하면 Opus 4.8로
    # 자동 폴백(품질·안정성). SDK가 미지원이면 일반 경로로 자연스럽게 내려간다.
    is_fable = args.model.startswith(("claude-fable", "claude-mythos"))

    def open_stream(msgs):
        base = dict(
            model=args.model, max_tokens=args.max_tokens, system=system_blocks,
            thinking={"type": "adaptive"}, output_config={"effort": args.effort},
            tools=tools, messages=msgs,
        )
        if is_fable:
            try:
                return client.beta.messages.stream(
                    **base, betas=["server-side-fallback-2026-06-01"],
                    fallbacks=[{"model": "claude-opus-4-8"}],
                )
            except TypeError:
                pass  # 설치된 SDK가 fallbacks 미지원 → 일반 경로
        return client.messages.stream(**base)

    # 서버측 웹검색은 한 응답 안에서 최대 10회 반복 후 pause_turn 으로 멈출 수 있다.
    # pause_turn 이면 대화를 그대로 다시 보내 이어서 진행한다.
    final = None
    for _ in range(8):  # pause_turn 연속 처리 상한
        try:
            with open_stream(messages) as stream:
                for text in stream.text_stream:
                    print(text, end="", flush=True)
                final = stream.get_final_message()
        except anthropic.BadRequestError as e:
            hint = ""
            if is_fable:
                hint = (" — Fable/Mythos 5는 30일 데이터 보존이 필요합니다"
                        "(ZDR 조직은 거부됨). --model claude-opus-4-8 로 바꿔 보세요.")
            sys.exit(f"요청 거부(400): {getattr(e, 'message', e)}{hint}")
        print(file=sys.stderr)

        if final.stop_reason == "pause_turn":
            messages.append({"role": "assistant", "content": final.content})
            print("… (pause_turn) 검색 이어서 진행", file=sys.stderr)
            continue
        break

    if final is None:
        sys.exit("응답을 받지 못했습니다.")
    if final.stop_reason == "refusal":
        sys.exit(f"요청이 거부되었습니다: {getattr(final, 'stop_details', None)}")

    report = "".join(b.text for b in final.content if b.type == "text").strip()
    if not report:
        sys.exit("보고서 텍스트가 비어 있습니다 (stop_reason="
                 f"{final.stop_reason}). max_tokens 를 늘려 보세요.")

    # 검색 진행 중계 등 제목 앞의 정크를 잘라낸다 — 보고서는 '#' 제목부터.
    m = re.search(r"^#\s", report, re.M)
    if m and m.start() > 0:
        report = report[m.start():]

    # max_tokens 로 잘린 보고서는 눈에 띄게 표시한다(조용한 불완전 저장 방지).
    truncated = final.stop_reason == "max_tokens"
    if truncated:
        report += ("\n\n---\n\n> ⚠️ **불완전한 보고서** — 출력 토큰 한도"
                   f"(max_tokens={args.max_tokens})에 걸려 끝이 잘렸다. "
                   "`--max-tokens` 를 늘려 다시 실행할 것.")
        print(f"⚠️ 보고서가 max_tokens({args.max_tokens})로 잘렸습니다 — "
              "--max-tokens 를 늘려 재실행하세요.", file=sys.stderr)

    out_dir.mkdir(parents=True, exist_ok=True)
    scope_suffix = "" if args.scope == "both" else f"-{args.scope}"
    fname = (f"{_dt.date.today().isoformat()}_{_slug(args.target)}"
             f"_{persona_id}{scope_suffix}.md")
    out_path = out_dir / fname
    if out_path.exists():  # 같은 날 재실행 → 덮어쓰지 않고 시각을 붙인다
        fname = f"{fname[:-3]}_{_dt.datetime.now():%H%M}.md"
        out_path = out_dir / fname

    # 렌더 뷰어(render/build.py)가 읽는 메타 — 보고서 앞에 프런트매터로 붙인다.
    front_matter = "\n".join([
        "---",
        f'title: "{args.target} 실적·컨콜 분석 — {persona.get("name", persona_id)} 관점"',
        f"date: {_dt.date.today().isoformat()}",
        f'target: "{args.target}"',
        f"persona: {persona_id}",
        f"scope: {args.scope}",
        f"competitive: {'true' if args.competitive else 'false'}",
        f"model: {args.model}",
        *(["truncated: true"] if truncated else []),
        "---",
        "", "",
    ])
    out_path.write_text(front_matter + report + "\n", encoding="utf-8")

    u = final.usage
    print(f"\n✔ 저장: {out_path}", file=sys.stderr)
    print(f"  입력 {u.input_tokens} / 출력 {u.output_tokens} 토큰", file=sys.stderr)
    return out_path


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)  # --help 등은 여기서 먼저 처리된다
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("환경변수 ANTHROPIC_API_KEY 를 설정하세요.")
    run(args)


if __name__ == "__main__":
    main()
