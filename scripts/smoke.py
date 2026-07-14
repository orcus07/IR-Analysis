#!/usr/bin/env python3
"""초경량 스모크 테스트 — API 키 불필요, 저장소 파일을 변경하지 않는다.

검사 항목:
  1. 프롬프트 빌더 3모드(both/earnings/call) 생성
  2. analyses/*.md 프런트매터 파싱
  3. 뷰어 빌드(render.build) — 임시 경로에 생성해 docs/ 는 건드리지 않음

사용: python scripts/smoke.py   (성공 시 종료코드 0)
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def main() -> None:
    # 1) 프롬프트 3모드 — scope별 골격이 실제로 갈라지는지까지 확인
    from ir_analysis.prompts import build_user_prompt

    prompts = {}
    for scope in ("both", "earnings", "call"):
        prompt = build_user_prompt(
            persona_name="스모크",
            persona_viewpoint="스모크 검증용 관점",
            focus_lenses=["테스트 렌즈"],
            industry_context="",
            target="TestCo",
            competitive=True,
            competitors=["RivalCo"],
            scope=scope,
        )
        assert f"[분석 범위] {scope}" in prompt, f"scope={scope}: 범위 표기 누락"
        assert "TestCo" in prompt and "RivalCo" in prompt, f"scope={scope}: 대상/경쟁사 누락"
        prompts[scope] = prompt
    assert len(set(prompts.values())) == 3, "scope별 프롬프트가 갈라지지 않음"
    print("✔ 프롬프트 3모드 생성")

    # 2) 커밋된 보고서 전수 파싱 — 프런트매터가 깨진 보고서를 조기 검출
    import render.build as build

    reports = [build.parse_report(p) for p in sorted(build.ANALYSES_DIR.glob("*.md"))]
    assert reports, "analyses/ 에 보고서가 없음"
    for r in reports:
        assert r["title"] and r["date"] and r["md"], f"{r['id']}: 메타/본문 누락"
    print(f"✔ 보고서 파싱 {len(reports)}건")

    # 3) 뷰어 빌드 — OUT_PATH 를 임시 경로로 돌려 docs/index.html 은 보존
    # (build.main 이 경로를 ROOT 기준 상대경로로 출력하므로 임시 디렉터리도 ROOT 아래에)
    with tempfile.TemporaryDirectory(dir=ROOT, prefix=".smoke-") as td:
        build.OUT_PATH = Path(td) / "index.html"
        build.main()
        html = build.OUT_PATH.read_text(encoding="utf-8")
        assert "const REPORTS" in html, "뷰어에 보고서 데이터가 주입되지 않음"
        assert len(html) > 10_000, "뷰어 HTML이 비정상적으로 작음"
    print("✔ 뷰어 빌드")
    print("스모크 통과")


if __name__ == "__main__":
    main()
