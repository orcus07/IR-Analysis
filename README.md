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
analyses/                     # 생성된 보고서(.md)
```

## 한계 / 주의

- **데이터 신뢰도**: SEC·IR 원문이 막히면 2차 매체 교차확인본을 쓰며, 보고서에
  ⚠️로 '확인 필요' 항목을 표시한다.
- **기간 정합성**: 회사마다 보고 분기가 달라, 경쟁 비교 시 보고서가 시점 차이를 고지한다.
- 분석은 공개 정보 기반의 참고용이며 투자 권유가 아니다.
