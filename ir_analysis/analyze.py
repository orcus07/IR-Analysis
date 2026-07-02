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
    path = PERSONA_DIR / f"{persona_id}.yaml"
    if not path.exists():
        avail = ", ".join(p.stem for p in PERSONA_DIR.glob("*.yaml") if not p.stem.startswith("_"))
        sys.exit(f"페르소나 '{persona_id}' 를 찾을 수 없습니다. 사용 가능: {avail}")
    return _load_yaml(path)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    cfg = _load_yaml(CONFIG_PATH) if CONFIG_PATH.exists() else {}
    p = argparse.ArgumentParser(description="실적·컨콜 분석 + 관점별 임플리케이션")
    p.add_argument("--persona", default=cfg.get("persona", "sk_hynix_marketer"))
    p.add_argument("--target", default=cfg.get("target", "Micron Technology"))
    comp = p.add_mutually_exclusive_group()
    comp.add_argument("--competitive", dest="competitive", action="store_true")
    comp.add_argument("--no-competitive", dest="competitive", action="store_false")
    p.set_defaults(competitive=cfg.get("competitive", True))
    p.add_argument("--competitors", nargs="*", default=cfg.get("competitors", []))
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


def run(args: argparse.Namespace) -> Path:
    persona = load_persona(args.persona)

    user_prompt = build_user_prompt(
        persona_name=persona.get("name", args.persona),
        persona_viewpoint=persona.get("viewpoint", ""),
        focus_lenses=persona.get("focus_lenses", []),
        industry_context=persona.get("industry_context", ""),
        target=args.target,
        competitive=args.competitive,
        competitors=args.competitors,
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
    messages = [{"role": "user", "content": user_prompt}]

    print(f"▶ 분석 시작: 대상={args.target} / 관점={persona.get('name')} / "
          f"경쟁분석={'ON' if args.competitive else 'OFF'}", file=sys.stderr)

    # Fable 5 / Mythos 5: 안전 분류기가 거부(stop_reason=refusal)하면 Opus 4.8로
    # 자동 폴백(품질·안정성). SDK가 미지원이면 일반 경로로 자연스럽게 내려간다.
    is_fable = args.model.startswith(("claude-fable", "claude-mythos"))

    def open_stream(msgs):
        base = dict(
            model=args.model, max_tokens=args.max_tokens, system=system_prompt,
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

    out_dir = ROOT / args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    fname = f"{_dt.date.today().isoformat()}_{_slug(args.target)}_{args.persona}.md"
    out_path = out_dir / fname
    out_path.write_text(report + "\n", encoding="utf-8")

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
