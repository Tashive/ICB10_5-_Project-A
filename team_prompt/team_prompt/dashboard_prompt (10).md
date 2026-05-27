# 웹 대시보드 개발 계획 프롬프트

## 1. 프로젝트 개요 및 목적
국민연금 가입 사업장 데이터를 활용하여 주요 통계 및 시각화 자료를 제공하는 HTML 기반의 정적 웹 대시보드를 개발합니다. 주요 목적은 사용자가 국민연금 데이터를 통해 대한민국의 고용 시장 트렌드, 지역별 경제 활동, 사업장 규모별 특성 등을 쉽게 탐색하고 이해할 수 있도록 하는 것이며, 배포 용이성과 경량성에 중점을 둡니다.

## 2. 주요 사용자
- 데이터 분석가 및 연구원: 심층 분석 결과를 HTML 형태로 빠르게 공유 및 확인
- 정책 입안자: 고용 시장 현황을 직관적으로 파악하고 정적인 보고서 형태로 활용
- 일반 대중: 국민연금 관련 정보에 대한 접근성 향상 및 데이터 기반 이해 증진

## 3. 대시보드에 포함될 주요 시각화 및 지표

### 개요 대시보드 (Overview Dashboard)
- **주요 지표**:
    - 전체 사업장 수
    - 전체 가입자 수
    - 총 당월고지금액
    - 신규가입자수 / 상실가입자수 추이
- **주요 시각화**:
    - **가입자수 분포 (Log Scale)**: 대부분의 사업장이 소규모(10인 미만)에 집중되어 있음을 보여주는 히스토그램. (`vis_1_hist_subscribers.png` 참고)
    - **당월고지금액 분포 (Log Scale)**: 고지 금액의 불균형을 보여주는 히스토그램. (`vis_2_hist_amount.png` 참고)
    - **지역별 연금 재정 기여도 비중**: 각 지역이 전체 연금 고지 금액에서 차지하는 비중을 파이 차트로 표시. (`vis_7_pie_region_total_amt.png` 참고)
    - **지역별 평균 가입자수 비교**: 특정 지역의 평균 가입자 규모가 높은 것을 보여주는 막대 그래프. (`vis_4_bar_region_avg_sub.png` 참고)

### 상세 분석 대시보드 (Detailed Analysis Dashboard)
- **주요 지표**:
    - 사업장명, 산업명, 가입자수, 추정연봉, 월고지금액, 인당보험료
- **주요 시각화**:
    - **가입자수와 고지금액 산점도**: 가입자 수와 고지 금액 간의 강한 선형 관계를 보여주는 산점도. (`vis_3_scatter_sub_vs_amt.png` 참고)
    - **고용 역동성 분석 (신규 vs 상실)**: 신규 채용과 퇴직(상실) 간의 관계를 보여주는 산점도. (`vis_6_scatter_new_vs_lost.png` 참고)
    - **지표 간 상호작용 (Heatmap)**: 주요 수치 지표들 간의 상관 계수를 시각화. (`vis_8_heatmap_corr.png` 참고)
    - **본점 및 지점 간 가입자 규모 분석**: 본점과 지점의 가입자 규모를 비교하는 박스플롯. (`vis_5_box_hq_vs_branch.png` 참고)
    - **상위 N개 기업 리스트**: 추정 평균 연봉 상위 기업, 월 총 고지금액 상위 기업 등 표 형태로 제공. (`detailed_company_analysis.md`, `top_salary_companies.md` 참고)

## 4. 데이터 소스
- `nps-company/data/국민연금공단_국민연금 가입 사업장 내역_20260423.csv`

## 5. 기술 스택 (예상)
- **기본**: HTML5, CSS3, JavaScript
- **데이터 시각화 라이브러리**: Chart.js, D3.js 또는 유사 경량 라이브러리 (정적 데이터셋을 활용)
- **배포**: GitHub Pages, Netlify 등 정적 호스팅 서비스

## 6. 예상되는 기능
- **정적 시각화**: 미리 생성된 모든 시각화 차트 및 표를 HTML 페이지에 포함하여 제공
- **제한적 상호작용**: (선택적으로) 클라이언트 측 JavaScript를 이용한 간단한 데이터 필터링 또는 정렬 기능 (데이터셋이 크지 않을 경우)
- **정보 제공**: 각 시각화 및 지표에 대한 상세 설명 및 분석 결과 제공

## 7. 참고 보고서
- `nps-company/report/eda_report_nps.md`
- `nps-company/report/eda_basic_verification.md`
- `nps-company/report/eda_slides_nps.md`
- `nps-company/report/detailed_company_analysis.md`
- `nps-company/report/top_salary_companies.md`
