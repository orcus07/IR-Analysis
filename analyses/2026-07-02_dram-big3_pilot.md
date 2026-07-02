---
title: "DRAM 빅3 비교 — 마이크론 FQ3'26 vs 삼성전자·SK하이닉스 CY1Q'26"
date: 2026-07-02
target: "DRAM Big 3 (Micron·Samsung·SK hynix)"
persona: neutral_dram_observer
quarter_anchor: "Micron FQ3'26 (2026-03~05) / Samsung·SK CY1Q'26 (2026-01~03)"
competitive: true
pipeline: pilot (세션 내 Fable 직접 수행, API 파이프라인과 동일 프레임)
model: claude-fable-5
---

# DRAM 빅3 비교 — 마이크론 FQ3'26 vs 삼성전자·SK하이닉스 CY1Q'26

**파일럿 케이스.** 관점은 중립(DRAM 시장 관찰자)이며, 세 회사를 같은 프레임으로
대칭 비교한다. 분석 축은 ① 분기 정량 ② DRAM 세부(ASP·점유율) ③ 컨콜 톤(원문
발췌) ④ 항목별 차이 ⑤ 시사점.

## 기간 정합성 — 회계연도(FY) ↔ 달력연도(CY) 매핑

| 회사 | 보고 분기 | 실제 기간 | 발표일 | 시점 차이 |
|---|---|---|---|---|
| Micron | FY2026 3분기(FQ3'26) | **2026-03 ~ 2026-05** (5/28 마감) | 2026-06-24 | 기준점(가장 최신) |
| SK하이닉스 | CY2026 1분기(1Q26) | **2026-01 ~ 2026-03** | 2026-04-23 | 마이크론보다 약 2개월 과거 |
| 삼성전자 | CY2026 1분기(1Q26) | **2026-01 ~ 2026-03** | 2026-04-30 | 마이크론보다 약 2개월 과거 |

가격이 매달 오르는 국면이라 **2개월 차이가 마진·ASP를 크게 벌린다.** 마이크론
수치가 더 좋게 보이는 부분 상당수는 시점 효과다. 직접 비교하는 표에는 이 점을
매번 표시했다. 삼성·SK의 CY2Q'26(4~6월) 실적은 7월 말 발표 예정이라 이 보고서에
없다.

## 데이터 신뢰도

- 세 회사 IR 원문(마이크론 prepared remarks PDF, SK하이닉스 뉴스룸, 삼성 뉴스룸)이
  모두 HTTP 403으로 막혔다. 수치는 복수 매체로 교차 확인했고, **발언 발췌는 2차
  전사 기준이라 원문 1:1 대조를 못 했다.** 어절 단위 정확성이 필요하면 IR 원문
  대조가 필요하다.
- ⚠️ 표시 항목은 매체 간 수치가 다르거나 기간 기준이 명시되지 않아 확인이 필요하다.

## 1. 분기 스코어보드 (정량)

| 지표 | Micron FQ3'26 | SK하이닉스 1Q26 | 삼성전자 1Q26 |
|---|---|---|---|
| 매출 | $41.46B (+346% YoY) | ₩52.58T ≈ $35.5B (+198% YoY, +60% QoQ) | ₩133.9T ≈ $90.6B (+69% YoY) — 전사 |
| 그중 메모리/DRAM | DRAM $31.3B (매출의 76%) | 전사가 사실상 메모리 | 메모리 매출 ₩74.8T (DS ₩81.7T 중) |
| 영업이익 | $33.68B (non-GAAP, 마진 81.2%) | ₩37.61T (마진 72%) | 전사 ₩57.23T (+755% YoY), DS ₩53.7T (마진 약 66%) |
| 순이익/EPS | EPS $25.11 (non-GAAP) | 순이익 ₩40.35T ⚠️ | — |
| 다음 분기 가이던스 | 매출 $50B±1B, GM ~86%, EPS $31±1 | 공식 수치 가이던스 없음(수요 초과 지속 전망) | 공식 수치 가이던스 없음(2Q 수요 강세 전망) |

⚠️ SK하이닉스는 순이익(₩40.35T)이 영업이익(₩37.61T)보다 크다. 영업외 이익이
포함된 것으로 보이나 원문을 확인하지 못했다.

주의: 마이크론 마진은 non-GAAP, 한국 두 회사는 K-IFRS 영업이익이라 **기준이 달라
절대 비교는 참고용**이다. 여기에 2개월 시점 차이(그 사이 가격 급등)까지 겹친다.

## 2. DRAM 세부 — ASP·점유율

### 분기 ASP 변화 (QoQ)

| 회사 | DRAM ASP 변화 | 기간 |
|---|---|---|
| Micron | +low-60%대 (비트 출하는 한 자릿수 초반 증가) | FQ3'26 (3~5월) |
| SK하이닉스 | +mid-60%대 | 1Q26 (1~3월) |
| 삼성전자 | ⚠️ "+146%" 보도 있으나 QoQ/YoY 기준 미확인 | 1Q26 (1~3월) |

세 회사 모두 "출하보다 가격"이 성장을 끌었다. 참고로 PC DRAM 고정거래가는 2026년
3월 $13로 11개월 연속 올랐다.

### CY1Q'26 DRAM 매출 점유율 (Omdia 기준, 달력분기로 환산 집계)

| 회사 | DRAM 매출 | 점유율 | QoQ 변화 |
|---|---|---|---|
| 삼성전자 | $37.4B | **38.6%** (1위) | +2.1pp (36.5%→38.6%) |
| SK하이닉스 | $28.0B | 28.8% (2위) | −4.1pp (32.9%→28.8%) |
| Micron | $21.7B | 22.4% (3위) | −0.4pp (22.8%→22.4%) |

- TrendForce 집계도 삼성 38.5%로 거의 같다. 삼성이 톱3 중 ASP 상승 폭이 가장
  컸고 서버 DRAM 매출 비중도 가장 컸다는 평가다.
- HBM만 보면 순위가 뒤집힌다: **SK하이닉스가 56.4%로 1위**(1Q26 기준).
- 정리하면 1Q26의 그림은 "범용 DRAM 가격 급등 국면에서 삼성이 전체 DRAM 1위
  격차를 약 10pp로 벌렸고, HBM 주도권은 여전히 SK하이닉스"다.

## 3. 컨콜 톤 비교 — 원문 발췌

발췌는 모두 2차 전사 기준(원문 1:1 대조 미완료).

### Micron — "사이클을 계약으로 끝냈다"는 톤

> "(We are) very pleased with our HBM4 product and Micron's shipments already of HBM4 of over $1 billion." — Sanjay Mehrotra, FQ3'26 콜

> "Supply shortages in memory and storage will take considerable time to improve, even as we expect industry supply to improve gradually in 2028."

- 16건의 장기 공급계약(SCA)이 핵심 메시지다. 잔여 계약액(RPO) 약 **$100B**,
  take-or-pay에 가격 하한까지 걸어 "역대 최고 마진보다 높은 수준을 보장"한다고
  했다. 실적 서프라이즈보다 **계약 구조로 사이클 변동성 자체를 없앴다**는 서사에
  힘을 실었다.
- 공급이 수요를 따라잡을 시점은 "가시성이 없다"고 했고, 신규 팹 의미 있는 출하는
  FY2028에나 가능하다고 못 박았다.

### SK하이닉스 — "구조적 역전, 과잉공급 위험은 관리된다"는 톤

> "Despite supply expansion, demand structurally outpaces supply. Long-term visibility from customer partnerships reduces oversupply risk." — 김우현 CFO, 1Q26 콜

> "The importance of memory has become greater than ever ... as this supply-demand imbalance persists, customers are prioritizing procurement over price." — 경영진, 1Q26 콜

- 2026년 HBM 물량은 완판이고 부족은 2027년까지 이어진다고 봤다. HBM4E는 하반기
  샘플, 2027년 양산 목표다.
- 용인 1기 클린룸 오픈을 2027년 2월로 3개월 당겼다. "수요는 구조적, 공급 확대는
  계획대로"라는 수성(守成)형 메시지다. 고객이 가격보다 물량 확보를 우선한다는
  발언은 가격 협상력이 완전히 공급자에게 넘어왔다는 뜻이다.

### 삼성전자 — "부족은 더 심해진다, 범용도 우리 무기"라는 톤

> (2차 전사 요지) 공급은 이미 수요에 크게 못 미치고, **이미 받은 주문 기준으로
> 2027년의 수급 격차는 2026년보다 더 벌어진다.** — 김재준 메모리사업부장, 1Q26 콜

- 셋 중 공급 부족 경고가 가장 셌다. 2026년 HBM 매출을 전년의 3배 이상으로 늘린다는
  계획도 밝혔다.
- 특이점은 **"요즘은 범용 DRAM이 HBM보다 수익성이 좋다"**는 취지의 발언이다.
  HBM 후발이라는 약점을 범용 DRAM 초강세 국면이 상쇄해 주는 지금 구도를
  솔직하게 드러냈다. 2월에 HBM4 양산을 시작(엔비디아 베라 루빈향)했다는 점도
  강조했다. ⚠️ HBM4 단가 $500~560, 마진 80% 이상이라는 보도는 매체 추정이다.

## 4. 항목별 비교 — 같은 항목, 같은 톤으로

| 항목 | Micron | SK하이닉스 | 삼성전자 | 핵심 차이 |
|---|---|---|---|---|
| 성장 서사 | 사이클 종식을 계약($100B RPO)으로 증명 | 구조적 수급 역전 + 장기 가시성으로 수성 | 부족 심화 경고 + 범용·HBM 양날개 | 마이크론은 **계약**, SK는 **구조**, 삼성은 **격차 확대 경고**를 앞세움 |
| HBM 위치 | HBM4 누적 $1B, 램프가 HBM3E의 2배 속도 | 점유율 56.4% 1위, 2026 완판 | 2월 HBM4 양산 개시, 2026 매출 3배 계획 | 현재 1위는 SK, 추격 속도는 마이크론·삼성이 강조 |
| 범용 DRAM | DRAM ASP +60%대(3~5월) | ASP +60%대 중반(1~3월) | 점유율 38.6%로 1위 격차 확대, ASP 상승 폭 최대 | 범용 가격 급등의 최대 수혜는 **삼성**(캐파·서버 DRAM 비중) |
| 공급 전망 발언 | 정상화 "가시성 없음", 신규 팹은 FY28 | 부족 2027년까지, 용인 3개월 앞당김 | **2027년 격차가 2026년보다 커진다** | 셋 다 부족 지속. 경고 강도는 삼성 > 마이크론 > SK 순 |
| 수익성(참고) | 영업마진 81.2% (non-GAAP, 3~5월) | 72% (K-IFRS, 1~3월) | DS 약 66% (K-IFRS, 1~3월) | 기준·시점이 달라 서열 단정 불가. 시점을 맞추면 격차는 줄어들 것 |
| 가이던스 스타일 | 수치 가이던스(+21% QoQ 성장 제시) | 정성 전망만 | 정성 전망만 | 마이크론만 숫자로 자신감을 표현 — 미국식 관행 차이도 있음 |

## 5. 시사점

1. **세 회사 모두 "부족 장기화"를 말하지만 근거가 다르다.** 마이크론은 계약(RPO),
   SK는 고객 파트너십 가시성, 삼성은 수주 잔량이다. 셋 다 자사에 유리한 프레임이라
   교차 검증 지표(하이퍼스케일러 캐펙스, 웨이퍼 투입량)로 따로 확인해야 한다.
2. **1Q26 점유율 이동은 '범용 DRAM 국면'의 산물이다.** 삼성의 +2.1pp는 HBM 역전이
   아니라 범용 가격·캐파 효과다. HBM4/4E 전환이 본격화되는 2026 하반기~2027년에
   점유율 그림이 다시 흔들릴 수 있다.
3. **마이크론의 $100B take-or-pay는 업계 가격 구조를 바꾼다.** 가격 하한이 걸린
   물량이 커질수록 다음 다운사이클의 바닥이 높아진다. 삼성·SK도 유사 계약을
   요구받을 공산이 크고, 7월 말 2Q26 콜에서 확인할 첫 번째 포인트다.
4. **다음 확인 시점: 삼성·SK의 CY2Q'26 발표(7월 말).** 마이크론 FQ3(3~5월)과
   기간이 2개월 겹쳐, 이번 보고서에서 시점 차이로 유보한 마진·ASP 비교를 그때
   제대로 맞춰볼 수 있다.

## 6. 결론

2026년 상반기 DRAM 시장은 "공급자 시장"이라는 말로도 부족한 초과수요 국면이다.
같은 국면을 두고 세 회사의 화법이 갈린다. 마이크론은 계약으로 미래 마진을
고정했다고 말하고, SK하이닉스는 구조적 우위를 지키고 있다고 말하며, 삼성은
부족이 더 심해진다고 경고하면서 범용 DRAM 1위 격차를 벌렸다. 숫자는 셋 다
사상 최고지만, **누가 이 사이클을 '구조'로 바꿔냈는지는 2027년 수급이 실제로
어긋나는 순간 판가름 난다.**

## Sources

- [Micron FQ3'26 8-K press release (SEC)](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000013/a2026q3ex991-pressrelease.htm) · [Investing.com 콜 전사](https://www.investing.com/news/transcripts/earnings-call-transcript-micron-tops-q3-2026-estimates-shares-jump-146-93CH-4759504) · [CNBC](https://www.cnbc.com/2026/06/24/micron-mu-earnings-report-q3-2026.html) · [TechTimes](https://www.techtimes.com/articles/319032/20260625/micron-q3-2026-earnings-100b-contracts-signals-ai-memory-cycle-break.htm) · [Futurum](https://futurumgroup.com/insights/micron-q3-fy-2026-hbm-and-lpdram-drive-the-next-phase-of-ai-memory-growth/)
- [SK hynix 1Q26 보도자료(뉴스룸)](https://news.skhynix.com/q1-2026-business-results/) · [CNBC](https://www.cnbc.com/2026/04/23/sk-hynix-earnings-ai-memory-shortage-hbm-demand.html) · [TechPowerUp](https://www.techpowerup.com/348448/sk-hynix-announces-1q26-financial-results) · [BigGo 콜 하이라이트](https://finance.biggo.com/news/KR_000660.KS_2026-04-23) · [StorageNewsletter](https://www.storagenewsletter.com/2026/04/29/sk-hynix-fiscal-1q26-financial-results/)
- [삼성전자 1Q26 실적 발표(뉴스룸)](https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2026-results) · [TechPowerUp](https://www.techpowerup.com/348675/samsung-q1-2026-results-memory-profit-up-nearly-50x-warns-of-2027-shortage) · [wccftech(범용 DRAM 수익성)](https://wccftech.com/samsung-q1-2026-earnings-conventional-dram-more-profitable-than-hbm-right-now/) · [DCD](https://www.datacenterdynamics.com/en/news/samsung-electronics-q1-26-operating-profit-exceeds-companys-fy25-full-year-total/)
- 점유율: [TechTimes(Omdia 집계)](https://www.techtimes.com/articles/318052/20260609/samsung-leads-dram-market-share-386-sk-hynix-trails-revenue-tops-profit-margins.htm) · [TrendForce(ASP)](https://www.trendforce.com/news/2026/05/18/news-memory-supercycle-drives-1q26-price-surge-samsung-flags-146-asp-jump-sk-hynix-sees-mid-60-dram-gains/) · [Counterpoint](https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share)

---
*공개 정보 기반 참고용 분석이며 투자 권유가 아니다. 발췌 인용은 2차 전사 기준.*
