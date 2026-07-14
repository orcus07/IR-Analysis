# 4개 레포 공통 표준 — 교차 검증 결과

작성일: 2026-07-14 · 입력: 4개 레포의 `docs/BENCHMARK-siblings.md`
(IR-Analysis `b07c3f7` 로컬 / PRIMITIVE_WEB·Mybots 기본 브랜치 /
sv-explorer `claude/youtube-transcript-folder-mfxvu7` 브랜치 — main에는 벤치마크 문서 없음)

판정 기준은 4개 문서와 동일: **1인 운영 소형 웹앱 규모에 맞는가**.
더 정교하다는 이유만으로는 표준이 되지 않는다. 상충 판정은 근거 파일을 직접 재확인해 결론냈고,
아래 인용 경로는 이 검증 시점의 각 레포 체크아웃에서 실재를 확인한 것이다.

---

## 1. 문서 간 판정이 갈렸던 지점과 최종 결론

### ② 에러 핸들링·로깅 — 4개 문서가 4개의 다른 답 (실질 상충)

| 문서 | "최우수" 판정 |
|---|---|
| sv-explorer 문서 | 동률: sv-explorer ≈ IR-Analysis |
| IR-Analysis 문서 | Mybots (지수 백오프 재시도 일관 적용) |
| PRIMITIVE_WEB 문서 | IR-Analysis (실패 모드 처리 성숙) |
| Mybots 문서 | PRIMITIVE_WEB (`isTransient`+`noRetry` 규율) |

**재검증 결과 — 각 문서가 서로 다른 하위 측면을 보고 있었고, 두 판정은 틀렸다:**

- **재시도 규율** 기준 최우수는 **PRIMITIVE_WEB ≈ sv-explorer 동률**이다.
  PRIMITIVE_WEB은 서버측에서 일시 오류만 재시도(`isTransient()`)하고 결정적 실패는
  `err.noRetry`로 즉시 중단한다(`src/lib/distill.js:236-267`). sv-explorer는 같은
  분류(`isTransient`/`isModelError`)에 모델 과부하 폴백(Sonnet→Haiku)까지 클라이언트측에
  갖췄다(main의 `public/distill.js:286-298, 347-402, 521-549` — 벤치마크 세션 브랜치가
  아니라 main에 이미 병합돼 있음을 확인).
- **IR-Analysis 문서의 "최우수 Mybots"는 오판.** Mybots의 재시도는 존재하지만
  **무조건적**이다 — 오류 종류를 보지 않고 3회를 다 돈다
  (`meeting-minutes/src/server.js:141-148`, `src/lib/transcribe.js:54-71`에 분류 로직 없음).
  Mybots 문서 스스로도 이를 약점으로 자인한다. '재시도가 있다'와 '재시도에 규율이 있다'를
  구분하지 못한 판정이다.
- **PRIMITIVE_WEB 문서의 "최우수 IR-Analysis"는 절반만 맞다.** IR-Analysis는
  **불완전 산출물 감지**(stop_reason 분기, max_tokens 절단 3중 경고,
  `ir_analysis/analyze.py:240-268`)에서는 최우수가 맞지만, 일시 장애(529/5xx)
  재시도가 **아예 없어**(`analyze.py` 전체에 백오프 부재, pause_turn 루프만 존재)
  종합 최우수는 아니다.

**최종 결론:** 이 축의 표준은 두 패턴의 합집합이다 — 재시도 규율은 PRIMITIVE_WEB에서,
불완전 산출물 감지는 IR-Analysis에서 가져온다(§2-② 참조).

### ① 구조·모듈화 — 표면상 상충, 실질 일치

sv-explorer·PRIMITIVE_WEB·Mybots 문서는 셋 다 **IR-Analysis**(코드/설정/렌더/산출물
디렉터리 분리)를 최우수로 지목했고, IR-Analysis 문서만 PRIMITIVE_WEB을 지목했다.
그러나 IR 문서의 "최우수"는 **자기 자신을 제외한 형제 중** 최우수이며, 본문에서 자기
구조를 "역할 대비 적절"로 평가한다. 실질 상충 아님 — **최종: IR-Analysis** (단, Node
웹앱 유형 안에서는 PRIMITIVE_WEB의 3계층이 참조형).

### ③ 테스트·검증 — 1개 문서만 이탈

세 문서는 "최우수 없음(공통 결함)", IR-Analysis 문서만 Mybots의 `/api/test-claude`
단계별 진단 엔드포인트를 최우수로 지목했다. 확인 결과 해당 엔드포인트는 실재하나
(`meeting-minutes/src/server.js:39`), 이는 **런타임 진단 도구지 테스트·검증 자산이
아니다**. **최종: "없음(공통 결함)"이 맞다.** 다만 진단 엔드포인트 관행 자체는 참고 가치가
있어 §2-③에 부기한다. 처방(경량 스모크 채택, 유닛 스위트 부적합)은 4개 문서 모두 일치.

### ⑤ 버전 핀 정책 — 상충처럼 보이나 둘 다 맞음

IR-Analysis 문서는 "`requirements.txt` `==` 정확 핀 **채택**", PRIMITIVE_WEB 문서는
"정확 핀 전환 **부적합**"이라 썼다. 생태계가 다르다 — npm은 `package-lock.json`이
정확 버전을 이미 고정하므로 캐럿 유지가 맞고, pip는 락파일이 없으므로 `==`가 그 등가물이다.
**최종: 표준을 "재현 가능한 설치"로 상위 정의**하고 수단은 생태계별로 둔다(§2-⑤).

### 일치했던 축 (상충 없음)

④ CI·배포: 4개 문서 모두 IR-Analysis(유일 CI — 단 배치 러너이며 검증 게이트 아님).
⑤ 의존성: 4개 문서 모두 sv-explorer(락파일+최소 의존성+engines).
⑥ 에이전트 자산: 4개 문서 모두 "전무 → 얇은 CLAUDE.md만 채택, 풀셋 부적합".

### 4개 문서가 모두 놓친 축

**사용자 데이터 내구성(브라우저 보관함의 백업·내보내기)** — 세 웹앱 모두 산출물을
localStorage/IndexedDB에만 두는데, sv-explorer(`public/app.js:549` `exportArchive`)와
PRIMITIVE_WEB(`public/app.js:555` `exportBackup`)은 내보내기/가져오기를 구현했고
Mybots 회의록 앱에는 없다. 어느 문서도 이를 비교 축으로 다루지 않았다.

---

## 2. 축별 공통 표준

각 표준은 "채택할 방식 + 출처 레포 + 근거 경로". 근거 경로는 출처 레포 루트 기준.

### ① 구조·모듈화

| 표준 | 출처 | 근거 |
|---|---|---|
| 실행 유형에 맞는 계층 분리 — 배치/CLI는 코드·설정·렌더·산출물 디렉터리 분리, 웹앱은 엔트리·`src/lib/`·`public/` 3계층 | IR-Analysis (디렉터리 분리) / PRIMITIVE_WEB (3계층) | `ir_analysis/` + `config/` + `render/` + `analyses/` 분리 / `src/server.js` + `src/lib/{fetchArticle,distill}.js` + `public/` |
| 반복 튜닝되는 프롬프트·문체 규칙은 코드 밖 데이터로 (단, 노브가 실제로 여러 개일 때만 — 상수 몇 개면 하드코딩 유지) | IR-Analysis | `config/config.yaml`, `config/personas/*.yaml`, `config/style_guide.md` |

**비표준(부적합/보류 컨센서스):** 잡 큐+폴링 서버의 타 유형 이식(아키텍처 불일치),
노브 수가 적은 웹앱의 config 외부화(파일만 늘림).

### ② 에러 핸들링·로깅

| 표준 | 출처 | 근거 |
|---|---|---|
| 외부 API 호출은 **일시 오류(408/429/5xx/네트워크)만** 지수 백오프로 2~3회 재시도, 결정적 실패는 즉시 중단(`noRetry`류 플래그) | PRIMITIVE_WEB (sv-explorer 동급) | `src/lib/distill.js:236-267` (`isTransient`+`noRetry`) / sv-explorer `public/distill.js:286-298,347-402` |
| LLM 응답의 `stop_reason` 분기 검사 — `max_tokens` 절단 시 산출물에 눈에 띄는 경고를 남겨 "조용한 불완전 저장" 방지 | IR-Analysis | `ir_analysis/analyze.py:240-268` (본문·프런트매터·stderr 3중 경고) |
| 과부하(529)·모델 ID 오류 시 하위 모델 폴백 (LLM이 제품 핵심인 앱에 한함) | sv-explorer | `public/distill.js:521-549` (Sonnet→Haiku) |

**비표준:** 구조적 로깅 라이브러리(winston/pino 등) — 4개 문서 만장일치 부적합.
plain console + 사용자향 단계 메시지로 충분.

### ③ 테스트·검증

| 표준 | 출처 | 근거 |
|---|---|---|
| **초경량 스모크 1개**를 레포 자산으로 커밋하고 실행 명령(`npm test` 등)에 등록 — 웹앱: 구문 검사 + 부팅 + `/api/health` 200 / 정적 파이프라인: 뷰어 빌드 + 프롬프트 생성 검사 | 공통 공백(넷-뉴) — 4개 문서 모두 채택 판정 | 기존 수동 검증 절차의 성문화 (예: PRIMITIVE_WEB 문서 ③, sv-explorer 문서 ③) |
| 상시 서버는 `/api/health`를 Render `healthCheckPath`로 연결 | sv-explorer·PRIMITIVE_WEB·Mybots 공통 | sv-explorer `render.yaml:10`, PRIMITIVE_WEB `src/server.js:88-90` |
| (참고) 외부 API 키·연결의 단계별 진단 엔드포인트 | Mybots | `meeting-minutes/src/server.js:39-119` (`/api/test-claude`) |

**비표준:** 유닛 테스트 프레임워크 풀 스위트 — 4개 문서 만장일치 부적합
(외부 API 의존이 커서 모킹 비용 > 효용).

### ④ CI·배포

| 표준 | 출처 | 근거 |
|---|---|---|
| 스모크가 생긴 뒤 push/PR에서 그것만 돌리는 **초경량 CI 1개** (배치 러너의 concurrency·rebase 재시도 같은 고급 패턴은 이식 금지) | IR-Analysis (유일 CI 보유 — 단 형태는 각자 게이트형으로) | `.github/workflows/analyze.yml` |
| 비밀은 코드 밖: Render `sync: false` + GitHub Secrets, 로컬 안내는 `.env.example` | 4개 레포 공통 관례 | PRIMITIVE_WEB `render.yaml:11-14`·`.env.example`, IR-Analysis Secrets |
| **코드가 읽는 모든 환경변수를 배포 설정에 선언** — Blueprint 재배포 시 조용히 빠지는 결함 방지 | PRIMITIVE_WEB 문서의 자체 발견(반면교사) | `src/server.js:68`은 `ACCESS_KEY`를 읽으나 `render.yaml` `envVars`에 없음 |
| 런타임 버전을 배포·CI 간 일치 고정 | Mybots·PRIMITIVE_WEB 문서의 지적(반면교사) | IR-Analysis `render.yaml:19`(3.11.9) vs `analyze.yml:69`(3.12) 불일치 |

### ⑤ 의존성 관리

| 표준 | 출처 | 근거 |
|---|---|---|
| **재현 가능한 설치**: npm → `package-lock.json` 커밋 + 캐럿 유지 / pip → `==` 정확 핀 (§1 결론) | sv-explorer | `package-lock.json` + `package.json` 캐럿 + `engines >=20` |
| 직접 의존성 최소화 + **미사용(사문화) 의존성 즉시 제거** | sv-explorer 문서의 자체 발견 | sv-explorer `@anthropic-ai/sdk`: `package.json`에 선언, `src/`·`public/` import 0건 (본 검증에서 재확인) |

### ⑥ 에이전트 설정 자산

| 표준 | 출처 | 근거 |
|---|---|---|
| **얇은 `CLAUDE.md` 1개**: 아키텍처 불변식, 검증 명령, 커밋·PR 규약, 배포 매핑(브랜치↔서비스), 샌드박스 제약 | 4개 레포 공통 공백 — 4개 문서 만장일치 채택 | Mybots 문서 ⑥이 근거로 든 브랜치 force-push 충돌 사고(배포 매핑 부재가 원인) |

**비표준:** `.claude/rules·skills·hooks`, `.mcp.json` 풀셋 — 4개 문서 만장일치 부적합/보류.

---

## 3. 레포별 적용 목록

이미 표준을 충족하는 항목은 제외했다. 충족 여부는 본 검증 시점의 체크아웃에서 확인.
작업량: S(1시간 미만) / M(반나절) / L(그 이상).

### sv-explorer

이미 충족: lockfile+캐럿, `isTransient` 재시도+모델 폴백(main 확인), env 문서화(`.env.example`), 보관함 내보내기.

| 우선순위 | 항목 | 표준 축 | 작업량 |
|---|---|---|---|
| 1 | `@anthropic-ai/sdk` 사문화 의존성 제거 (`package.json` 1줄 + `npm install` 락파일 갱신) | ⑤ | S |
| 2 | `CLAUDE.md` (서버는 자막만·브라우저 직접 호출·키는 서버에 없음·모델 ID를 산출물에 넣지 않기) | ⑥ | S |
| 3 | 스모크(부팅+`/api/health` 200+lib import) + `npm test` 등록 | ③ | S |
| 4 | push/PR 스모크 CI 1개 (3번 선행) | ④ | S |
| 5 | `docs/BENCHMARK-siblings.md`가 세션 브랜치에만 있음 — main으로 병합 | (문서 정합) | S |

### PRIMITIVE_WEB

이미 충족: lockfile, `isTransient`+`noRetry`, `stop_reason` 절단 검사(`distill.js:243,386` — 자기 벤치마크의 5번 후보를 이미 이행), `ACCESS_KEY` 게이트, `.env.example`, 보관함 내보내기.

| 우선순위 | 항목 | 표준 축 | 작업량 |
|---|---|---|---|
| 1 | `render.yaml` `envVars`에 `ACCESS_KEY`·`READER_PROXY` 선언(`sync: false`) — 미수정 확인 | ④ | S |
| 2 | `CLAUDE.md` (잡 모델·캐시 버스팅 `?v=` 규칙·Render 무료 티어 제약·샌드박스 제약) | ⑥ | S |
| 3 | 스모크(`node --check`+부팅+`/api/health` 200) + `npm test` 등록 | ③ | S |
| 4 | push 스모크 CI 1개 (3번 선행) | ④ | S |

### IR-Analysis (현재 레포)

이미 충족: CI 보유(축 ④ 최우수), 절단 3중 경고·`stop_reason` 분기, 코드/설정/렌더/산출물 분리(축 ① 최우수), 비밀은 GitHub Secrets.

| 우선순위 | 항목 | 표준 축 | 작업량 |
|---|---|---|---|
| 1 | `requirements.txt` `==` 정확 핀 (`anthropic`, `PyYAML`) | ⑤ | S |
| 2 | 스트림 호출부에 일시 장애(529/5xx) 지수 백오프 재시도 — PRIMITIVE_WEB `distill.js:236-267` 패턴 이식 (긴 실행 1회의 토큰 비용 보호) | ② | M |
| 3 | `CLAUDE.md` (프런트매터 스키마·`python -m render.build` 재빌드 사이클·스쿼시 머지 후 브랜치 동기화·"2차 전사" 표기 원칙) | ⑥ | S |
| 4 | 경량 스모크(뷰어 빌드+프롬프트 3모드 생성) 커밋 + Actions에 검증 스텝 추가 | ③④ | M |
| 5 | Python 버전 정합: `render.yaml`(3.11.9) vs `analyze.yml`(3.12) 한쪽으로 통일 | ④ | S |

### Mybots

이미 충족: `meeting-minutes/` 자체의 3계층 분리, `rootDir` 격리 배포, `/api/health`+`/api/test-claude`.

| 우선순위 | 항목 | 표준 축 | 작업량 |
|---|---|---|---|
| 1 | `meeting-minutes/package-lock.json` 커밋 + 미사용 의존성 `openai`·`youtube-transcript` 제거 (import 0건 재확인) | ⑤ | S |
| 2 | `CLAUDE.md` (레포↔브랜치↔배포 매핑 + "PRIMITIVE_WEB에 force push 금지" 경계 규칙 — 과거 사고 재발 방지) | ⑥ | S |
| 3 | 재시도에 규율 부여: `isTransient`+`noRetry` 이식 (현재 무조건 3회, `src/server.js:141-148`) | ② | S |
| 4 | `ACCESS_KEY` 접근 게이트 이식 (PRIMITIVE_WEB `src/server.js:65-74`) — Opus 사용이라 남용 피해가 가장 큼 | ② | S |
| 5 | 스모크(구문+부팅+`/api/health` 200) + `npm test` 등록 | ③ | S |
| 6 | 보관함 내보내기/가져오기 (sv-explorer `public/app.js:549` 패턴) — §1 "놓친 축" 해당, 유일 미구현 레포 | (신규 축) | M |
