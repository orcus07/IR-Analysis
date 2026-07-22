---
title: "Super Micro Computer 실적·컨콜 분석 — SK하이닉스 마케터 관점"
date: 2026-07-22
target: "Super Micro Computer"
persona: sk_hynix_marketer
scope: both
competitive: true
model: claude-fable-5
---

# Super Micro Computer 최신 실적·컨콜 분석 — SK하이닉스 마케터 관점

> **케이스 설정**
> - **페르소나**: SK하이닉스 메모리(HBM/DRAM/NAND) 마케팅 담당자
> - **분석 대상**: Super Micro Computer(SMCI) — FY2026 3분기(2026년 3월 31일 종료, 5월 5일 발표) + 오늘(7월 22일) 공개된 FY2026 4분기 예비 실적
> - **경쟁 분석**: ON — Dell Technologies(FY2027 1분기), HPE(FY2026 2분기)
> - **작성일**: 2026-07-22

### 데이터 신뢰도 경고

- **1차 사료 확보**: SMCI 실적 보도자료(IR)와 회사가 게시한 컨콜 준비 발언 PDF, SMCI FY26 4분기 예비 실적 공지(IR), Dell 보도자료(자사 뉴스룸·SEC 8-K 첨부), HPE 보도자료(IR PDF)를 확보했다.
- **컨콜 전문은 2차 전사에 의존**: SMCI·Dell·HPE 컨콜 발췌는 Investing.com, Motley Fool, Yahoo Finance 등 2차 전사를 썼다. **원문 1:1 대조는 미완료**다. 실제로 2차 전사에는 오탈이 있다. 예컨대 Investing.com 전사는 SMCI 가이던스를 "first quarter"로 적었으나, 회사 공식 준비 발언 PDF는 "For the fourth quarter, we target $12 billion given stable supply conditions."라고 명기했다. 본 보고서는 공식 PDF를 우선했다.
- **컨센서스 집계 기관**: SMCI는 Investing.com 집계(매출 $12.39B, 비GAAP EPS $0.62)와 CNBC 집계(매출 약 $12.33B)·Bloomberg 집계(비GAAP 매출총이익률 6.75%)를 병기했다. Dell은 LSEG와 Zacks, HPE는 CNBC 인용 컨센서스를 썼다.
- **⚠️ 확인 필요 항목**:
  - SMCI 발표 직후 주가 반응이 매체마다 다르다(시간외 +1.18% vs 시간외 약 +18% vs 발표 후 +24.5%). 시점 차이로 보이나 확인이 필요하다.
  - Dell AI서버 매출의 YoY 증가율이 상충한다(Futurum +757% vs Blocks & Files +291.7%). 본문에서는 금액($16.1B)만 쓴다.
  - HPE FY27 프레임의 "operating margins of 12% to 16%" 표현은 1차 사료 대조가 안 됐다. '영업이익 성장률'의 오기 가능성이 있어 확인이 필요하다.
  - Dell FQ1'27 분기 종료일(5월 1일 추정)은 1차 사료에서 날짜를 직접 확인하지 못했다.
  - SMCI 4분기 예비치는 확정 실적이 아니다. 확정 실적과 컨콜은 8월 11일에 나온다.

### 기간 정합성 — 회계연도 vs 캘린더 매핑

| 회사 | FY 명칭 | 실제 기간 | 분기 종료일 | CY 매핑 |
|---|---|---|---|---|
| SMCI | FY2026 Q3 | 2026년 1~3월 | 2026-03-31 | CY26 1분기 |
| SMCI(예비) | FY2026 Q4 | 2026년 4~6월 | 2026-06-30 | CY26 2분기 |
| Dell | FY2027 Q1 | 2026년 2~5월 초 | 2026-05-01 추정 ⚠️ | CY26 2~4월 |
| HPE | FY2026 Q2 | 2026년 2~4월 | 2026-04-30 | CY26 2~4월 |

> **시점차 주의**: SMCI 3분기는 3월 말에 끝나 Dell·HPE보다 약 한 달 이르다. 다만 SMCI는 오늘 6월 분기(CY26 2분기) 예비치를 냈으므로, 이를 함께 보면 세 회사의 시점이 대체로 맞춰진다.

## 1. Super Micro Computer — 정량 요약

**FY2026 3분기 (2026-03-31 종료, 5월 5일 발표)**

| 지표 | FQ3'26 실적 | 전분기(FQ2'26) | 전년동기(FQ3'25) | 컨센서스 | 판정 |
|---|---|---|---|---|---|
| 매출 | $10.2B | $12.7B | $4.6B (+123% YoY) | $12.39B(Investing.com) | **하회(약 -18%)** |
| GAAP 매출총이익률 | 9.9% | 6.3% | 9.6% | — | — |
| 비GAAP 매출총이익률 | 10.1%* | 6.4% | 9.7% | 6.75%(Bloomberg) | **상회*** |
| GAAP 순이익 | $483M | $401M | $109M | — | — |
| GAAP 희석 EPS | $0.72 | $0.60 | $0.17 | — | — |
| 비GAAP 희석 EPS | $0.84 | — | $0.31 | $0.62 | **상회(+35%)** |
| 영업현금흐름 | -$6.6B(유출), 설비투자 $97M | 약 -$24M | — | — | **대규모 유출 ⚠️** |

\* **주의(깨끗한 서프라이즈 아님)**: 이번 마진 반등에는 전분기 대비 소멸한 비용 요인이 섞였다. Motley Fool 전사에 따르면 마진 개선은 "improved customer and product mix, and reduced tariffs, expedite, and inventory reserve charges" 때문이다. 즉 고객·제품 믹스 개선에 더해 관세·긴급운송·재고평가 충당 비용이 줄어든 효과가 컸다. 구조적 마진 개선과 일회성 완화 효과를 나눠 봐야 한다.

**가이던스와 4분기 예비 실적**

| 항목 | 회사 가이던스(5/5 제시) | 시장 기대 | 예비 실적(7/22 공개) |
|---|---|---|---|
| FQ4'26 매출 | $11.0~12.5B | $11.07B(CNBC 인용) | 가이던스 하단 부근 |
| FQ4'26 비GAAP EPS | $0.65~0.79 | $0.55(CNBC 인용) | 8/11 발표 예정 |
| FQ4'26 매출총이익률 | 8.2~8.4% | — | **15~17%로 대폭 상회**(우호적 고객·제품 믹스) |
| FY26 연간 매출 | $38.9~40.4B | — | — |
| 수주 | — | — | 4분기에만 신규 수주 $60B 초과, 백로그 사상 최대 |

## 2. Super Micro Computer — 컨콜 정성(톤) 발췌 분석

*아래 발췌는 2차 전사(투자매체) 기반이며 원문 1:1 대조는 미완료다. 회사 공식 PDF에서 확인한 발언은 별도 표기했다.*

**① 성장 자신감 — 목표 숫자를 직접 제시**
- 원문(공식 PDF): "For the fourth quarter, we target $12 billion given stable supply conditions." 연간으로는 400억 달러를 목표한다고 밝혔다.
- 원문(2차 전사): "I remain very bullish about our growth in the AI and data center market."
- 해석: 매출이 컨센서스를 18% 밑돌았는데도 CEO는 목표 숫자를 물리지 않았다. 다만 "공급이 안정된다면"이라는 단서를 달았다.
- 시사점: 서버 조립 최상위권 업체가 분기 120억 달러 매출을 공언한다. 이 물량이 소화할 서버 DRAM·eSSD 수요는 그만큼 커진다. 동시에 '공급 단서'는 부품 공급자가 협상 지렛대를 쥐고 있다는 증거다.

**② 매출 미스의 원인 — 수요가 아니라 '현장 준비'와 부품**
- 원문: "Several customers were not yet equipped with the power and networking required for their cloud deployment"
- 해석: 고객 데이터센터의 전력·네트워킹이 늦어 매출 인식이 밀렸다고 설명했다. 수요 소멸이 아니라 이연이라는 프레임이다.
- 시사점: AI 인프라 병목이 GPU에서 전력·냉각·현장 준비로 옮겨 간다. 메모리 수요의 분기별 출렁임은 커질 수 있으나, 총량은 유지된다. 분기 단위 주문 변동에 과민할 필요가 없다.

**③ 공급관 — 메모리를 병목으로 지목**
- 근거(2차 매체 요약): CFO는 업계 전반의 공급 제약이 실적을 깎았다고 말했고, CEO는 메모리 가격이 급등했고 GPU·인텔 CPU도 부족하다고 말했다. (CNBC 기사 요약이며 축어 인용 아님)
- 원문(CFO): "we expect some challenge going forward, but not like we incurred over the last six months"
- 해석: 지난 6개월이 가장 힘들었고, 앞으로도 제약은 남지만 완화를 기대한다는 톤이다.
- 시사점: 고객이 어닝콜에서 '메모리 가격 급등'을 실적 변수로 공식 언급했다. 가격 인상이 시장에 정착했다는 뜻이다. 다만 CFO의 '완화 기대'는 하반기 협상에서 인상 폭 저항 논리로 쓰일 수 있다.

**④ 마진·사업 모델 — 두 자릿수 마진 공약과 DCBBS**
- 원문: "We are committed to achieving a sustainable double-digit gross margin model"
- 근거: 엔터프라이즈 시장과 DCBBS(Data Center Building Block Solutions)에 집중해 마진을 높이겠다고 했고, 네오클라우드·소버린 AI·에이전틱 AI 부문 수요가 매우 강하다고 밝혔다. 소프트웨어 매출은 몇 분기 전 분기당 1,000만 달러 미만에서 지난 분기 3,400만 달러, 이번 분기 4,600만 달러 이상 수주로 늘었다.
- 해석: 하드웨어 조립 마진에서 소프트웨어·서비스 동반 판매로 이익 구조를 바꾸는 중이다. 실제로 4분기 예비 마진 15~17%가 나오면서 이 공약은 조기에 숫자로 증명됐다.
- 시사점: 고객의 지불 여력이 커졌다. 시스템 업체가 마진을 두 배 가까이 늘리는 국면이라면, 메모리 가격 인상분을 최종 가격에 전가할 공간도 그만큼 넓다.

**⑤ 로드맵 — 차세대 플랫폼 선점 경쟁**
- 원문: "We are preparing to be among the first to market with the new Vera Rubin systems"
- 근거: GB300 NVL72, B300 HGX, B200 NVL4 등 최신 랙스케일 시스템을 다수 출하 중이라고 밝혔다.
- 해석: NVIDIA 차세대 플랫폼의 '최초 출시(first to market)' 지위를 마케팅 핵심으로 삼는다.
- 시사점: Vera Rubin 세대는 HBM4 채용 세대다. 시스템 업체의 '최초 출시' 경쟁은 곧 HBM4 조기·대량 확보 경쟁이다. 플랫폼 전환 일정에 맞춘 선행 영업이 필요하다.

**⑥ 회사 정체성 — '토털 데이터센터 인프라' 서사**
- 원문(보도자료): "Supermicro's transformation into a total datacenter infrastructure provider is accelerating"
- 해석: 서버 조립사가 아니라 데이터센터 인프라 전체를 파는 회사라는 서사를 민다. 한편 이번 분기 영업현금흐름은 66억 달러 유출로, 성장 자금 부담(부품 선구매·재고)이 크다는 이면도 드러났다.
- 시사점: 현금이 빠듯한 고객은 결제 조건·선급 구조에 민감하다. 공급 계약 설계 시 물량 커밋과 대금 조건을 함께 다뤄야 한다.

## 3. 경쟁 현황 — 정량 비교

> **시점차 고지**: SMCI는 3월 말 종료 분기(+6월 분기 예비치), Dell·HPE는 4월 말~5월 초 종료 분기다. 직접 비교 시 약 한 달의 시차가 있다.

| 지표 | SMCI (FQ3'26) | Dell (FQ1'27) | HPE (FQ2'26) | 핵심 차이(1줄) |
|---|---|---|---|---|
| 매출 / YoY | $10.2B / +123% | $43.84B / +88% | $10.68B / +40% | 절대 규모는 Dell, 성장률은 SMCI가 앞섬 |
| 컨센서스 대비 | 매출 -18% 하회, EPS +35% 상회 | EPS +59.9%·매출 +23.6% 상회(Zacks) | EPS $0.79 vs $0.53, 매출 $10.68B vs $9.79B 상회 | SMCI만 매출 미스, Dell·HPE는 전면 상회 |
| AI서버 매출 | 별도 미공시(NVIDIA GPU 플랫폼이 매출의 80% 이상) | $16.13B | 미공시(AI 시스템 신규 수주 $1.8B) | AI서버 매출 규모는 Dell이 압도 |
| 수주·백로그 | FQ4에 신규 수주 $60B+, 백로그 사상 최대 | AI 수주 $24.4B, AI 백로그 $51.3B 사상 최대 | 주문 2배 이상 증가, 회사 전체 백로그 사상 최대 | 세 회사 모두 백로그 신기록 — 수요>공급 공통 |
| 매출총이익률(비GAAP) | 10.1%(FQ4 예비 15~17%) | 별도 미공시(영업이익률 9.66%) | 36.9%, 전년比 +750bp 기록 | 마진 수준은 HPE, 마진 개선 속도는 SMCI |
| 비GAAP EPS / YoY | $0.84 / +171%($0.31→) | $4.86 / +214% | $0.79 / +108%(전년 $0.38) | 세 회사 모두 세 자릿수 이익 성장 |
| 차기 분기 가이던스 | 매출 $11.0~12.5B | 매출 $44~45B(약 +50%), ISG +75% | 매출 $11.5~12.1B | 성장 지속 가이던스는 공통, 상향 폭은 Dell 최대 |
| 연간 가이던스 | FY26 매출 $38.9~40.4B | FY27 매출 $165~169B·EPS $17.90(LSEG 기대 $142.5B·$13.09 대폭 상회), AI서버 $60B로 상향 | FY26 비GAAP EPS $3.35~3.45로 상향, FCF $3.5B+ | Dell은 연 매출 $27B 상향, HPE는 장기목표 조기 달성 |
| 현금흐름 | 영업현금 -$6.6B | 영업현금 +$4.1B 분기 기록 | FCF +$915M(+$1.8B 개선) | SMCI만 대규모 현금 유출 — 재고·선구매 부담 |
| 메모리 관련 언급 | 메모리 가격 급등을 실적 변수로 지목 | 최대 제약은 메모리(DRAM·NAND)와 CPU라고 명시 | 메모리 원가 상승이 2026년 내내 지속된다고 언급(FQ1 콜) | 세 회사 모두 메모리를 최상위 병목으로 공인 |

## 4. 경쟁 현황 — 정성(톤) 비교

| 축 | SMCI | Dell | HPE | 핵심 차이(1줄) |
|---|---|---|---|---|
| 톤·자신감 | 매출 미스에도 목표 유지. "I remain very bullish…"라며 목표 숫자를 반복함 | 기록 경신을 나열하는 확신형. "our pipelines have never been healthier, they're actually growing at greater than historical rates"라며 가이던스 상향을 정당화함 | 자체 전망 초과를 강조하는 상향형. "Our large backlog, favorable industry tailwinds, and improved demand visibility support a higher growth outlook."이라 말함 | SMCI는 '방어적 낙관', Dell은 '증명된 확신', HPE는 '초과 달성 서사' |
| 수요 내러티브 | 네오클라우드·소버린 AI·에이전틱 AI가 견인한다고 말함 | AI 고객 5,000곳 초과, 6개월 새 50% 이상 증가라고 말함, "We booked $24.4 billion in AI orders and recognized $16.1 billion of AI server revenue." | "Traditional server orders increased triple digits"이라며 AI와 전통 서버 동반 수요를 말함, 보안 중시 산업의 온프렘 AI 가속을 말함 | SMCI는 신흥 세그먼트, Dell은 고객 수 확장, HPE는 온프렘·전통 서버 부활 |
| 공급관(메모리·부품) | 메모리 가격 급등과 GPU·인텔 CPU 부족을 말함 | 수요가 공급을 계속 앞서며 메모리 등 부품이 최대 제약이라고 말함 | "on the memory cost increases, we will continue to see that throughout 2026"이라 말함(FQ1'26 콜, 3월) | 세 회사 모두 메모리 병목을 공인 — 표현 강도는 Dell이 가장 높음 |
| 가격 구조·전가 | 가격 정책 직접 언급은 확인 못 함(⚠️). 다만 FQ4 마진 15~17% 예비치로 전가+믹스 개선을 방증함 | "we are repricing it feels like every day. And I am sure our customers feel that pain."이라며 상시 재가격을 말함 | 기록적 매출총이익률 36.9%로 원가 상승 속 마진 방어를 보여줌 | Dell은 '일 단위 재가격'을 공개 선언 — 인상 전가가 가장 공격적 |
| 점유율·경쟁 태도 | "We are preparing to be among the first to market with the new Vera Rubin systems"라며 신플랫폼 선점을 말함 | "folks are trying to secure that supply now and over multiple years because it is going to be more constrained"이라며 다년 물량 선점 수요를 말함 | "the combination of networking, compute, storage, and memory positions HPE competitively"라며 포트폴리오 결합 우위를 말함 | SMCI는 속도, Dell은 공급 확보력, HPE는 포트폴리오 폭으로 경쟁함 |
| 투자·재무 기조 | 영업현금 -$6.6B로 성장에 현금을 쏟아붓는 기조를 보임 | 기록적 현금창출($4.1B)과 주주환원 $2.1B를 병행함 | FY26 말 2x 순레버리지 조기 달성 후 FCF의 75% 이상 환원을 말함 | SMCI는 현금 소진형 성장, Dell·HPE는 성장+환원 병행 |
| 리스크 단서 | "given stable supply conditions"라는 조건부 단서를 닮 | "we are living in an inflationary environment that is changing at a rate that obviously we have never seen before"라며 인플레 지속을 말함 | 수요 선반영(pull-in) 증거는 없다고 말함 | 셋 다 수요보다 공급·원가를 위험으로 지목함 |

## 5. SK하이닉스 마케터를 위한 임플리케이션

**(1) 방어 — 경쟁 위협 신호**
- 고객(서버 OEM) 3사가 모두 메모리를 최대 병목으로 공식화했다. Dell은 고객이 "지금, 그리고 다년에 걸쳐" 공급을 확보하려 한다고 말했다. 다년 계약 수요는 기회이지만, 고정가 요구로 이어지면 상승 사이클의 수익을 스스로 잠그는 결과가 된다. 다년 '물량' 커밋과 '가격' 커밋을 분리해 대응해야 한다.
- SMCI CFO는 공급 제약이 지난 6개월만큼 나쁘지는 않으리라고 말했다. 고객이 하반기 협상에서 '공급 완화' 논리로 인상 폭을 깎으려 들 수 있다. 국내 매체가 짚었듯 2026~2027년 신규 캐파는 HBM에 우선 배정되고 범용 D램 증산은 공정 전환에 의존해 부족이 이어질 전망이므로, 공급 데이터로 반박 논리를 준비해야 한다.

**(2) 공세 — 마케팅 기회**
- 백로그가 수요 가시성을 보증한다. SMCI는 한 분기에 신규 수주 600억 달러를 넘겼고, Dell은 AI 백로그 513억 달러, HPE는 회사 전체 백로그 신기록을 말했다. 서버향 DRAM·eSSD 수요는 최소 4~6분기 이상 견조하다는 뜻이다. '공급 확실성'을 프리미엄 가치로 팔 국면이다. SMCI의 "given stable supply conditions"라는 단서가 그 증거다. 고객의 매출 가이던스 달성이 우리 공급에 달렸다는 프레임으로 협상 지위를 굳혀야 한다.
- 플랫폼 전환이 HBM4 선행 영업 시점을 알려준다. SMCI는 Vera Rubin 시스템의 최초 출시를 준비한다고 말했다. HBM4는 3분기부터 출하가 본격화하고 내년도 HBM 공급가 협상이 진행 중이므로, 시스템 업체의 '최초 출시' 경쟁을 HBM4 조기 인증·물량 배정 마케팅으로 연결해야 한다.
- HPE의 전통 서버 주문 세 자릿수 증가는 AI 외 일반 서버 D램 수요의 복원을 보여준다. AI향에 가려진 범용 서버 세그먼트도 가격·물량 협상에서 강하게 다룰 수 있다.

**(3) 가격·계약 구조 점검**
- Dell은 사실상 매일 재가격한다고 말했다. 고객은 판가를 일 단위로 올리는데 우리가 분기·연간 고정가에 묶이면 인상분이 고객 마진으로 흘러간다. 실제로 SMCI는 FQ4 마진을 가이던스(8.2~8.4%)의 두 배인 15~17%로 예고했다. 시스템 업체의 마진 급팽창은 '전가 여력이 충분하다'는 증거이므로, 인상 협상에서 근거 자료로 쓸 수 있다. 계약은 시장가 연동(인덱스) 또는 짧은 재협상 주기로 설계해야 한다.
- SMCI의 영업현금 66억 달러 유출은 부품 선구매 부담을 보여준다. 물량 보장을 원하는 고객에게는 선급금·장기 커밋을 조건으로 붙이는 구조가 유효하다.

**(4) 수요처 변화 — 마케팅 외연**
- SMCI가 말한 네오클라우드·소버린 AI·에이전틱 AI, Dell의 AI 고객 5,000곳 초과, HPE가 말한 보안 중시 산업의 온프렘 AI 가속은 하이퍼스케일러 밖의 신규 수요층이다. 대형 CSP 중심의 키어카운트 영업을 네오클라우드·소버린·엔터프라이즈 온프렘으로 넓힐 근거가 확보됐다.
- HPE는 네트워킹·컴퓨트·스토리지에 '메모리'를 나란히 놓고 경쟁력을 말했다. 시스템 업체 스스로 메모리를 가치의 축으로 인정한 발언이므로, 공동 마케팅(레퍼런스 아키텍처, 검증 프로그램) 제안의 문이 열려 있다.

**(5) 톤 벤치마크**
- Dell은 주문($24.4B)→매출($16.1B)→백로그($51.3B)의 삼각 수치로 신뢰를 만든다. SMCI는 미스 상황에서도 분기 120억 달러라는 목표 숫자로 서사를 방어한다. HPE는 장기 목표(FY28)를 앞당겨 달성했다는 프레임으로 상향을 정당화한다. SK하이닉스도 '수주 잔고·공급 가시성'을 수치화한 메시지로 투자자·고객 신뢰 프레임에서 밀리지 않아야 한다. 특히 셋 모두 '수요는 문제없고 공급이 병목'이라는 서사를 쓰는 만큼, 그 병목의 해결자가 우리라는 자리매김이 톤의 핵심이다.

## 6. 한 줄 결론

서버 3사가 사상 최대 백로그와 '메모리가 최대 병목'이라는 진술로 메모리 공급자 우위를 스스로 증언한 지금, SK하이닉스는 고정가 다년 계약의 유혹을 피하고 '공급 확실성'을 프리미엄으로 파는 가격·계약·메시징 전략을 밀어붙여야 한다.

### 출처

**Super Micro (1차)**
- [Supermicro IR — Q3 FY2026 실적 보도자료 (2026-05-05)](https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Third-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx)
- [Supermicro — Q3 FY2026 컨콜 준비 발언 PDF](https://s204.q4cdn.com/707617056/files/doc_financials/2026/q3/SMCI-Q326-Prepared-Remarks.pdf)
- [Supermicro IR — Q4 FY2026 예비 실적 업데이트 (2026-07-22)](https://ir.supermicro.com/news/news-details/2026/Supermicro-Provides-Fourth-Quarter-of-Fiscal-Year-2026-Preliminary-Business-Update/default.aspx)
- [BusinessWire — SMCI Q3 FY2026 보도자료(가이던스)](https://secure.businesswire.com/news/home/20260505466308/en/Supermicro-Announces-Third-Quarter-Fiscal-Year-2026-Financial-Results)

**Super Micro (2차)**
- [CNBC — SMCI Q3 실적 기사](https://www.cnbc.com/2026/05/05/super-micro-smci-q3-earnings-report-2026.html)
- [Investing.com — SMCI Q3 컨콜 전사](https://www.investing.com/news/transcripts/earnings-call-transcript-super-micro-computer-q3-2026-beats-eps-revenue-falls-short-93CH-4661414)
- [Motley Fool — SMCI Q3 컨콜 전사](https://www.fool.com/earnings/call-transcripts/2026/05/05/super-micro-smci-q3-2026-earnings-transcript/)
- [Yahoo Finance — SMCI Q3 컨콜 전사](https://finance.yahoo.com/quote/SMCI/earnings/SMCI-Q3-2026-earnings_call-551278.html)
- [Investing.com — SMCI Q3 슬라이드 분석(컨센서스·현금흐름)](https://www.investing.com/news/company-news/super-micro-q3-fy26-slides-eps-beats-amid-revenue-miss-cash-concerns-93CH-4661466)
- [Yahoo Finance — SMCI Q3 실적·주가 반응](https://finance.yahoo.com/markets/stocks/articles/super-micro-computer-q3-2026-131352850.html)
- [HPCwire — SMCI Q3 보도자료 전재](https://www.hpcwire.com/off-the-wire/supermicro-announces-3rd-quarter-fiscal-year-2026-financial-results/)
- [MarketScreener — SMCI Q4 예비 실적](https://www.marketscreener.com/news/supermicro-provides-fourth-quarter-of-fiscal-year-2026-preliminary-business-update-ce7f51d8dc81f027)

**Dell (1차·2차)**
- [Dell 뉴스룸 — FY2027 1분기 실적 (2026-05-28)](https://www.dell.com/en-us/dt/corporate/newsroom/announcements/detailpage.press-releases~usa~2026~05~dell-technologies-delivers-first-quarter-fiscal-2027-financial-results.htm)
- [SEC — Dell 8-K 첨부 실적자료](https://www.sec.gov/Archives/edgar/data/1571996/000157199626000021/exhibit991earnings8kq1fy27.htm)
- [CNBC — Dell Q1 실적·LSEG 컨센서스](https://www.cnbc.com/2026/05/28/dell-q1-earnings-report-2027.html)
- [Motley Fool — Dell Q1 FY2027 컨콜 전사](https://www.fool.com/earnings/call-transcripts/2026/05/28/dell-dell-q1-2027-earnings-call-transcript/)
- [Yahoo Finance — Dell Q1 컨콜 전사](https://finance.yahoo.com/markets/stocks/articles/dell-dell-q1-2027-earnings-221639763.html)
- [Yahoo Finance — Dell Q1 컨콜 하이라이트(백로그 $51.3B)](https://finance.yahoo.com/markets/stocks/articles/dell-technologies-q1-earnings-call-220710464.html)
- [Futurum — Dell Q1 FY2027 분석](https://futurumgroup.com/insights/dell-q1-fy-2027-ai-server-demand-drives-raised-fy-2027-outlook/)
- [TIKR — Dell Q1 FY2027 분석](https://www.tikr.com/blog/dell-technologies-reports-43-8b-revenue-and-beats-street-by-8-billion-in-q1-2027)
- [Blocks & Files — Dell AI서버 분석](https://www.blocksandfiles.com/ai-ml/2026/05/29/dells-extraordinary-ai-server-revenue-acceleration/5248541)

**HPE (1차·2차)**
- [HPE IR — FY2026 2분기 실적 보도자료 PDF (2026-06-01)](https://investors.hpe.com/~/media/Files/H/HP-Enterprise-IR/documents/q2-2026/q2-2026-earnings-press-release.pdf)
- [CNBC — HPE Q2 실적 기사](https://www.cnbc.com/2026/06/01/hpe-stock-earnings-q2.html)
- [Quartz — HPE Q2 실적·컨센서스](https://qz.com/hpe-earnings-record-revenue-ai-server-demand-060126)
- [Yahoo Finance — HPE Q2 컨콜 전사](https://finance.yahoo.com/quote/HPE/earnings/HPE-Q2-2026-earnings_call-592596.html)
- [GuruFocus — HPE Q2 컨콜 하이라이트](https://www.gurufocus.com/news/8895025/hewlett-packard-enterprise-co-hpe-q2-2026-earnings-call-highlights-record-revenue-and-strong-ai-demand-propel-growth)
- [Futurum — HPE Q2 FY2026 분석](https://futurumgroup.com/insights/hpe-q2-fy-2026-ai-orders-remain-strong-as-supply-constraints-persist/)
- [Investing.com — HPE Q1 FY2026 컨콜 전사(메모리 원가 발언)](https://www.investing.com/news/transcripts/earnings-call-transcript-hpe-beats-q1-2026-eps-forecast-by-12-stock-dips-93CH-4550906)

**메모리 산업 맥락(국내)**
- [뉴데일리 — HBM 쏠림에 D램 품귀 (2026-06-26)](https://biz.newdaily.co.kr/site/data/html/2026/06/26/2026062600020.html)
- [KB Think — 메모리 반도체 가격 급등 정리 (2026-02-13)](https://kbthink.com/investment/issues/memory-semiconductor.html)
