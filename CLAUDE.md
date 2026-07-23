# CLAUDE.md

실적·컨콜 분석 파이프라인(Python CLI) + 자급식 정적 뷰어. 상시 서버 없음 —
실행은 GitHub Actions `workflow_dispatch`(`.github/workflows/analyze.yml`),
서빙은 render.com 정적 사이트(`render.yaml`, `docs/` 퍼블리시).

## 아키텍처 불변식

- 역할 분리를 유지한다: `ir_analysis/`(파이프라인) / `config/`(노브·페르소나·문체) /
  `render/`(뷰어 빌더) / `analyses/`(보고서 산출물) / `docs/`(빌드된 뷰어).
- **`docs/index.html`은 생성물이다 — 직접 편집 금지.** `render/template.html`이나
  `render/build.py`를 고치고 `python -m render.build`로 재생성한다.
- 튜닝 노브(persona·target·model·effort·max_tokens 등)는 코드가 아니라
  `config/config.yaml`에 둔다.
- 우리말 문체 규칙은 `config/style_guide.md`에 있고 런타임에 시스템 프롬프트로
  주입된다(`ir_analysis/analyze.py`). 문체 수정은 코드가 아니라 이 파일에서 한다.
- 보고서 프런트매터 스키마(뷰어가 읽음): `title, date, target, persona, scope,
  competitive, model` + 선택 `truncated, quarter_anchor`. 파일명 관례:
  `YYYY-MM-DD_<target-slug>_<persona-id>[-scope][_HHMM].md`.
- 컨콜 발언 발췌에서 1차 전사를 못 얻으면 "2차 전사, 원문 1:1 대조 미완료"를
  명시한다 — `ir_analysis/prompts.py`의 원칙이며 완화하지 않는다.

## 작업 사이클·검증

- `analyses/*.md`를 추가·수정하면 반드시 `python -m render.build`로 뷰어를
  재빌드해 `docs/index.html`을 **함께** 커밋한다.
- 스모크: `python scripts/smoke.py` — API 키 불필요(프롬프트 3모드 생성 +
  보고서 파싱 + 뷰어 빌드). 코드 변경 후 커밋 전에 돌린다.
- 실제 분석 실행은 `ANTHROPIC_API_KEY` 필요: `python -m ir_analysis.analyze --help`.

## 커밋·PR 규약

- 지정된 작업 브랜치에서 개발하고 PR은 스쿼시 머지. **머지된 브랜치에 새 커밋을
  쌓지 않는다** — 후속 작업은 최신 main에서 브랜치를 다시 만든다.
- Actions 실행이 결과(`analyses/` + `docs/`)를 실행한 브랜치에 봇 커밋
  (`ir-analysis-bot`)으로 직접 푸시한다 — 작업 시작 전 `git pull`, 푸시 충돌 시 rebase.

## 배포·환경

- Python 3.12로 통일 고정: Actions(`analyze.yml`)와 Render(`render.yaml`
  `PYTHON_VERSION`)가 같은 계열을 쓴다. 한쪽만 바꾸지 말 것.
- 비밀은 GitHub Secrets(`ANTHROPIC_API_KEY`, 프라이빗 페르소나 레포용 선택
  `PERSONAS_TOKEN`)에만 둔다. 코드·설정·커밋에 키를 넣지 않는다.
- Render 빌드가 실패하면 커밋된 `docs/`를 그대로 서빙한다(`render.yaml`
  buildCommand 폴백) — 그래서 `docs/index.html` 커밋 누락은 조용한 장애가 된다.
