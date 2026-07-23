---
title: "Alphabet 실적·컨콜 분석 — 바이사이드 애널리스트 관점"
date: 2026-07-23
target: "Alphabet"
persona: buyside_analyst
scope: both
competitive: true
model: claude-opus-4-8
---

# Alphabet 최신 실적·컨콜 분석 — 바이사이드 애널리스트 관점

> **케이스 설정** · 페르소나: 메모리 반도체(HBM/DRAM/NAND) 담당 바이사이드 애널리스트 / 분석 대상: **Alphabet — FY2026 2분기(4~6월), 2026-07-22(미 동부) 장 마감 후 발표** / 경쟁 분석: **ON (Microsoft·Meta)** / 작성일: 2026-07-23
>
> **관점 조정 고지** — 페르소나의 실제 운용 대상은 삼성전자·SK하이닉스·마이크론 같은 메모리 업체다. 따라서 이 보고서는 Alphabet 자체를 평가하는 동시에, Alphabet·Microsoft·Meta의 캐펙스·공급 발언을 **메모리 수요(HBM·서버 DRAM)의 선행 지표**로 읽는다. 세 하이퍼스케일러의 투자 규율과 톤 변화가 곧 다음 메모리 사이클의 방향타다.

---

### 데이터 신뢰도 경고

- **1차 사료 확보 상태**
  - Alphabet Q2: SEC 8-K(2026-07-22 접수)와 회사 실적 발표문(q4cdn PDF, SEC EDGAR exhibit)을 확보했다. 헤드라인 수치는 1차 사료로 교차 확인했다. EDGAR에 2026-07-22 접수된 8-K가 6월 실적과 재무를 담고 있으며, Q2 매출 $119.8B·Google Cloud $24.8B·보통주 귀속 순이익 $112.107B을 기록했다.
  - Microsoft·Meta: 회사 IR 보도자료(microsoft.com, Meta press release 인용)로 헤드라인을 확인했다.
- **발췌(톤) 출처 등급**
  - Pichai 발언 일부는 회사가 직접 게시한 편집본(blog.google)에서 인용했다 — **준(準)1차**.
  - Q2 컨콜 Q&A 인용은 gurufocus·Seeking Alpha·Yahoo·Motley Fool 등 **2차 전사**를 사용했다. **원문 1:1 대조 미완료**이므로 검증된 정확 인용으로 위장하지 않는다.
- **컨센서스 집계 기관**: 매출·EPS는 **LSEG**, 세그먼트(Search·YouTube·Cloud)는 **StreetAccount**, 캐펙스는 **Visible Alpha**로 각각 출처를 명시했다.
- **⚠️ 확인 필요 항목**
  1. **Alphabet Q2 '일회성 제외' 순이익의 전년 대비 방향**이 매체마다 엇갈린다. 한 매체는 순이익이 $98B 일회성 지분 평가익 덕에 298% 늘었고, 이를 빼면 전년보다 줄었다고 본다. 반면 실적 발표문 기준 순이익에 대한 지분 평가익 순효과는 +$77.1B이어서(112.1−77.1≈$35B 대 전년 $28.2B), 산술상으로는 증가로 계산된다. 기준(세금·전년 지분손익 포함 여부) 차이로 보이므로 **⚠️ 확인 필요**로 남긴다.
  2. Meta의 **$27B Nebius 인프라 계약**은 단일 2차 출처다. **⚠️ 확인 필요**.

---

### 기간 정합성 — 회계연도 vs 캘린더 매핑

| 회사 | FY 명칭 | 실제 기간 | 분기 종료일 | CY 매핑 | 비고 |
|---|---|---|---|---|---|
| **Alphabet** | FY2026 Q2 | 2026-04-01 ~ 06-30 | 2026-06-30 | **CY 2026 Q2** | FY=캘린더. **최신** |
| **Microsoft** | FY2026 Q3 | 2026-01-01 ~ 03-31 | 2026-03-31 | **CY 2026 Q1** | 6월 결산. FY26 Q4(4~6월)는 **7/29 발표 예정, 미공개** |
| **Meta** | FY2026 Q1 | 2026-01-01 ~ 03-31 | 2026-03-31 | **CY 2026 Q1** | FY=캘린더. Q2(4~6월)는 **7월 말 발표 예정, 미공개** |

> **⚠️ 시점차 주의(중요)** — Alphabet의 최신 분기는 **4~6월(CY Q2)**인데, Microsoft·Meta의 '가장 최신 공시'는 아직 **1~3월(CY Q1)**이다. 두 경쟁사의 6월 분기는 이 보고서 작성 시점(7/23)에 아직 나오지 않았다. 따라서 아래 비교는 **Alphabet이 한 분기 앞선 데이터**라는 점을 감안해 읽어야 한다. 특히 "메모리 가격 급등"은 CY Q2에 더 심해졌으므로, MSFT·Meta의 다음 실적(7/29~말)에서 캐펙스·원가 문구가 더 강해질 여지가 있다.

---

## 1. Alphabet — 정량 요약

### 핵심 손익 (Q2 2026, 4~6월)

| 지표 | Q2 2026 | 전년 동기 | YoY | 컨센서스(집계) | 판정 |
|---|---|---|---|---|---|
| 매출 | **$119.80B** | $96.4B | **+24%** (cc +23%) | $116.93B (LSEG) | **상회** |
| 영업이익 | **$40.77B** | ~$31.3B | **+30.4%** | — | 상회 |
| 영업이익률 | **34.0%** | ~32.5% | +약1.5%p | — | 개선 |
| GAAP 순이익 | **$112.1B** | $28.2B | **+298%** | — | 상회* |
| GAAP 희석 EPS | **$9.11** | — | **+294%** | — | 상회* |
| **조정(핵심) EPS** | **$2.85** | — | — | **$2.89 (LSEG)** | **소폭 하회\*** |
| 분기 캐펙스 | **$44.9B** | ~$22B | 약 2배 | $44.8B (Street) | 부합 |

**\* 일회성 요인(별표) 각주** — 헤드라인 순이익·EPS 급증은 영업 성과가 아니라 지분 평가익이 만든 착시다. 기타손익에 $98.0B 순이익이 반영됐는데 이는 주로 보유 지분의 미실현 평가익이었고, Q2에 지분 평가익 $99.0B의 순효과가 순이익을 $77.1B, 희석 EPS를 $6.26 늘렸다. 이 순이익에는 Anthropic·SpaceX 등 보유 지분에서 나온 $99B 규모 순평가익이 포함됐다. 즉 **핵심 EPS $2.85는 컨센서스 $2.89를 소폭 하회**했다. "실적이 추정치를 압도했다"는 서사는 지분 평가익을 걷어내면 성립하지 않는다.

### 세그먼트 분해

| 세그먼트 | 매출 | YoY | 컨센서스 대비 |
|---|---|---|---|
| Google Services | $94.5B | +15% | — |
| ─ Search & other | **$63.3B** | +17% | $63.4B 소폭 하회 (Street) |
| ─ YouTube 광고 | $11.06B | +13% | $10.8B 상회 (Street) |
| ─ 구독·플랫폼·기기 | $12.91B | +15% | — |
| **Google Cloud** | **$24.77B** | **+82%** | $18.05B 추정 대비 대폭 상회(Street, 1Q 기준값)* |
| Other Bets | $382M | +2% | 적자 $1.8B |

- **클라우드가 이번 분기의 서사다.** Google Cloud 매출이 AI 인프라·엔터프라이즈 AI 수요에 힘입어 82% 늘어 $24.8B에 이르렀고, 클라우드 영업이익은 전년 $2.8B에서 $8.8B로 뛰었다. 영업이익률은 전년 20.7%에서 35.6%로 상승했다.
- **백로그(미인식 계약 잔액)가 수요 가시성을 담보한다.** 백로그는 전분기 대비 $50B 넘게 늘어 $514B에 이르렀고, 이 중 절반 남짓이 향후 24개월 안에 인식된다.

### 가이던스 — 캐펙스가 주가를 결정했다

- 회사는 올해 캐펙스 전망을 지난 분기 $180B~$190B에서 $195B~$205B로 올렸다. Visible Alpha 집계 애널리스트들은 2026년 캐펙스를 약 $188B로 보고 있었다. → **컨센서스를 최대 $17B 초과하는 상향**.
- CFO Ashkenazi는 $44.9B 캐펙스 대부분이 AI 구축을 위한 기술 인프라에 갔고, 인프라 투자의 약 60%가 서버, 40%가 데이터센터·네트워킹 장비에 쓰였다고 밝혔다.
- **주가 반응**: Alphabet은 매출·클라우드 성장에서 시장 예상을 웃돌았지만, 2026년 캐펙스를 사상 최대인 $205B로 올린 뒤 시간외에서 5% 하락했다. → **좋은 숫자보다 무거운 투자 규모가 먼저 반영됐다.**

---

## 2. Alphabet — 컨콜 정성(톤) 발췌 분석

> 구조: ① 발언 원문(영문) → ② 해석 → ③ 관점 시사점. Q&A 인용은 2차 전사(원문 1:1 대조 미완료).

### (1) 자신감 — 지난 분기보다 톤이 한 단계 올라갔다
- **① 원문**: "We are in the early stages of a secular shift across multiple areas... We are more bullish on the opportunities ahead." (Pichai)
- **② 해석**: "여러 영역에서 구조적 전환의 초기 국면에 있고, 앞으로의 기회에 더 강하게 확신한다"는 뜻이다. Q1의 "terrific quarter" 수준을 넘어 **강도가 세졌다**.
- **③ 시사점**: 말과 숫자가 같은 방향이다. 매출 성장(20%→24%)과 클라우드 가속(63%→82%)이 톤 상향을 뒷받침한다. **말이 숫자를 앞서가는 괴리는 아직 없다.**

### (2) 공급관 — "여전히 공급 제약"을 다분기째 반복
- **① 원문**: "We're still in a supply-constrained environment. I think we've said this now for multiple quarters in a row, and we are seeing very strong demand both from external cloud customers as well as across the business." (Ashkenazi)
- **② 해석**: "여러 분기 연속으로 공급이 부족하다고 말해 왔고, 외부 클라우드 고객과 내부 양쪽에서 수요가 매우 강하다"는 뜻이다.
- **③ 시사점**: **메모리 관점에서 가장 중요한 문장이다.** 하이퍼스케일러가 스스로 "여전히 부족"이라 말하면, 그 병목의 상당 부분이 가속기·HBM·서버 DRAM이다. 브리지 전략까지 동원한다. "공급 제약 환경을 고려해 내부 용량을 늘리는 동안 3분기에는 3자(외부) 용량 사용을 브리지 전략으로 확대하겠다"고 했다.

### (3) 투자 규율 — ROI 프레임을 방패로 든다
- **① 원문**: Pichai는 "수익의 규모와 시점 모두 1년 전보다 나아 보인다"고 답했고, Ashkenazi는 "매력적인 ROI가 보이는 한, 다년 관점에서 투자한다"고 덧붙였다.
- **② 해석**: 캐펙스 급증에 대한 방어 논리를 "ROIC 프레임 + 다년 관점"으로 세웠다. Q1의 "제약된 환경에서 배분할 때 견고한 ROIC 프레임에 따라 움직인다"는 문구를 재확인했다.
- **③ 시사점**: 규율을 강조할수록, 역설적으로 **투자자 불안(현금흐름·감가상각)이 크다**는 방증이다. 주가가 빠진 이유도 여기 있다.

### (4) 로드맵·점유율 — 풀스택과 자체 실리콘을 차별점으로
- **① 원문**: "수직 최적화된 AI 스택, 공동 개발 부품, 프런티어 모델과 실리콘 소유가 우리를 차별화한다... 남들보다 고객 수요를 더 잘 충족한다." (Pichai, Q1)
- **② 해석**: 자체 TPU·모델·데이터센터를 한데 묶는 **풀스택**을 경쟁 우위로 내세운다.
- **③ 시사점**: Alphabet의 캐펙스 상향은 GPU 조달만이 아니라 **자체 TPU 확대**를 포함한다. TPU도 HBM을 대량 소비하므로 메모리 수요에는 동일하게 긍정적이다. 다만 GPU 의존 하이퍼스케일러와 달리, Alphabet은 캐펙스 상향 사유로 "부품 가격"을 콕 집지 않고 "수요를 맞추기 위한 용량 인도 가속"을 들었다. **가격 전가보다 물량 확대 메시지에 가깝다.**

### (5) 가격·경쟁 압력 — 톤에 균열의 조짐
- **① 원문/사실**: 중국 오픈웨이트 도구의 압박이 커지는 가운데, 기업들이 늘어나는 토큰 비용을 억제하고 있다.
- **② 해석**: 수요는 강하지만, **토큰 단가·저가 모델 경쟁**이라는 반대 축이 등장했다. 회사는 이번 주 저가형 Gemini 3종을 내놨다.
- **③ 시사점**: '초과수요=무한 가격 결정력'이 아니라는 신호다. 메모리와 달리 컴퓨트/추론 단가는 하방 압력을 받는다. **다운사이클 트리거를 볼 때 이 대목을 주시한다.**

---

## 3. 경쟁 현황 — 정량 비교

> **⚠️ 시점차**: Alphabet은 **CY Q2(4~6월)**, Microsoft·Meta는 **CY Q1(1~3월)** 기준이다. 표 안 모든 셀은 같은 어법으로 적었고, 마지막 열에 '핵심 차이(1줄)'를 뒀다.

| 지표 | **Alphabet** (Q2'26, 4~6월) | **Microsoft** (FY26 Q3, 1~3월) | **Meta** (Q1'26, 1~3월) | 핵심 차이(1줄) |
|---|---|---|---|---|
| 매출 | $119.8B (+24%) | $82.9B (+18%) | $56.3B (+33%) | 성장률은 Meta>Alphabet>MSFT, 규모는 역순 |
| 영업이익률 | 34.0% | **46.3%** | 41% | MSFT가 마진 최상위, Alphabet이 최하위 |
| GAAP 순이익 | $112.1B (+298%)* | $31.8B (+23%) | $26.8B (+61%)* | Alphabet·Meta는 일회성으로 부풀려짐 |
| 순이익 일회성 | 지분평가익 +$77.1B(순효과)* | OpenAI 손익 −$14M(경미) | 세금혜택 +$8B* | **MSFT만 상대적으로 '깨끗'** |
| 핵심 EPS vs 컨센 | $2.85 vs $2.89 **하회\*** | $4.27 vs $4.07 **상회** | $7.31 vs $6.79 **상회\*** | 클린 기준 EPS는 Alphabet만 미스 |
| AI/클라우드 성장 | Cloud +82% | Azure +40%(cc +39%) | 광고사(AI로 광고 강화) | 클라우드 가속폭은 Alphabet 압도 |
| 계약 백로그/RPO | $514B (+$50B QoQ) | $627B (약 2배) | 해당 없음 | 절대 백로그는 MSFT, 증가 모멘텀은 Alphabet |
| 분기 캐펙스 | $44.9B | $31.9B(리스 포함) | $19.8B | 절대 투자액은 Alphabet 최대 |
| **CY2026 캐펙스 가이드** | **$195~205B** (↑$180~190B) | **~$190B** | **$125~145B** (↑$115~135B) | 셋 다 상향, 규모는 Alphabet≈MSFT>Meta |
| **메모리/부품 언급** | 캐펙스 상향=**용량 인도 가속** | **~$25B가 부품가 상승분** | 상향 사유=**메모리·부품가** | **MSFT·Meta가 메모리 인플레를 명시** |

**표 각주(일회성 별표)**
- Alphabet\*: 지분 평가익 $99.0B의 순효과가 순이익을 $77.1B, EPS를 $6.26 늘렸다. 클린 EPS $2.85는 컨센 하회.
- Meta\*: 1분기 이익은 $8B 세금 혜택 덕을 봤고, 이는 OBBBA 시행으로 2025년 3분기에 낸 $15.9B 세금 부담을 상쇄했다. 이를 뺀 EPS $7.31이 진짜 서프라이즈다.
- Microsoft: 3분기 OpenAI 투자 관련 순손실이 순이익을 $14M 줄였고 EPS 영향은 미미했다. → **세 회사 중 가장 깨끗한 서프라이즈**.

---

## 4. 경쟁 현황 — 정성(톤) 비교

> 축별로 세 회사를 같은 어법으로 비교하고, 각 축에 발췌 앵커를 달았다.

| 축 | **Alphabet** | **Microsoft** | **Meta** | 핵심 차이(1줄) |
|---|---|---|---|---|
| **경영진 톤** | "구조적 전환 초기, 더 강세" (Pichai) | "클라우드·AI 수요 성장" (Nadella) — 담담·집행 중심 | "모든 신호가 확신을 준다" (Zuckerberg) — 선언적 | Meta가 가장 비전 지향, MSFT가 가장 절제 |
| **공급관** | "여전히 공급 제약, 3자 용량 브리지" | "적어도 2026년까지 제약 지속" | 인프라 확충 총력, 부품 확보 강조 | 셋 다 '공급<수요' 일치 — **메모리 강세 합창** |
| **가격 구조** | 저가 Gemini로 토큰 단가 방어 필요 | Copilot을 '좌석+사용량' 모델로 전환 | 광고 단가 +12%·노출 +19% 동반 상승 | Meta만 가격·물량 동반 개선(광고), 컴퓨트 단가는 하방 |
| **점유율 태도** | 풀스택·자체 TPU로 차별화 주장 | Copilot "Outlook 수준 사용" 강조 | "업계 최강 연구팀 구축" 선언 | MSFT는 침투율, Meta는 인재·모델, Alphabet은 스택 |
| **투자 기조** | ROIC·다년 관점, 2027 "유의미 증가" | "수익 확신, 용량 조기 확보에 집중" | "공격 투자 지속 + 인력 8천 명 감축" | Meta만 캐펙스↑와 감원↓ 병행(효율 압박) |

**발췌 앵커**
- **Microsoft(공급·투자)**: "추가 투자와 GPU·CPU·스토리지 조기 온라인 노력에도, 적어도 2026년까지 제약이 지속될 것으로 본다... 2026 캘린더 캐펙스는 약 $190B이며 이 중 약 $25B가 부품가 상승에서 비롯된다. 더 높은 수요 신호와 사용 증가, 효율성으로 투자 수익을 확신한다." (Hood)
- **Meta(톤·투자)**: Zuckerberg는 비용 상승 요인으로 "메모리 가격"을 지목하며 "우리 자체 작업과 업계 전반에서 보이는 모든 신호가 이 투자에 확신을 준다"고 했다. 동시에 캐펙스 상향과 약 8,000명(전체의 약 10%) 감원을 함께 발표해 주가가 시간외 7% 빠졌다.
- **Alphabet(공급)**: 위 §2-(2) 참조.

> **크로스 리드(메모리 렌즈)**: 세 회사가 **동시에** "수요>공급"을 말하고, 그중 **둘(MSFT·Meta)은 캐펙스 상향의 원인으로 '메모리·부품 가격'을 직접 지목**했다. 이는 메모리 업체 실적에 **물량+가격**이 함께 실린다는 1차 확인이다.

---

## 5. 바이사이드 애널리스트를 위한 임플리케이션

### 렌즈 A — 가이던스 대비 실적(상회 폭과 지속성)
- Alphabet은 매출·클라우드에서 명확히 상회했으나, **클린 EPS는 소폭 하회**했다. 서프라이즈의 질이 낮다(일회성 지분익 의존).
- 하이퍼스케일러 3사 모두 **캐펙스 가이드를 상향**했다. Alphabet $195~205B, MSFT ~$190B, Meta $125~145B. **메모리 수요의 하방 경직성**을 강화한다.
- **지속성 판단**: Alphabet 백로그 $514B, MSFT RPO $627B는 향후 수요를 계약으로 잠갔다는 뜻이다. 단기 사이클 반전 리스크가 낮다.

### 렌즈 B — 마진 구조(가격 vs 물량, 계약 방어력)
- **메모리 본업 관점**이 핵심이다. 하이퍼스케일러 캐펙스에서 메모리가 차지하는 비중이 급등하고 있다. SemiAnalysis는 메모리 비중이 2023~24년 약 8%에서 2026년 약 30%로 오른다고 보고, CLSA는 2026년 35%에서 2027년 48%까지 본다.
- **가격 방어력은 계약으로 잠겨 있다.** 소수 하이퍼스케일러에 수요가 집중되며 이들이 이례적 가격 결정력을 갖고, Meta·Google·Microsoft·Amazon이 프리미엄이되 안정적인 가격으로 공급을 사실상 보장하는 장기 DRAM 계약을 맺고 있어 소비자 공급망이 변동성을 흡수한다. → **메모리 업체엔 물량·가격·기간이 함께 고정되는 우호 구조**.

### 렌즈 C — 캐펙스·공급 규율(다음 다운사이클 트리거)
- 지금은 규율이 **완화 방향**이다(3사 동시 상향). 다운사이클 트리거는 아직 **미점등**.
- **점검할 조기 경보**:
  1. **하이퍼스케일러 중 하나라도 캐펙스 가이드를 하향·평탄화** → 수요 바닥 붕괴 신호.
  2. **HBM 계약가의 QoQ 하락** → 현재는 SK하이닉스가 2026년 HBM·DRAM·NAND 용량을 사실상 완판했다고 밝혔을 만큼 타이트.
  3. **DRAM 가격 상승 둔화**: 일반 DRAM 계약가가 Q1 기록적 QoQ +90~95% 뒤 Q2에는 +58~63%로 둔화가 예상된다. 가격 상승의 '속도'가 꺾이는 국면을 예의주시한다.
- **구조적 타이트니스는 2027까지**: 삼성 메모리 수장은 4/30 실적에서 메모리 전반의 "심각한 공급 부족"이 적어도 2027년까지 이어진다고 경고했다. 골드만삭스는 2026년 DRAM 4.9%·NAND 4.2%·HBM 5.1%의 공급 부족을 2011년 이후 최대로 본다.

### 렌즈 D — 경영진 톤 벤치마크(확신 vs 경계, 말·숫자 괴리)
- **확신 강도**: Meta(선언적·비전) > Alphabet(강세 전환) > Microsoft(절제·집행). 
- **말·숫자 괴리 점검**: Alphabet은 톤과 숫자가 대체로 일치하나, **헤드라인 순이익의 착시**와 **토큰 단가 경쟁 등장**이 옥에 티다. Meta는 캐펙스↑와 감원을 병행해 **'성장 서사 + 방어적 원가 관리'가 공존**한다. → 메모리 업체엔 **수요는 유지되되 고객이 원가에 민감**해진다는 신호. 협상에서 하이퍼스케일러의 가격 저항이 서서히 강해질 수 있다.

### 렌즈 E — 상대 밸류에이션(프리미엄/디스카운트 근거 변화)
- **메모리 3사 대비 하이퍼스케일러**: 하이퍼스케일러 캐펙스가 메모리 매출로 전환되는 구조라, 메모리 업종은 **하이퍼스케일러 실적의 후행 수혜주**로 재평가될 여지가 크다. 골드만삭스는 2026~2031년 하이퍼스케일러 AI 캐펙스를 누적 $7.6조로 추정한다.
- **디스카운트 해소 논거**: 과거 메모리주는 사이클 변동성 때문에 낮은 멀티플을 받았다. 지금은 2026년 HBM이 확정 가격에 완판돼 있고, 2027년 협상에서 가격이 약해질 때가 수요 포화의 신호라는 점에서, **사이클 가시성 개선 → 멀티플 재평가**의 근거가 쌓인다. 다만 이는 하이퍼스케일러가 캐펙스를 유지한다는 전제 위에 선다.

### 실행 요약(방어 / 공세 / 구조 점검)
- **방어(다운사이드 헤지)**: 하이퍼스케일러 캐펙스 가이드·HBM 계약가를 월 단위로 추적한다. 어느 하나라도 하향 시 메모리 비중 축소.
- **공세(업사이드)**: MSFT(7/29)·Meta(말) 6월 분기에서 **'메모리·부품가' 문구가 더 강해지면** HBM·서버 DRAM 노출을 확대한다. Alphabet이 이미 그 방향을 선반영했다.
- **구조 점검**: HBM↔DDR5 웨이퍼 3:1 전환비가 유지되는 한 일반 DRAM 공급까지 압박된다. 신규 팹은 2027년 말~2028년 전까지 유의미한 양산에 이르지 못한다. → 공급 반전은 구조적으로 늦다.

---

## 6. 한 줄 결론

Alphabet의 Q2는 **매출·클라우드는 진짜 강세, 헤드라인 이익은 지분평가익이 만든 착시**였고(클린 EPS는 소폭 하회), 세 하이퍼스케일러가 **동시에 캐펙스를 올리며 "공급 부족"과 "메모리 가격"을 합창**한 점이 메모리 담당 바이사이드에게는 본업 수요를 확증하는 가장 중요한 신호다 — 다운사이클 트리거(캐펙스 하향·HBM 계약가 하락)는 아직 켜지지 않았다.

---

### 출처

- [9to5Google — Alphabet Q2 2026 실적](https://9to5google.com/2026/07/22/alphabet-q2-2026-earnings/)
- [Quiver Quantitative — GOOG Q2 2026](https://www.quiverquant.com/news/Alphabet+%28GOOG%29+Releases+Q2+2026+Earnings%3A+Revenue+Jumps+24%25)
- [Variety — YouTube Q2 2026 광고](https://variety.com/2026/digital/news/youtube-q2-2026-ad-sales-alphabet-google-earnings-results-1236818132/)
- [Yahoo/Quartz — Alphabet Q2 2026 Cloud +82%](https://finance.yahoo.com/markets/stocks/articles/alphabet-q2-2026-earnings-revenue-203058727.html)
- [StockTitan — Alphabet Q2 2026 8-K](https://www.stocktitan.net/sec-filings/GOOG/8-k-alphabet-inc-reports-material-event-c600716f9a4d.html)
- [CNBC — Alphabet Q2 실적·캐펙스 상향](https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html)
- [TradingKey — Google Q2 캐펙스 논쟁](https://www.tradingkey.com/analysis/stocks/us-stocks/262048041-google-earnings-report-q2-2026-goog-googl-services-cloud-search-capital-expenditures-tradingkey)
- [TheWrap — Alphabet Q2 2026](https://www.thewrap.com/industry-news/business/alphabet-earnings-q2-2026/)
- [Alphabet 실적발표문 PDF (q4cdn)](https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf)
- [Easternherald — 캐펙스 $205B, 주가 −5%](https://easternherald.com/2026/07/23/alphabet-q2-2026-earnings-capex-cloud-stock/)
- [GuruFocus — Q2 2026 Alphabet 컨콜 전사](https://www.gurufocus.com/news/8973389/q2-2026-alphabet-inc-earnings-call-transcript)
- [Seeking Alpha — Alphabet $195~205B 캐펙스·백로그](https://seekingalpha.com/news/4617114-alphabet-signals-195b-205b-2026-capex-while-expanding-third-party-capacity-as-a-bridge)
- [BigGo Finance — Alphabet Q2 컨콜 하이라이트](https://finance.biggo.com/news/US_GOOGL_2026-07-22)
- [Markets Daily — Alphabet Q2 컨콜](https://www.themarketsdaily.com/2026/07/22/alphabet-q2-earnings-call-highlights.html)
- [Yahoo — Alphabet Q2 컨콜 하이라이트](https://finance.yahoo.com/technology/ai/articles/alphabet-inc-goog-q2-2026-050111614.html)
- [blog.google — Pichai Q2 2026 발언](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/)
- [SiliconANGLE — Alphabet 캐펙스 상향](https://siliconangle.com/2026/07/22/alphabets-stock-sinks-after-it-bumps-up-ai-infrastructure-spending-yet/)
- [CNBC — Alphabet Q1 2026](https://www.cnbc.com/2026/04/29/alphabet-googl-q1-2026-earnings.html)
- [Microsoft IR — FY26 Q3 보도자료](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast)
- [Tickeron — MSFT FY Q3 2026 정리](https://tickeron.com/earnings/MSFT/)
- [247WallSt — MSFT Q3 2026](https://247wallst.com/companies/msft/earnings)
- [CNBC — Microsoft Q3 2026](https://www.cnbc.com/2026/04/29/microsoft-msft-q3-earnings-report-2026.html)
- [Yahoo — MSFT Q3 FY2026 컨콜 전사](https://finance.yahoo.com/quote/MSFT/earnings/MSFT-Q3-2026-earnings_call-547930.html)
- [Futurum — MSFT Q3 FY2026 분석](https://futurumgroup.com/insights/microsoft-q3-fy-2026-earnings-show-cloud-growth-with-capacity-still-tight/)
- [IG — Microsoft Q4 2026 프리뷰](https://www.ig.com/en/news-and-trade-ideas/microsoft-corp-q4-2026-earnings-preview--260721)
- [Trefis — Meta Q1 2026 캐펙스 상향](https://www.trefis.com/stock/meta/articles/598036/meta-platforms-8-6-raised-2026-capex-guidance-sparks-investor-concern/2026-05-02)
- [CoinDCX — Meta Q1 2026](https://coindcx.com/blog/us-stock/meta-q1-2026-earnings-results/)
- [CNBC — Meta Q1 2026](https://www.cnbc.com/2026/04/29/meta-q1-earnings-report-2026.html)
- [Fortune — Meta $145B 캐펙스](https://fortune.com/2026/04/29/meta-zuckerberg-145-billion-ai-spending-roi/)
- [Yahoo — Meta 캐펙스 상향(메모리 가격)](https://finance.yahoo.com/markets/stocks/articles/meta-just-bumped-2026-capex-232250811.html)
- [Motley Fool — Meta Q1 2026 컨콜 전사](https://www.fool.com/earnings/call-transcripts/2026/04/29/meta-meta-q1-2026-earnings-call-transcript/)
- [EarningsCall — Meta Q1 2026 요약](https://earningscall.biz/blog/meta-q1-2026-earnings-call)
- [Network World — 삼성, 메모리 가격 급등 경고](https://www.networkworld.com/article/4113772/samsung-warns-of-memory-shortages-driving-industry-wide-price-surge-in-2026.html)
- [KuCoin/SemiAnalysis·CLSA — 하이퍼스케일러 캐펙스 내 메모리 비중](https://www.kucoin.com/news/flash/memory-to-account-for-nearly-50-of-hyperscaler-capex-by-2027-per-semianalysis-and-clsa)
- [Tom's Hardware — 삼성·SK하이닉스 공급 부족 경고](https://www.tomshardware.com/tech-industry/artificial-intelligence/samsung-and-sk-hynix-warn-ai-driven-memory-shortages-could-last-until-2027-and-beyond-as-hbm-demand-explodes-customers-already-reserving-supply-years-ahead-while-the-wider-dram-market-begins-to-tighten)
- [NAND Research — 2026년 5월 메모리 위기 업데이트](https://nand-research.com/memory-nand-flash-crisis-may-2026-update/)
- [Tech-Insider — 2026 메모리 쇼티지](https://tech-insider.org/memory-chip-shortage-2026-ai-consumer-electronics/)
- [Luminix — DRAM 사이클 분석](https://www.useluminix.com/reports/industry-analysis/dram-cycle-position-analysis-peak-timing-indicators)
