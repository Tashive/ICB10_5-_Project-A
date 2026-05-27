# 국민연금 가입 사업장 데이터 정적 HTML 대시보드 제작 계획서 (dashboard_prompt.md)

이 문서는 `nps-company/report/eda_report.md`의 분석 결과를 바탕으로, 별도의 서버 없이 웹 브라우저에서 즉시 확인 가능한 **정적 HTML 기반 대시보드**를 제작하기 위한 프롬프트 가이드라인입니다.

## 1. 프로젝트 개요
- **목표**: 분석 보고서의 핵심 인사이트를 단일 HTML 파일 내에 현대적인 UI로 재구성하여 시각적 가독성 극대화
- **권장 기술 스택**: HTML5, CSS3 (Tailwind CSS CDN), JavaScript (Chart.js 또는 ApexCharts)
- **자산 활용**: `nps-company/images/` 폴더 내의 정적 이미지 및 보고서 내 통계 수치

## 2. 대시보드 구성 설계 (Static Layout)

### [Header & Hero]
- 타이틀: "국민연금 가입 사업장 데이터 분석 대시보드"

### [KPI Section - 카드형 레이아웃]
- **총 사업장 수**: 582,825개
- **평균 가입자 수**: 19.5명
- **당월 고지금액**: 약 7.15M (평균)

### [Main Visualization Grid]
1. **지역별 현황 (Bar Chart)**: 보고서의 '상위 10개 광역시도별 사업장 수' 데이터를 Chart.js로 구현
2. **사업장 분포 (Image View)**: `images/sub_dist.png` 및 `images/form_pie.png`를 반응형 카드 내에 배치
3. **고용 유동성 (Scatter Plot Area)**: `images/new_lost_scatter.png` 이미지를 설명과 함께 배치

### [Insight Section]
- 보고서의 '종합 결론' 내용을 카드 형태의 텍스트 영역으로 배치

## 3. 구현 프롬프트 예시 (HTML/CSS/JS)

```markdown
"보고서 `eda_report.md`의 내용을 바탕으로 단일 파일 HTML 대시보드를 만들어줘.
1. Tailwind CSS를 사용하여 현대적인 대시보드 레이아웃(Grid 시스템)을 구성해.
2. 상단에는 총 사업장 수, 평균 가입자 수 등 주요 통계를 보여주는 KPI 카드를 배치해줘.
3. '광역시도별 사업장 수' 데이터를 사용하여 Chart.js 막대 그래프를 중앙에 배치해.
4. `images/` 폴더에 있는 시각화 결과 이미지들을 슬롯에 맞춰 적절히 배치해줘."
```
