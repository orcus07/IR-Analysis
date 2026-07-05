"""분석 프롬프트 빌더.

페르소나/분석대상/경쟁사/분석범위(scope)를 받아, 웹검색으로 최신 실적·컨콜을
수집·분석하고 관점별 임플리케이션을 도출하도록 지시하는 프롬프트를 만든다.
scope: "both"(통합) | "earnings"(IR 실적 딥다이브) | "call"(어닝콜 딥다이브).
직전 보고서(previous_report)가 있으면 '직전 대비 톤 델타' 분석을 추가로 지시한다.
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
- 컨센서스 수치는 집계 기관(LSEG/IBES/FactSet/Visible Alpha 등)을 명시하고 출처를 단다.
- 일회성 항목(세제 혜택, 지분 평가익 등)이 낀 상회/하회 판정은 표에서 별표(*)를 붙이고
  각주로 일회성 요인을 설명한다. 깨끗한 서프라이즈처럼 보이게 두지 않는다.
- 회계연도(FY)와 캘린더(CY)가 다른 회사가 있으면, 보고 분기를 'FY명칭 → 실제 기간 → 분기 종료일 → CY 매핑'으로 표를 만들어 정합성을 고지한다.
- 정성(톤) 요약은 추상 요약이 아니라 '실제 발언 원문(영문) 발췌 → 해석 → 시사점' 구조로 쓴다. 1차 전사가 막히면 2차 전사 출처를 명시하고 '원문 1:1 대조 미완료'를 밝힌다(발췌를 검증된 정확 인용처럼 위장하지 말 것).
- 경쟁 비교표는 모든 셀을 동일한 어법으로 쓰고, 각 행 마지막에 '핵심 차이(1줄)' 열을 두어 회사 간 차이를 일관된 톤으로 명시한다(셀마다 길이·톤이 따로 놀지 않게).
- 분석 대상과 경쟁사의 보고 분기(시점)가 다르면 반드시 시점 차이를 고지한다.
- 대상·경쟁사에 한국 기업이 있으면 영어 검색과 함께 **한국어 검색어로도 검색**한다
  (국내 매체·공시가 1차 사료에 더 가깝다).
- 추측을 사실처럼 쓰지 않는다. 모르면 모른다고 한다.
- 모든 주요 수치·인용에는 출처를 달고, 보고서 끝에 'Sources' 링크 목록을 둔다.

출력 규칙(중요):
- 최종 출력은 보고서 마크다운 본문만 낸다. 검색 진행 중계("Now let me…" 등),
  서두 코멘트, 계획 서술을 출력에 섞지 않는다.
- 최종 출력의 첫 줄은 반드시 '#'로 시작하는 보고서 제목이다.
"""


def _bullets(items: Sequence[str]) -> str:
    return "\n".join(f"  - {x}" for x in items)


def _competitive_block(competitive: bool, competitors: Sequence[str], scope: str) -> str:
    if not (competitive and competitors):
        return "3) 경쟁 현황 분석 (OFF): 경쟁사 비교는 생략한다."
    comp_line = ", ".join(competitors)
    if scope == "earnings":
        detail = "   - 정량 비교표 중심: 매출/이익률/성장/가이던스/캐펙스를 한 표에 나란히 (보고 분기 시점 명시)"
    elif scope == "call":
        detail = "   - 정성(톤) 비교표 중심: 경영진 톤·내러티브·공급관·가격구조·점유율 태도·투자기조를 축별로, 각사 발췌 앵커와 함께 비교"
    else:
        detail = ("   - 정량 비교표: 매출/이익률/성장/HBM 등 핵심 지표를 한 표에 나란히 (보고 분기 시점 명시)\n"
                  "   - 정성 비교표: 경영진 톤·내러티브·공급관·가격구조·점유율 태도·투자기조를 축별로 비교")
    return (f"3) 경쟁 현황 분석 (ON): 다음 경쟁사를 분석 대상과 '동일 프레임'으로 비교한다 — {comp_line}\n"
            f"{detail}\n"
            "   - 각 경쟁사의 최신 분기 실적/컨콜도 웹검색으로 직접 확인한다.")


def _output_format(target: str, persona_name: str, scope: str, competitive: bool,
                   has_history: bool) -> str:
    """scope별 보고서 골격."""
    delta_note = ("\n### 직전 대비 톤 델타 (직전 보고서 제공됨)\n"
                  "(새로 등장한 메시지 / 사라진 메시지 / 확신·경계 수위가 바뀐 지점 / "
                  "가이던스의 상향·하향)" if has_history else "")
    comp_on = competitive

    if scope == "earnings":
        comp_sec = ("\n## 4. 경쟁 현황 — 정량 비교 (경쟁 분석 ON)\n"
                    "(같은 지표로 나란히 + '핵심 차이(1줄)' 열, 시점차 명시)" if comp_on else "")
        return f"""\
# {target} 실적 분석(IR 딥다이브) — {persona_name} 관점

> **케이스 설정** (페르소나 / 분석 대상 + 보고 분기 / 범위: 실적 / 작성일)

### 데이터 신뢰도 경고
(1차 사료 확보 여부, 컨센서스 집계 기관, ⚠️ 확인 필요 항목)

### 기간 정합성 — 회계연도 vs 캘린더 매핑 (경쟁 분석 ON일 때)

## 1. 정량 스코어보드
(손익 전 항목: 매출/부문/이익/마진/EPS — 컨센서스 대비, 일회성 항목 별표 처리)

## 2. 세그먼트·현금흐름·캐펙스 분해
(부문별 성장의 물량/가격 분해, 현금흐름·재무상태, 캐펙스의 구성과 방향)

## 3. 가이던스 품질
(범위·가정·전분기 가이던스 대비 변경점, 달성 가능성에 대한 근거){delta_note}{comp_sec}

## 5. {persona_name}를 위한 임플리케이션
(렌즈별 구조화 — 숫자 근거를 반드시 붙인다)

## 6. 한 줄 결론

### 출처
(컨콜 발언은 가이던스 해석에 필요한 최소만 인용한다. 톤 분석은 이 보고서의 범위가 아니다.)"""

    if scope == "call":
        comp_sec = ("\n## 5. 경쟁사 톤 비교 (경쟁 분석 ON)\n"
                    "(축별로 각사 발췌 앵커와 함께, '핵심 차이(1줄)' 열)" if comp_on else "")
        return f"""\
# {target} 어닝콜 딥다이브 — {persona_name} 관점

> **케이스 설정** (페르소나 / 분석 대상 + 보고 분기 콜 일시 / 범위: 컨콜 / 작성일)

### 데이터 신뢰도 경고
(전사(transcript) 소스 등급: 회사 게시 1차 전사인지 2차 매체 전사인지)

## 1. 콜 개요
(참석 경영진, prepared remarks/Q&A 구조, 발표 직후 시장 반응 한 줄)

## 2. Prepared Remarks — 주제별 발췌 딥다이브
(주제별로 ① 발언 원문(영문) 발췌 → ② 해석 → ③ 관점 시사점.
자신감/수요·공급관/가격/로드맵/리스크 등 — 통합 보고서보다 발췌 수를 늘려 깊게)

## 3. Q&A 분석
(애널리스트 질문이 몰린 주제 / 경영진이 즉답을 피하거나 되돌린 질문 /
답변의 확신 수위가 높았던 대목 — 각각 원문 발췌 포함)

## 4. 말과 숫자의 괴리
(발언 대비 공시 수치의 긴장 지점 — 숫자는 대조에 필요한 최소만){delta_note}{comp_sec}

## 6. {persona_name}를 위한 임플리케이션

## 7. 한 줄 결론

### 출처
(실적 수치 자체의 딥다이브는 이 보고서의 범위가 아니다.)"""

    # both (통합)
    comp_sec = ("""
## 3. 경쟁 현황 — 정량 비교 (경쟁 분석 ON일 때만)
(세 회사를 같은 지표로 나란히 + 마지막 '핵심 차이(1줄)' 열, 일관 톤)

## 4. 경쟁 현황 — 정성(톤) 비교 (경쟁 분석 ON일 때만)
(축별로 세 회사를 같은 어법 + 발췌 앵커로 비교 + '핵심 차이' 열)""" if comp_on else "")
    return f"""\
# {target} 최신 실적·컨콜 분석 — {persona_name} 관점

> **케이스 설정** (페르소나 / 분석 대상 + 보고 분기 / 경쟁 분석 on·off / 작성일)

### 데이터 신뢰도 경고
(1차 사료 확보 여부, 발췌의 출처 등급, 컨센서스 집계 기관, ⚠️ 확인 필요 항목)

### 기간 정합성 — 회계연도 vs 캘린더 매핑 (경쟁 분석 ON일 때)
(회사별 'FY명칭 → 실제 기간 → 분기 종료일 → CY 매핑' 표 + 시점차 감안 주의)

## 1. {target} — 정량 요약
(핵심 수치 표 + 가이던스, 컨센서스 대비·일회성 항목 별표 처리)

## 2. {target} — 컨콜 정성(톤) 발췌 분석
(항목별로 ① 발언 원문(영문) 발췌 → ② 해석 → ③ 관점 시사점. 자신감/공급관/점유율/가격/로드맵 등){delta_note}{comp_sec}

## 5. {persona_name}를 위한 임플리케이션
(렌즈별로 구조화: 방어 / 공세 / 구조 점검 / 톤 벤치마크 등)

## 6. 한 줄 결론

### 출처
(사용한 URL을 마크다운 링크 목록으로)"""


_SCOPE_TASK = {
    "both": "정량(숫자)과 정성(경영진 톤·내러티브)을 분리해 정리한다.",
    "earnings": ("실적(IR) 딥다이브: 손익·세그먼트·현금흐름·캐펙스·가이던스를 깊게 분해한다. "
                 "컨콜 발언은 가이던스 해석에 필요한 최소만 쓴다."),
    "call": ("어닝콜 딥다이브: prepared remarks와 Q&A를 분리해 발언을 주제별로 깊게 분석한다. "
             "실적 수치는 발언 맥락에 필요한 최소만 쓴다."),
}


def build_user_prompt(
    *,
    persona_name: str,
    persona_viewpoint: str,
    focus_lenses: Sequence[str],
    industry_context: str,
    target: str,
    competitive: bool,
    competitors: Sequence[str],
    scope: str = "both",
    previous_report: str | None = None,
    output_language: str = "한국어",
    today: str | None = None,
) -> str:
    today = today or _dt.date.today().isoformat()
    scope = scope if scope in _SCOPE_TASK else "both"

    history_block = ""
    if previous_report:
        history_block = f"""

[직전 보고서 — 톤 델타 비교용]
아래는 같은 대상({target})을 다룬 직전 보고서다. 이번 보고서에 '직전 대비 톤 델타'
하위 섹션을 넣어라: 새로 등장한 메시지 / 사라진 메시지 / 확신·경계 수위가 바뀐 지점 /
숫자 가이던스의 상향·하향. 직전 보고서의 수치·인용을 재사용할 때는 검증 없이 사실로
재인용하지 말고 '직전 보고서 기준'임을 밝힌다. **특히 직전 보고서에서 ⚠️ 로 표시된
항목은 인용하지 말고 이번에 새로 검증하라** — 오류가 보고서를 타고 전파되면 안 된다.
직전 보고서와 이번 분기가 같은 분기라면 델타 대신 '동일 분기 재분석'임을 밝히고
관점 차이만 짚는다.
<previous_report>
{previous_report}
</previous_report>"""

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

[분석 범위] {scope} — {_SCOPE_TASK[scope]}

[작업]
1) 웹검색으로 {target}의 '가장 최신' 분기 실적 발표와 어닝콜 발언을 찾는다.
2) {_SCOPE_TASK[scope]}
{_competitive_block(competitive, competitors, scope)}
4) 위 페르소나의 렌즈로 임플리케이션을 도출한다.{history_block}

[출력 형식] — {output_language}로, 아래 마크다운 구조를 따른다:

{_output_format(target, persona_name, scope, competitive, bool(previous_report))}

지금 웹검색을 시작해 위 보고서를 작성하라. 출력은 보고서 본문만, 첫 줄은 '#' 제목."""
