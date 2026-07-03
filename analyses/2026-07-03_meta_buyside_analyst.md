---
title: "Meta 실적·컨콜 분석 — 바이사이드 애널리스트 관점"
date: 2026-07-03
target: "Meta"
persona: buyside_analyst
competitive: true
model: claude-fable-5
---

# Meta 최신 실적·컨콜 분석 — 바이사이드 애널리스트 관점

> **케이스 설정**
> - 페르소나: 반도체(메모리) 섹터 담당 기관투자자(바이사이드) 애널리스트
> - 분석 대상: Meta Platforms — **CY2026 1분기(2026.1~3월, 4/29 발표)**
> - 경쟁 분석: **ON** (Alphabet/Google, Microsoft, Amazon — 모두 같은 캘린더 분기)
> - 작성일: 2026-07-03
> - 분석 렌즈: Meta 자체의 투자 논거보다, **하이퍼스케일러 실적을 메모리(HBM/DRAM/NAND) 수요 사이클의 선행 신호로 읽는 관점**을 병행한다

### 데이터 신뢰도 경고

| 항목 | 등급 | 비고 |
|---|---|---|
| Meta 실적 수치 | **1차 사료 확보** | 회사 IR 보도자료(PR Newswire 전문), 10-Q(SEC), 회사 게시 컨콜 전사 PDF(q4cdn)로 확인 |
| Meta 컨콜 발췌 | 1차 전사 + 2차 매체 혼용 | 회사 전사 PDF에서 직접 발췌한 부분과 Fortune·CNBC 등 2차 매체가 전한 발언이 섞여 있다. **원문 1:1 전량 대조는 미완료** |
| Alphabet | 1차(실적 릴리스 PDF) + 2차 | ⚠️ 조정 EPS 해석이 매체 간 상충: CNBC는 "조정 EPS $2.62로 컨센($2.63) 소폭 하회"로, 일부 매체는 "$5.11이 컨센($2.62)의 두 배"로 보도. GAAP $5.11에는 투자 평가익이 들어 있어 CNBC 해석을 채택하되 **확인 필요** |
| Microsoft | 1차(공식 보도자료·8-K 링크 확인) + 2차 | ⚠️ 캐펙스 "1,900억 달러"가 **캘린더 2026 기준**이라는 보도(Global Data Center Hub)를 채택했으나 1차 사료 원문 대조 미완료. MS 회계연도(6월 결산)와 다르므로 주의 |
| Amazon | **2차 매체 교차 확인만** | ⚠️ IR 릴리스 원문 직접 대조 미완료. CNBC·TIKR·CoinDCX·QZ 4개 매체로 교차 확인. Jassy 발언은 2차 전사 인용 |
| 기타 ⚠️ | — | Alphabet 매출 성장률이 CNBC 본문(20%)과 공식 릴리스(22%, 환율 불변 19%)에서 다르다. 공식 릴리스를 채택. Meta 분기 중 신규 계약 약정 +1,070억 달러는 Digitimes 단독 보도 성격이라 확인 필요 |

### 기간 정합성 — 회계연도 vs 캘린더 매핑

| 회사 | FY 명칭 | 실제 기간 | 분기 종료일 | CY 매핑 |
|---|---|---|---|---|
| Meta | FY2026 Q1 (FY=CY) | 2026.1~3월 | 2026-03-31 | CY26 Q1 |
| Alphabet | FY2026 Q1 (FY=CY) | 2026.1~3월 | 2026-03-31 | CY26 Q1 |
| **Microsoft** | **FY2026 Q3** (6월 결산) | 2026.1~3월 | 2026-03-31 | CY26 Q1 |
| Amazon | FY2026 Q1 (FY=CY) | 2026.1~3월 | 2026-03-31 | CY26 Q1 |

네 회사 모두 **같은 캘린더 분기(CY26 Q1)** 를 보고했고 발표일도 2026-04-29로 같다. 시점차 조정은 필요 없다. 다만 Microsoft만 분기 명칭이 다르고, 연간 캐펙스 발언이 캘린더 기준인지 회계연도 기준인지 매체마다 표기가 달라 위 ⚠️를 유지한다.

---

## 1. Meta — 정량 요약

**손익 (CY26 Q1, 전년동기비)**

| 지표 | 실적 | 성장/비교 | 컨센서스 대비 |
|---|---|---|---|
| 매출 | $56.31B | +33% | IBES $55.45B 대비 약 +1.6% 상회 |
| Family of Apps 매출 | $55.91B (광고 ~$55B) | +33% | — |
| Reality Labs 매출 | $402M | -2% | 퀘스트 부진, AI 글라스는 일간 사용자 3배 |
| 영업이익 | $22.87B (마진 40.6%) | FoA +$26.90B / RL **-$4.03B** | — |
| 순이익 / GAAP EPS | $26.77B / $10.44 | +61% | **일회성 세제 혜택 $8.03B 포함**(제외 시 EPS $3.13 낮음) |
| 조정 EPS | $7.31 | +14% | LSEG $6.79 대비 **+7.7% 상회** |

**운영·현금흐름 지표**

| 지표 | 실적 | 비고 |
|---|---|---|
| DAP(일간 활동자) | 3.56B, +4% | **q/q 소폭 감소** — 이란 인터넷 차단, 러시아 WhatsApp 제한 탓. 컨센 하회 |
| 광고 노출량 / 단가 | +19% / +12% | 물량·가격 동반 성장 |
| 인당 매출(ARPP) | $15.66 | 컨센 $15.26 상회 (전분기 $16.56) |
| 영업현금흐름 | $32.2B | — |
| **분기 캐펙스**(파이낸스리스 포함) | **$19.84B** | 서버·데이터센터·네트워크 집중. 분기 수치는 컨센 하회 |
| 현금성 자산 / 장기부채 | $81.18B / $58.75B | 배당 $1.35B 지급 |
| 비해지성 계약 약정 | **$237.67B** | ⚠️ 분기 중 +$107B 증가 보도(Digitimes) — 확인 필요 |
| 헤드카운트 | 77,986명, +1% | 효율화 명분 감원 계획 보도(DCD) |

**가이던스**

| 항목 | 내용 |
|---|---|
| Q2 2026 매출 | $58~61B (중간값 성장 약 +25%, 환율 +2%p 순풍 가정) |
| FY26 총비용 | $162~169B — **기존 유지** |
| FY26 영업이익 | 2025년 영업이익 상회 목표 유지 |
| **FY26 캐펙스** | **$125~145B로 상향**(기존 $115~135B) — 사유: **부품 가격 상승(특히 메모리)** + 미래 용량용 데이터센터 비용 |
| 세율 | 잔여 분기 13~16% |

발표 직후 주가는 시간외에서 약 7% 내렸다. 매출·이익이 컨센을 넘었는데도, 시장은 캐펙스 상향과 유저 지표 부진에 더 무게를 뒀다.

---

## 2. Meta — 컨콜 정성(톤) 발췌 분석

**(1) 자신감 — 슈퍼인텔리전스 내러티브를 전면에 세웠다**

- ① 원문(회사 보도자료, Zuckerberg): *"We're on track to deliver personal superintelligence to billions of people."*
- ② 해석: 수십억 명에게 개인용 슈퍼인텔리전스를 전달하는 경로 위에 있다고 말했다. Meta Superintelligence Labs가 만든 첫 모델(Muse Spark)을 이번 분기 성과의 중심에 놓았다.
- ③ 시사점: 광고 실적이 아니라 AI 모델 진척을 분기 서사의 앞에 세웠다. 캐펙스 정당화 논리가 '광고 ROI'에서 '슈퍼인텔리전스 선점'으로 옮겨가는 중이다. 메모리 관점에서는 지출 하방 경직성을 높이는 신호다.

**(2) 투자 확신 + 실리콘 다변화 — 이번 컨콜에서 가장 중요한 대목**

- ① 원문(Fortune이 전한 Zuckerberg 발언, 원문 1:1 대조 미완료): *"Every sign that we're seeing in our own work and across the industry gives us confidence in this investment"*
- ② 해석: 자사 내부와 업계 전반에서 보는 모든 신호가 이번 투자에 확신을 준다고 했다. 이어서 Broadcom과 함께 개발한 자체 실리콘을 1기가와트 넘게 배치하고, Nvidia 신규 시스템을 보완하려고 AMD 칩도 대량 도입한다고 밝혔다.
- ③ 시사점: 지출 확신과 비용 효율화를 한 문장 안에 묶었다. GPU 공급선을 Nvidia 단일에서 Nvidia+AMD+자체 ASIC 3원 체제로 바꾸는 그림인데, 커스텀 ASIC도 HBM을 탑재하므로 **메모리 수요에는 중립 이상**이다. 오히려 고객 저변이 넓어진다.

**(3) 캐펙스 상향 사유 — '메모리 가격'을 이름 붙여 불렀다**

- ① 원문(실적 릴리스 문구, Tom's Hardware 인용): *"higher component pricing this year, particularly memory"*
- ② 해석: 캐펙스 상향분(구간 기준 +$10B)의 주 사유가 용량 확장이 아니라 **부품, 특히 메모리 가격 상승**이라고 못박았다.
- ③ 시사점: 메모리 애널리스트에게는 이번 시즌 최고 수위 발언이다. 구매자가 가격 인상을 받아들이고 예산을 늘렸다고 스스로 공시했다. DRAM 계약가 협상에서 공급자(삼성전자·SK하이닉스·마이크론) 우위가 재확인됐다.

**(4) 2027년 캐펙스 — 확신 속의 유보**

- ① 원문(회사 전사 PDF, Zuckerberg): *"we are, frankly, undergoing a very dynamic planning process"*
- ② 해석: 2027년 이후 용량 수요를 두고 매우 유동적인 계획 과정을 거치고 있다고 했다. 모델 출시 주기도 경쟁 정보라며 말을 아꼈고, 연구는 언제 성과가 나올지 모른다고 덧붙였다.
- ③ 시사점: 확신(투자 지속)과 유보(규모 미확정)를 같이 담았다. 2027년 가이던스가 나오는 10월~내년 1월 컨콜이 메모리 주문 가시성의 다음 분수령이다. 경쟁사(Alphabet·Microsoft)가 이미 2027년 증액을 예고한 점과 대비하면 Meta 톤이 상대적으로 조심스럽다.

**(5) 신중 신호 — 규제·유저 지표**

- ① 원문: 별도 인용 없음(보도자료 요지). 회사는 EU·미국 규제 역풍, 청소년 관련 재판에서 중대한 손실 가능성을 명시했고, DAP는 이란·러시아 요인으로 전분기보다 줄었다.
- ② 해석: 성장 서사와 별개로 법률 리스크 문단의 수위를 유지했고, 유저 감소를 외부 요인으로 설명했다.
- ③ 시사점: 광고 매출의 물량 엔진(노출량 +19%)이 유저 수가 아니라 체류시간·AI 추천에서 나온다는 구조를 재확인했다. 메모리 수요 관점의 직접 영향은 작다.

**(6) 분기 후 신호 — 컴퓨트 외판 가능성**

- ① 원문(CNBC, 5/27, Zuckerberg): 클라우드 사업 진출이 *"definitely on the table"*
- ② 해석: 남는 컴퓨트를 외부에 파는 클라우드 사업을 선택지에 올려놓았다고 말했다.
- ③ 시사점: 실현되면 Meta 인프라 투자가 '내부 소비형'에서 '매출 창출형'으로 바뀐다. 과잉 투자 우려를 되사는 카드이자, 인프라(=메모리) 구매의 상한을 한 단계 높일 재료다.

---

## 3. 경쟁 현황 — 정량 비교 (모두 CY26 Q1, 2026-03-31 종료 분기)

| 지표 | Meta | Alphabet | Microsoft (FY26 Q3) | Amazon | 핵심 차이(1줄) |
|---|---|---|---|---|---|
| 매출 / 성장 | $56.3B / +33% | $109.9B / +22% | $82.9B / +18% | $181.5B / +17% | 성장률은 Meta, 절대 규모는 Amazon 우위 |
| 매출 컨센 대비 | 상회 (+1.6%) | 상회 (+2.5%) | 상회 (+1.8%) | 상회 (+2.4%) | 네 회사 모두 매출 상회, 상회 폭은 대동소이 |
| 영업이익 / 마진 | $22.9B / 40.6% | $39.7B / 36.1% | $38.4B / 46.3% | $23.9B / 13.1%(사상 최고치) | 마진 수준은 MS 최고, 마진 개선 폭은 Amazon 최대 |
| 조정 EPS vs 컨센 | $7.31 vs $6.79 상회 | ⚠️ $2.62 vs $2.63 소폭 하회 | $4.27 vs $4.06 상회 | $2.78 vs $1.65 상회(Anthropic 평가익 $16.8B 포함) | EPS 서프라이즈의 질은 MS가 가장 깨끗, Meta·Amazon은 일회성 항목 포함 |
| 클라우드·핵심 성장축 | FoA 광고 +33% | Cloud $20.0B **+63%**, 백로그 $462B | Azure **+40% cc**(5분기 연속 가속), AI 런레이트 $37B+ | AWS $37.6B +28%(15분기 최고), AWS 영업이익 $14.2B | 클라우드 성장 속도 Google > MS > AWS, Meta만 클라우드 부재 |
| 분기 캐펙스 | $19.8B | $35.7B(약 2배 증가) | $31.9B(+49%, 컨센 하회) | $43.2B | 절대 지출은 Amazon 최대, Meta는 4사 중 최소 |
| 2026 연간 캐펙스 | $125~145B(상향) | $180~190B(상향), 2027 대폭 증액 예고 | 약 $190B(⚠️CY 기준, 컨센 $154.6B 대비 +$35B) | 약 $200B | 상향 서프라이즈 폭은 MS 최대, 절대 규모는 Amazon 최대 |
| 메모리·부품 발언 | 상향 사유로 "메모리" 명시 | 부품 직접 언급보다 공급 제약·2027 증액 강조 | **$25B를 부품(메모리) 인플레로 명시 계량** | 메모리·스토리지 비용 급등 언급, 파트너십으로 물량 선확보 | 메모리 인플레를 숫자로 밝힌 회사는 MS( $25B)가 유일 |
| 커스텀 실리콘 | MTIA(Broadcom) 1GW+ 배치, AMD 병행 | TPU — **하드웨어 외판 개시**, 백로그에 반영 | Maia 200(TSMC 3nm)·Cobalt 확산 | Trainium — 실리콘 사업 런레이트 $20B+, q/q +40% | 실리콘의 '사업화'는 Amazon·Google이 앞서고 Meta·MS는 내부 효율용 |
| 발표 후 주가 | 시간외 -7% | 시간외 +7% | 다음날 -3.9% | 시간외 -2% 안팎 | 같은 캐펙스 상향인데 클라우드 매출 증거가 있는 Alphabet만 보상받음 |

> 4사 합산 CY2026 캐펙스는 약 $725B로 전년보다 77% 늘어난다는 집계(Tom's Hardware)가 있다. TrendForce 기준 Q1 DRAM 계약가는 q/q 약 +95%, Q2는 +58~63% 전망, NAND Q2는 +70~75% 전망이며 2026년 NAND 생산분은 전량 선약정됐다는 보도가 있다.

---

## 4. 경쟁 현황 — 정성(톤) 비교

| 축 | Meta | Alphabet | Microsoft | Amazon | 핵심 차이(1줄) |
|---|---|---|---|---|---|
| 톤·자신감 | 확신 상향 — "모든 신호가 투자 확신을 준다"(§2-(2)) | 확신 최고조 — Pichai: *"Our enterprise AI solutions have become our primary growth driver for cloud for the first time in Q1"* | 확신 유지·비용 방어 — AI 마진이 초기 클라우드보다 낫다고 강조 | 확신 상향 — Jassy: *"in the middle of some of the biggest inflections of our lifetime"* | 매출 증거로 말하는 Alphabet·Amazon, 미래 서사로 말하는 Meta |
| 내러티브 중심 | 개인용 슈퍼인텔리전스 + 자체 모델(Muse Spark) | 풀스택(모델+TPU+클라우드) — Pichai: *"revenue from products built on our gen AI models grew nearly 800% year-over-year"* | Copilot·Azure AI 수익화 + 실리콘 내재화 | AWS 재가속 + OpenAI 계약 확대 + 자체 칩 사업화 | Meta만 '외부 판매 없는 내부 투자' 서사 — 그래서 시장이 가장 박하게 평가 |
| 공급관(용량 제약) | 용량 계획 유동적, 2027 미확정(§2-(4)) | 공급 제약이 성장의 관문이라고 인정, 백로그 $462B — Ashkenazi: *"just over half of it will convert to revenue in the next 24 months"* | GPU·CPU·스토리지 제약이 2026년 내내 지속된다고 명시(Tom's Hardware 전언) | 공급을 파트너십으로 선확보했다고 강조 | 4사 모두 '수요 > 공급' 인정 — 공급자 우위 사이클 지속 신호 |
| 가격·비용 구조 | 메모리 인플레를 캐펙스 상향 사유로 명시 | 부품보다 용량·감가상각 중심 화법 | Hood: *"The sequential increase includes roughly $5 billion from higher component pricing"* — 인플레를 분기 단위로 계량 | 메모리·스토리지 급등 인정, 지속되면 마진 위험이라고 유보 | 부품 인플레 수용도: MS·Meta 명시 > Amazon 유보 > Alphabet 침묵 |
| 점유율 태도 | 광고 점유 방어보다 AI 선점 공세 | 검색 방어 성공 선언(Search +19% 가속) + 클라우드 공세 | Azure 가속으로 AWS 추격 공세 | 수성 — AWS 재가속과 OpenAI $100B 증액 계약으로 리더십 재확인 | 클라우드 3사는 상호 공세, Meta는 다른 링(광고·AI)에서 경기 중 |
| 투자 기조 | 상향하되 2027은 유보 | 상향 + 2027 대폭 증액 선예고 | 상향 폭 최대(컨센 +$35B), 분기 $40B+ 예고 | 절대 규모 최대($200B), FCF 압박 감수 명시 | 지출 규율 신호는 4사 어디에도 없다 — 다운사이클 트리거 아직 부재 |

---

## 5. 바이사이드 애널리스트를 위한 임플리케이션

**렌즈 1. 가이던스 대비 실적 — 서프라이즈의 질을 가려 읽어야 한다**
- Meta는 매출·조정 EPS 모두 상회했으나, GAAP EPS 급증($10.44)은 세제 혜택 $8.03B가 만든 착시다. 반복 가능한 서프라이즈는 광고 단가 +12%와 노출량 +19%의 동반 성장뿐이다.
- 네 회사 모두 매출을 상회하고도 세 회사 주가가 내렸다. 시장의 채점 기준이 이미 손익에서 **캐펙스·FCF 궤적**으로 옮겨갔다. 메모리 업체를 볼 때도 같은 기준을 적용해야 한다. 매출 서프라이즈보다 '가격 수용성의 지속 기간'이 멀티플을 결정한다.

**렌즈 2. 마진 구조 — 가격 효과와 물량 효과의 분해**
- 이번 시즌의 핵심 발견: 하이퍼스케일러 캐펙스 상향분의 상당 부분이 **물량(용량)이 아니라 가격(부품 인플레)** 이다. Microsoft는 $25B, Meta는 상향분 $10B의 주 사유를 메모리 가격이라고 밝혔다.
- 메모리 3사에 주는 함의는 이중적이다. (+) ASP 인상을 최대 구매자가 공개적으로 수용했다 — Q1 DRAM 계약가 +95% q/q라는 외부 집계와 정합한다. (−) 캐펙스 총액 성장률(+77%)을 비트 수요 성장률로 직역하면 안 된다. 가격 인플레 부분을 걷어낸 실질 물량 성장은 그보다 낮다.
- 계약 구조 관점에서는 Amazon의 '전략적 파트너십을 통한 물량 선확보', NAND 2026년 생산분 전량 선약정 보도가 중요하다. 장기·고정성 계약 비중이 커질수록 메모리 업체의 다음 다운사이클 방어력이 높아진다. LTA(장기공급계약) 조건 공시를 추적 항목으로 올린다.

**렌즈 3. 캐펙스·공급 규율 — 다음 다운사이클의 트리거 점검**
- 현재 확인되는 트리거는 없다. 4사 모두 상향했고, Alphabet·Microsoft는 2027년 추가 증액까지 예고했다. Meta의 비해지성 약정 $237.67B는 지출의 하방 경직성을 계약으로 굳혔다.
- 다만 선행 경계 신호 세 가지를 상시 점검한다. ① **감가상각 파도** — 동시 투자가 2027~28년 손익을 일제히 누른다(Global Data Center Hub 지적). FCF 압박이 임계치를 넘으면 지출 규율이 갑자기 등장한다. ② **부품 인플레의 수요 파괴** — 하이퍼스케일러가 소비자 DRAM·NAND 물량을 밀어내는 구조라, PC·모바일 수요 훼손이 사이클 왜곡을 만들 수 있다. ③ **Meta의 2027 유보** — 4사 중 유일하게 2027년 증액을 확언하지 않았다. Meta가 처음으로 '효율'을 말하는 순간(감원 보도는 그 예고편일 수 있다)이 사이클 톤 전환의 조기 경보다.
- 커스텀 실리콘 확산(MTIA·Maia·Trainium·TPU)은 Nvidia 물량 배분에는 변수지만, HBM 수요에는 중립 이상이다. ASIC도 HBM을 탑재하며, 구매 주체가 늘어날수록 메모리 협상 상대가 다변화된다. Broadcom 라인(Meta MTIA, Google TPU)의 HBM 조달처 추적이 필요하다.

**렌즈 4. 경영진 톤 변화 — 말과 숫자의 괴리**
- Meta: 말(슈퍼인텔리전스 확신)과 숫자(RL 분기 손실 $4.03B, DAP q/q 감소, FCF 압축)의 괴리가 4사 중 가장 크다. 시장은 그 괴리에 -7%로 답했다. 다만 메모리 수요 관점에서는 괴리가 클수록 지출이 늘므로 나쁘지 않다.
- Alphabet: 말과 숫자가 가장 잘 붙는다. 클라우드 +63%, 백로그 $462B, TPU 외판이라는 매출 증거가 캐펙스를 정당화했고, 홀로 주가 보상을 받았다.
- Microsoft: 톤은 차분하나 숫자가 가장 공격적이다(컨센 대비 +$35B). 부품 인플레를 계량 공시한 유일한 회사로, 메모리 가격 전망의 벤치마크 발언으로 삼을 만하다.
- Amazon: 낙관 톤과 사상 최고 마진이 일치하나, 인플레 지속 시 마진 위험이라는 유보를 남겼다. 4사 중 처음으로 '비용 전가의 한계'를 시사한 발언이라 다음 분기 톤 변화를 주시한다.

**렌즈 5. 상대 밸류에이션 — 멀티플 근거의 변화**
- 하이퍼스케일러 내부: 같은 캐펙스 상향이라도 '클라우드 매출 증거 보유'(Alphabet·Amazon)와 '내부 소비형'(Meta·Microsoft Copilot 초기 단계)의 멀티플 차별화가 진행 중이다. Meta 멀티플 회복의 조건은 컴퓨트 외판("definitely on the table") 구체화 또는 2027 캐펙스와 ROI 증거의 동시 제시다.
- 메모리 3사: 이번 시즌은 프리미엄 근거를 강화했다. 구매자가 가격을 수용하고, 공급 제약을 인정하고, 2027년 증액을 예고했다. HBM·서버 DRAM 노출이 큰 SK하이닉스, 가격 탄력이 큰 마이크론에 유리한 조합이다. 다만 계약가 급등 구간의 피크 멀티플 압축 위험을 감안해, '가격 모멘텀'보다 '약정 물량·기간'을 상대 비교 축으로 삼는다.

## 6. 한 줄 결론

Meta의 CY26 Q1은 광고가 낸 깨끗한 비트(매출 +33%)보다 "캐펙스 상향의 사유가 메모리 가격"이라는 공시 한 줄이 더 중요했다 — 4사 캐펙스 $725B 시대에 하이퍼스케일러는 메모리 가격의 수용자가 됐고, 이는 메모리 3사 강세 논거를 계약으로 굳히는 신호이되, 물량과 가격을 분해하지 않은 낙관은 금물이다.

### 출처

**Meta (1차)**
- [Meta Reports First Quarter 2026 Results — PR Newswire(회사 보도자료)](https://www.prnewswire.com/news-releases/meta-reports-first-quarter-2026-results-302757852.html)
- [Meta Q1 2026 Earnings Call Transcript — 회사 게시 PDF(q4cdn)](https://s21.q4cdn.com/399680738/files/doc_financials/2026/q1/META-Q1-2026-Earnings-Call-Transcript.pdf)
- [Meta 10-Q (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/0001326801/000162828026028526/meta-20260331.htm)
- [Meta IR 보도자료 페이지](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/d)

**Meta (2차)**
- [CNBC — Meta Q1 2026 earnings report](https://www.cnbc.com/2026/04/29/meta-q1-earnings-report-2026.html)
- [StockTitan — META 10-Q 요약](https://www.stocktitan.net/sec-filings/META/10-q-meta-platforms-inc-quarterly-earnings-report-3bd7ce5dd651.htm)
- [TIKR — Meta Q1 2026 분석](https://www.tikr.com/blog/meta-platforms-q1-2026-33-revenue-growth-as-ai-investment-hits-145b)
- [Fortune — Meta capex $145B](https://fortune.com/2026/04/29/meta-zuckerberg-145-billion-ai-spending-roi/)
- [Motley Fool — Meta Q1 2026 컨콜 전사](https://www.fool.com/earnings/call-transcripts/2026/04/29/meta-meta-q1-2026-earnings-call-transcript/)
- [Digitimes — Meta 1Q26 하드웨어 공급망 분석](https://www.digitimes.com/news/a20260430VL219/meta-2026-earnings-hardware-infrastructure.html)
- [heygotrade — Meta Q1 2026 리액션](https://www.heygotrade.com/en/blog/meta-q1-2026-earnings-reaction/)
- [Global Data Center Hub — Meta $145B 리셋](https://www.globaldatacenterhub.com/p/meta-q1-2026-the-145b-reset-and-the)
- [DCD — Meta 캐펙스 상향·감원 계획](https://www.datacenterdynamics.com/en/news/meta-raises-planned-capex-for-2026-plans-layoffs-for-efficiency-reasons)
- [CNBC — Zuckerberg, 클라우드 사업 "on the table" (5/27)](https://www.cnbc.com/2026/05/27/mark-zuckerberg-says-meta-starting-cloud-business-on-the-table.html)

**Alphabet**
- [Alphabet Q1 2026 실적 릴리스 PDF(회사 게시)](https://s206.q4cdn.com/479360582/files/doc_financials/2026/q1/2026q1-alphabet-earnings-release.pdf)
- [CNBC — Alphabet Q1 2026 earnings](https://www.cnbc.com/2026/04/29/alphabet-googl-q1-2026-earnings.html)
- [9to5Google — Alphabet Q1 2026](https://9to5google.com/2026/04/29/alphabet-q1-2026-earnings/)
- [Google 블로그 — Pichai 실적 메시지](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q1-2026/)
- [Motley Fool — Alphabet Q1 2026 컨콜 전사](https://www.fool.com/earnings/call-transcripts/2026/04/29/alphabet-googl-q1-2026-earnings-call-transcript/)
- [heygotrade — Alphabet Q1 2026 리액션](https://www.heygotrade.com/en/blog/alphabet-q1-2026-earnings-reaction/)

**Microsoft**
- [Microsoft 공식 보도자료 — FY26 Q3](https://news.microsoft.com/source/2026/04/29/microsoft-cloud-and-ai-strength-fuels-third-quarter-results/)
- [Microsoft 8-K (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526191457/msft-ex99_1.htm)
- [CNBC — Microsoft $190B capex, 메모리 가격](https://www.cnbc.com/2026/04/29/microsoft-msft-q3-earnings-report-2026.html)
- [Tom's Hardware — 빅테크 캐펙스 $725B와 메모리 인플레](https://www.tomshardware.com/tech-industry/big-tech/microsoft-attributed-25-billion-of-its-record-ai-budget-to-memory-chip-costs)
- [Global Data Center Hub — Microsoft $190B 캐펙스 플랜](https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex)
- [Fortune — MS·Meta·Google 캐펙스 비교](https://fortune.com/2026/04/29/microsoft-meta-google-ai-capex-spending-billions/)

**Amazon**
- [CNBC — AWS Q1 2026](https://www.cnbc.com/2026/04/29/aws-earnings-q1-2026.html)
- [QZ — Amazon Q1 2026](https://qz.com/amazon-q1-2026-earnings-aws-cloud-growth-042926)
- [TIKR — Amazon 사상 최고 영업마진](https://www.tikr.com/blog/amazon-posts-181-5b-revenue-and-highest-operating-margin-in-company-history)
- [CoinDCX — Amazon Q1 2026 결과](https://coindcx.com/blog/us-stock/amazon-q1-2026-earnings-results/)
