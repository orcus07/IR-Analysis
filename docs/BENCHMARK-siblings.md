# 형제 레포 벤치마크 — IR-Analysis vs sv-explorer · PRIMITIVE_WEB · Mybots

작성일: 2026-07-14 · 기준 커밋: `5dea29f` · 판정 기준: **1인 운영 소형 웹앱 규모에 맞는가**
(더 정교하다는 이유만으로는 채택하지 않는다. 근거 경로는 각 레포 루트 기준.)

## 0. 현재 레포(IR-Analysis) 요약

회사·페르소나·분석 범위를 입력하면 Claude가 웹검색으로 최신 실적·컨콜을 수집해
관점별 임플리케이션 보고서를 만드는 Python 파이프라인이다(`ir_analysis/analyze.py`,
`ir_analysis/prompts.py`). 보고서는 `analyses/`에 쌓이고, `render/build.py`가 전체를
자급식 단일 HTML 뷰어(`docs/index.html`)로 빌드해 render.com 정적 사이트로 서빙한다
(`render.yaml`). 실행은 GitHub Actions `workflow_dispatch`(`.github/workflows/analyze.yml`)
로 자동화되어, 뷰어의 실행 패널에서 입력 → 분석 → 커밋 → 재배포가 한 사이클로 돈다.
코드 규모는 Python+HTML 합쳐 약 1,150줄이며 외부 의존성은 `anthropic`, `PyYAML` 둘이다
(`requirements.txt`).

## 세 레포 개요 (한 줄씩)

| 레포 | 역할 | 스택 | 근거 |
|---|---|---|---|
| sv-explorer | 유튜브 링크 → 자막 수집 → 브라우저에서 Claude 증류(요약·병기 번역) 리더 | Node 20+/Express(ESM) + 바닐라 JS | `README.md`, `src/server.js` |
| PRIMITIVE_WEB | 영문 장문 링크/PDF → Claude 한글 증류 리더(잡 큐 + 폴링) | Node 20+/Express(ESM) + 바닐라 JS | `README.md`, `src/server.js` |
| Mybots | ① 칩 아키텍처 인터랙티브 정적 페이지 ② 음성→Whisper→Claude 회의록 서비스 | 정적 HTML + Node/Express | `project_summary.md`, `meeting-minutes/src/server.js` |

참고: PRIMITIVE_WEB과 Mybots에도 `docs/BENCHMARK-siblings.md`가 있다 — 이 벤치마크는
레포 간 순회 관행이며, 이 문서가 IR-Analysis 차례다.

---

## ① 프로젝트 구조·모듈화

- **최우수: PRIMITIVE_WEB.** 엔트리(`src/server.js`, 라우팅·잡 관리) / 도메인 라이브러리
  (`src/lib/fetchArticle.js` 수집 3중 전략, `src/lib/distill.js` LLM 로직) / UI(`public/`)의
  3계층이 가장 뚜렷하고, 서버 메모리 잡 맵 + 폴링(fire-and-forget) 패턴으로 장시간 LLM
  작업을 HTTP 연결에서 분리했다(`src/server.js:92-144`).
- **현재 레포:** 파이프라인(`ir_analysis/analyze.py`) / 프롬프트 빌더(`ir_analysis/prompts.py`)
  / 페르소나 동기화(`ir_analysis/sync_personas.py`) / 뷰어 빌더(`render/build.py` +
  `render/template.html`) / 설정(`config/`)으로 분리. 역할 대비 파일 수·계층이 적절하다.
- **차이의 원인:** 상시 서버(Node 웹앱) vs 배치 CLI+정적 사이트(Python)라는 실행 모델
  차이. 잡 큐·폴링은 서버가 있어야 성립하고, 현재 레포는 그 역할을 GitHub Actions가
  대신한다(`.github/workflows/analyze.yml`).
- **판정: 부적합(이식 불요).** 현재 구조가 규모에 맞고, 잡 큐 패턴을 들여오려면 상시
  서버가 필요해 "정적 사이트 + Actions" 아키텍처의 단순성(서버 비용 0, 운영 부담 0)을
  깨뜨린다.

## ② 에러 핸들링·로깅

- **최우수: Mybots.** 외부 API 호출에 **지수 백오프 재시도**를 일관 적용 — Claude 3회
  (5s/10s), Whisper 3회(4s/8s)(`meeting-minutes/src/server.js`의 `processJob`,
  `meeting-minutes/src/lib/transcribe.js`의 `whisper`), 임시 파일은 `finally`에서 정리.
  PRIMITIVE_WEB의 `noRetry` 플래그(재시도 무의미한 오류 구분, `src/server.js:117-125`)도
  좋은 세부다.
- **현재 레포:** `pause_turn` 연속 처리(최대 8회)와 400 오류의 원인 힌트(ZDR 안내),
  잘림(`max_tokens`) 감지·표기, 동기화 실패의 레포 단위 격리(`ir_analysis/analyze.py`,
  `ir_analysis/sync_personas.py:main`)는 갖췄다. 그러나 **일시 장애(529 overloaded,
  5xx, 네트워크 단절)에 대한 재시도가 없다** — 발생 시 Actions 실행이 통째로 실패하고
  검색에 쓴 토큰 비용도 버려진다. 로깅은 세 레포 모두와 같은 stderr/console 수준.
- **차이의 원인:** 형제 레포들은 실사용 중 Whisper/Claude의 일시 오류를 겪으며 재시도를
  붙인 흔적이 보인다(우회 구현 주석 등). 현재 레포는 아직 실전 실행 횟수가 적다.
- **판정: 채택(재시도만).** Mybots식 지수 백오프를 스트림 호출부에 적용할 가치가 크다
  — 실행 1회가 길고 비싸기 때문. 구조화 로거 도입은 **부적합**(1인 규모에 과함,
  세 레포 모두 console 수준으로 충분히 운영 중).

## ③ 테스트·검증 (smoke test 유무)

- **최우수: Mybots.** 자동화 테스트는 없지만 검증 수단이 가장 실용적이다 —
  `/api/health`(키 설정 여부)에 더해 `/api/test-claude`가 키 형식 → raw fetch → SDK
  순서로 **단계별 연결 진단**을 제공한다(`meeting-minutes/src/server.js:31-119`).
  sv-explorer·PRIMITIVE_WEB도 `/api/health`를 Render `healthCheckPath`로 연결해 배포
  검증에 쓴다(sv-explorer `render.yaml:10`).
- **현재 레포:** 커밋된 테스트·스모크 자산이 **없음**. 개발 세션 중 headless Chromium
  스모크와 프롬프트 빌더 단위 검증을 반복 수행했지만 일회성 스크립트로 소비되어 레포에
  남아 있지 않다. 정적 사이트라 `healthCheckPath` 같은 런타임 헬스체크는 성립하지 않는다.
- **차이의 원인:** 형제 레포들은 상시 서버라 "떠 있는가"를 확인할 엔드포인트가 자연스럽게
  생겼고, 현재 레포는 검증이 세션(사람) 쪽에 붙어 있었다.
- **판정: 채택(경량 스모크 1개).** 뷰어 빌드·렌더와 프롬프트 3모드 생성을 검사하는
  스크립트 하나를 커밋하고 Actions의 뷰어 재빌드 뒤 실행하면, 세션에서 하던 검증이
  레포 자산이 된다. 테스트 프레임워크(pytest 스위트) 도입은 **부적합**(형제 레포 셋 다
  없이 운영되는 규모이고, 코드 1,150줄에 스위트는 과함).

## ④ CI·배포 (Render 설정, 환경변수 관리)

- **최우수: 현재 레포(IR-Analysis).** 네 레포 중 유일하게 GitHub Actions 워크플로를
  보유하고, `concurrency` 큐잉·푸시 충돌 시 리베이스+재빌드+재시도·프라이빗 소스용
  토큰 폴백까지 갖췄다(`.github/workflows/analyze.yml`). Render 설정도 빌드 실패 시
  커밋본 폴백(`render.yaml` buildCommand)과 `PYTHON_VERSION` 고정으로 방어적이다.
  환경변수 관리는 네 레포가 같은 모범을 공유한다 — 비밀은 코드 밖(현재: GitHub Secrets
  `ANTHROPIC_API_KEY`·`PERSONAS_TOKEN` / 형제: Render `sync:false` + `.env.example`,
  PRIMITIVE_WEB `render.yaml:11-16`).
- **형제에서 얻을 교훈(역채택 아님):** 문서-코드 불일치가 두 곳에서 발견됐다 —
  sv-explorer `DEPLOY.md:38-40`은 폐기된 서버측 키 입력을 안내하고, PRIMITIVE_WEB은
  README가 `claude-opus-4-8`이라 쓰지만 코드는 `claude-sonnet-5`를 쓴다
  (`README.md:26` vs `src/lib/distill.js:11-12`). 같은 부패가 이 레포의 README 모델
  표·설정 주석에도 생길 수 있다.
- **판정: 현재 방식 유지 + 보류 1건.** 형제의 `.env.example` 관례는 로컬 실행 안내용으로
  가볍게 채택해도 좋으나(파일 1개), 현재 레포는 로컬 실행 시 환경변수 하나뿐이라
  README 한 줄로 대체 중 — **보류**.

## ⑤ 의존성 관리

- **최우수: sv-explorer(PRIMITIVE_WEB 동급).** 런타임 의존성 4개로 최소화하고
  (레이트리밋도 자체 구현으로 의존성 억제, `src/server.js:59-78`), **lockfile을 커밋**해
  재현성을 확보하며(`package-lock.json`), `engines.node ">=20"`으로 런타임 하한을
  명시한다(`package.json:5-13`). 반면 Mybots는 lockfile이 없어 대비된다.
- **현재 레포:** 의존성 2개로 가장 적으나 `anthropic>=0.92.0` 하한만 있고 상한·고정이
  없다(`requirements.txt`). anthropic SDK는 마이너 버전에서 API가 자주 바뀌는
  라이브러리라(이 레포도 `fallbacks` 미지원 SDK를 `try/except TypeError`로 방어 중,
  `ir_analysis/analyze.py`), Actions가 매 실행 최신판을 설치하는 현 구조는 **어느 날
  조용히 깨질 수 있는** 지점이다.
- **차이의 원인:** npm은 lockfile이 기본 생성물이라 공짜로 얻지만 pip는 의식적으로
  만들어야 한다.
- **판정: 채택.** `requirements.txt`를 정확 버전(`==`)으로 고정하는 것으로 충분하다
  (의존성 2개라 lock 도구 도입은 과함). 갱신은 의도적·수동으로.

## ⑥ 에이전트 설정 자산 (CLAUDE.md, .claude/rules·skills·hooks, .mcp.json)

- **최우수: 없음 — 네 레포 모두 부재.** sv-explorer·PRIMITIVE_WEB·Mybots 모두
  `CLAUDE.md`, `.claude/`(rules/skills/hooks), `.mcp.json`이 존재하지 않는다(각 레포
  루트 확인). 현재 레포도 `.claude/`가 빈 디렉터리로만 있다. Mybots의
  `project_summary.md`(개발 히스토리·특이사항 정리)가 그나마 에이전트 온보딩 문서에
  가장 가까운 관행이다.
- **현재 레포가 가장 아쉬운 축이다.** 네 레포 중 세션 간 이어받아야 할 관례가 가장
  많기 때문 — 프런트매터 스키마, 우리말 스타일 가이드 주입 구조(`config/style_guide.md`),
  "analyses 수정 → `python -m render.build` 재빌드" 사이클, 스쿼시 머지 후 브랜치 동기화
  절차, 보고서 발췌의 "2차 전사" 표기 원칙 같은 것들이 전부 대화 기록에만 있다.
- **판정: 채택(CLAUDE.md 1개), 나머지는 부적합.** 위 관례를 담은 CLAUDE.md 하나면
  다음 세션의 재파악 비용이 크게 준다. `.claude/rules·skills·hooks`와 `.mcp.json`
  풀세트는 1인 소형 레포에 과함 — 형제 레포 셋이 없이도 잘 돌아간다는 것이 그 방증이다.

---

## 채택 후보 Top 5 (구현 비용 대비 효과 순)

| 순위 | 항목 | 출처(벤치마크 근거) | 비용 | 효과 |
|---|---|---|---|---|
| 1 | **의존성 정확 버전 고정** (`requirements.txt` `==`) | sv-explorer의 lockfile 커밋 관행 | 몇 분 | Actions가 매번 최신 SDK를 설치하다 조용히 깨지는 미래 장애 차단 |
| 2 | **API 호출 지수 백오프 재시도** (스트림 개시·pause_turn 재개 시 529/5xx 3회 재시도) | Mybots `processJob`·`whisper`의 재시도 패턴 | 코드 십수 줄 | 길고 비싼 분석 실행 1회가 일시 장애로 통째 실패하는 것 방지 — 토큰 비용 보호 |
| 3 | **CLAUDE.md 작성** (프런트매터 스키마·재빌드 사이클·머지 절차·표기 원칙) | 네 레포 공통 공백 + Mybots `project_summary.md` 관행 | 30분 | 세션 재시작 시 재파악 비용 제거, 관례 이탈로 인한 회귀 방지 |
| 4 | **경량 스모크 스크립트 커밋** (뷰어 빌드·렌더 + 프롬프트 3모드 검사, Actions에 검증 단계 추가) | sv-explorer·Mybots의 healthCheck/진단 엔드포인트의 정적 사이트 등가물 | 1~2시간 | 세션에서 매번 손으로 하던 검증의 자산화, 깨진 뷰어가 배포되는 사고 차단 |
| 5 | **문서-코드 정합 점검** (README 모델 표·config 주석을 릴리스 때 대조) | sv-explorer `DEPLOY.md` 부패, PRIMITIVE_WEB README-코드 모델명 불일치 사례 | 습관(0원) | 형제 레포에서 실제로 발생한 문서 부채의 예방 — 잘못된 안내로 시간 낭비 방지 |

**부적합으로 분류한 것들(요약):** 잡 큐+폴링 서버(①, 아키텍처 불일치), 구조화 로거(②),
pytest 스위트(③), `.claude/` 풀세트·`.mcp.json`(⑥) — 모두 "1인 운영 소형" 기준에서
비용이 효과를 넘는다.

---
*분석 방법: 세 레포를 `/tmp`에 `--depth 1` 클론 후 레포당 서브에이전트가
tree → README → 설정 → 대표 소스 순으로 탐색. 현재 레포는 메인 세션이 직접 확인.*
