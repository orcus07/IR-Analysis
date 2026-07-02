# IR-Analysis

지시하면 바로 **특정 회사의 최신 실적 발표·어닝콜 발언을 분석**하고, 지정한
**관점(페르소나)** 에서 임플리케이션을 뽑는 파이프라인. 관점·분석 대상은 매번
바꿔서 호출할 수 있고, 옵션으로 **경쟁사도 동일 프레임(정량·정성)으로 비교**한다.

## 작동 방식

3개의 변수만 바꿔 재사용한다:

| 변수 | 설명 | 기본값 (few-shot 케이스) |
|------|------|--------------------------|
| **페르소나(관점)** | 누구의 시각에서 임플리케이션을 뽑을지 | SK하이닉스 마케터 |
| **분석 대상** | 실적·컨콜을 분석할 회사 | Micron Technology |
| **경쟁사 분석** | 켜면 경쟁사를 같은 프레임으로 비교 | ON (SK하이닉스·삼성) |

파이프라인은 Anthropic Claude(`claude-opus-4-8`)에 **웹검색 도구**를 붙여, 대상
회사의 최신 분기 실적·컨콜을 직접 수집·분석하고 지정 관점의 임플리케이션을
도출한 마크다운 보고서를 `analyses/` 에 저장한다.

## 설치

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
```

## 사용

```bash
# 기본 케이스 (config/config.yaml): SK하이닉스 마케터 관점 + 마이크론 + 경쟁사 비교
python -m ir_analysis.analyze

# 관점/대상/경쟁사를 바꿔서
python -m ir_analysis.analyze --persona sk_hynix_marketer \
    --target "NVIDIA" --competitors "AMD" "Intel"

# 경쟁사 비교 끄기
python -m ir_analysis.analyze --target "Micron Technology" --no-competitive
```

CLI 인자는 `config/config.yaml` 의 기본값을 덮어쓴다.

### 모델 선택 (품질 1순위 / 비용 2순위)

| 모델 | 용도 | 비고 |
|------|------|------|
| `claude-fable-5` (기본) | 품질 최상 | 가장 유능·장기 에이전틱 강함. $10/$50, 30일 데이터 보존 필요(ZDR 불가) |
| `claude-opus-4-8` | 균형 | Fable에 근접, 비용 절반($5/$25) |
| `claude-sonnet-5` | 대량 배치 | 비용형 — 품질 1순위 용도엔 비권장 |

Fable/Mythos 모델은 안전 분류기 거부 시 **Opus 4.8로 자동 폴백**한다(파이프라인 내장). 품질 민감 작업은 `--effort xhigh` 권장.

## 렌더 뷰어 — 보고서 누적 열람

분석할 때마다 보고서가 `analyses/` 에 쌓이고, 한 번의 빌드로 **모바일에서
열리는 단일 HTML 뷰어**가 갱신된다. 뷰어 상단에서 **대상 회사 → 보고서**를
고르면 해당 분석이 바로 렌더링된다.

```bash
python -m render.build     # analyses/*.md → docs/index.html (자급식, CDN 불필요)
```

- 보고서 맨 앞의 YAML 프런트매터(title/date/target/persona)를 메타로 쓴다.
  파이프라인이 자동으로 붙이므로 손댈 필요 없다.
- `docs/` 를 GitHub Pages 소스로 지정하면 폰에서 URL 하나로 전체 보고서를
  열람한다. Pages 없이도 `docs/index.html` 파일 하나만 열면 된다.

### 렌더 페이지에서 바로 실행

뷰어 상단 **"▶ 새 분석 실행"** 패널에서 회사·관점을 입력하고 버튼을 누르면,
브라우저가 GitHub Actions API(`workflow_dispatch`)를 직접 호출해 분석을
돌리고 진행 상태를 폴링해 보여 준다. 서버가 따로 없다.

```
[렌더 페이지 입력] ─▶ GitHub Actions ─▶ analyze.py ─▶ analyses/*.md
                                                        │
        열람(모바일) ◀── docs/index.html (Pages) ◀── render/build.py
```

준비물 2가지 (한 번만):

1. **저장소 Secrets → `ANTHROPIC_API_KEY`** — Actions가 분석을 돌릴 때 쓴다.
2. **GitHub fine-grained 토큰** — 이 저장소만, 권한은 *Actions: Read and write*.
   패널에 한 번 붙여 넣으면 그 브라우저의 localStorage에만 저장된다.
   (공용 기기에서는 쓰지 말 것)

`docs/` 를 GitHub Pages 소스로 지정하면 폰 브라우저에서 입력 → 실행 → 열람이
전부 한 페이지에서 된다. 완료 후 Pages 반영까지 1~2분 걸린다.
Actions 탭에서 직접 Run workflow 해도 같은 결과다.

### 웹 배포 (render.com)

루트의 `render.yaml` 이 Blueprint 설정이다. 무료 정적 사이트로 올린다:

1. [dashboard.render.com](https://dashboard.render.com) → **New → Blueprint** →
   GitHub 계정 연결 → `IR-Analysis` 저장소 선택 (브랜치는 `main` 권장)
2. Render가 `render.yaml` 을 읽어 `ir-analysis` 정적 사이트를 만든다.
   빌드마다 `analyses/` 를 다시 스캔하므로 뷰어는 항상 최신이다.
3. 발급된 `https://ir-analysis.onrender.com` 류의 URL을 폰에 북마크.

이후에는 푸시(수동 커밋, Actions 봇의 보고서 커밋 포함)마다 자동으로 다시
배포된다. 즉 렌더 페이지에서 분석을 실행하면 몇 분 뒤 같은 페이지에 새
보고서가 올라온다.

## 새 관점 추가

페르소나는 `config/personas/<id>.yaml` 파일이다. 템플릿을 복사해 만든다:

```bash
cp config/personas/_template.yaml config/personas/samsung_strategy.yaml
# 편집 후
python -m ir_analysis.analyze --persona samsung_strategy --target "Micron Technology"
```

## 구조

```
config/
  config.yaml                 # 기본 실행 설정(페르소나/대상/경쟁사/모델 등)
  style_guide.md              # 우리말 작성 규칙(번역체 줄이기 등) — 시스템 프롬프트에 자동 주입
  personas/
    sk_hynix_marketer.yaml    # 기본 페르소나
    _template.yaml            # 새 관점용 템플릿
ir_analysis/
  prompts.py                  # 분석 프롬프트 빌더
  analyze.py                  # CLI 파이프라인
render/
  build.py                    # analyses/*.md → docs/index.html 뷰어 빌드
  template.html               # 뷰어 셸(선택 UI + 마크다운 렌더러)
analyses/                     # 생성된 보고서(.md, 프런트매터 포함)
docs/
  index.html                  # 누적 뷰어(자급식) — GitHub Pages 소스로 지정 가능
.github/workflows/
  analyze.yml                 # Actions 원클릭: 입력 → 분석 → 뷰어 갱신 → 커밋
```

## 한계 / 주의

- **데이터 신뢰도**: SEC·IR 원문이 막히면 2차 매체 교차확인본을 쓰며, 보고서에
  ⚠️로 '확인 필요' 항목을 표시한다.
- **기간 정합성**: 회사마다 보고 분기가 달라, 경쟁 비교 시 보고서가 시점 차이를 고지한다.
- 분석은 공개 정보 기반의 참고용이며 투자 권유가 아니다.
