"""분석 프롬프트 빌더.

페르소나/분석대상/경쟁사 3개 변수를 받아, 웹검색으로 최신 실적·컨콜을
수집·분석하고 관점별 임플리케이션을 도출하도록 지시하는 프롬프트를 만든다.
출력 포맷은 analyses/ 의 첫 케이스 보고서와 동일한 구조를 따른다.
"""
from __future__ import annotations

import datetime as _dt
from typing import Sequence


SYSTEM_PROMPT = """\
당신은 기업 실적 발표(earnings release)와 어닝콜(컨퍼런스콜) 발언을 분석하는
시니어 IR/경쟁분석 애널리스트다. 지정된 페르소나의 관점에서, 분석 대상 회사의
최신 분기 실적과 컨콜 발언을 웹검색으로 수집해 정량(숫자)과 정성(경영진 톤)을
분리해 정리하고, 그 관점에서 실행 가능한 임플리케이션을 도출한다.

원칙:
- 반드시 웹검색으로 '가장 최신' 분기의 실적/컨콜을 찾는다. 추정·기억에 의존하지 말 것.
- 1차 사료(SEC 8-K/10-Q, 회사 IR 보도자료·컨콜 전문)를 우선하되, 접근이 막히면
  신뢰할 만한 2차 매체를 다수 교차 확인한다.
- 매체 간 수치가 상충하거나 1차 사료를 확인하지 못한 항목은 ⚠️로 표시하고 '확인 필요'라고 적는다.
- 분석 대상과 경쟁사의 보고 분기(시점)가 다르면 반드시 시점 차이를 고지한다.
- 추측을 사실처럼 쓰지 않는다. 모르면 모른다고 한다.
- 모든 주요 수치·인용에는 출처를 달고, 보고서 끝에 'Sources' 링크 목록을 둔다.
"""


def _bullets(items: Sequence[str]) -> str:
    return "\n".join(f"  - {x}" for x in items)


def build_user_prompt(
    *,
    persona_name: str,
    persona_viewpoint: str,
    focus_lenses: Sequence[str],
    industry_context: str,
    target: str,
    competitive: bool,
    competitors: Sequence[str],
    output_language: str = "한국어",
    today: str | None = None,
) -> str:
    today = today or _dt.date.today().isoformat()

    if competitive and competitors:
        comp_line = ", ".join(competitors)
        competitive_block = f"""\
3) 경쟁 현황 분석 (ON): 다음 경쟁사를 분석 대상과 '동일 프레임'으로 비교한다 — {comp_line}
   - 정량 비교표: 매출/이익률/성장/HBM 등 핵심 지표를 한 표에 나란히 (보고 분기 시점 명시)
   - 정성 비교표: 경영진 톤·내러티브·공급관·가격구조·점유율 태도·투자기조를 축별로 비교
   - 각 경쟁사의 최신 분기 실적/컨콜도 웹검색으로 직접 확인한다."""
    else:
        competitive_block = "3) 경쟁 현황 분석 (OFF): 경쟁사 비교는 생략한다."

    return f"""\
오늘 날짜: {today}

[페르소나]
- 이름: {persona_name}
- 관점: {persona_viewpoint}
- 산업 맥락: {industry_context}
- 임플리케이션 도출 렌즈:
{_bullets(focus_lenses)}

[분석 대상]
{target}

[작업]
1) 웹검색으로 {target}의 '가장 최신' 분기 실적 발표와 어닝콜 발언을 찾는다.
2) 정량(숫자)과 정성(경영진 톤·내러티브)을 분리해 정리한다.
{competitive_block}
4) 위 페르소나의 렌즈로 임플리케이션을 도출한다(방어/공세/구조점검/톤 등).

[출력 형식] — {output_language}로, 아래 마크다운 구조를 따른다:

# {target} 최신 실적·컨콜 분석 — {persona_name} 관점

> **케이스 설정** (페르소나 / 분석 대상 + 보고 분기 / 경쟁 분석 on·off / 작성일)
> **데이터 신뢰도 경고** (1차 사료 확보 여부, ⚠️ 표시 항목)
> **기간 정합성 경고** (대상 vs 경쟁사 보고 분기 시점차 — 경쟁 분석 ON일 때)

## 1. {target} — 정량 요약
(핵심 수치 표 + 가이던스)

## 2. {target} — 컨콜 정성(톤) 요약
(경영진의 자신감/공급관/점유율 전략/로드맵 등 — 가능하면 발언 인용)

## 3. 경쟁 현황 — 정량 비교 (경쟁 분석 ON일 때만)
## 4. 경쟁 현황 — 정성(톤) 비교 (경쟁 분석 ON일 때만)

## 5. {persona_name}를 위한 임플리케이션
(렌즈별로 구조화: 방어 / 공세 / 구조 점검 / 톤 벤치마크 등)

## 6. 한 줄 결론

### 출처
(사용한 URL을 마크다운 링크 목록으로)

지금 웹검색을 시작해 위 보고서를 작성하라."""
