# [Prompt] 국민연금 가입 사업장 분석 웹 대시보드 구축 기획

이 문서는 기존 수행된 국민연금 가입 사업장 내역 EDA 결과를 바탕으로, 이를 인터랙티브한 웹 대시보드로 시각화하기 위한 상세 기획 및 구현 프롬프트를 포함합니다.

---

## 1. 프로젝트 개요
- **목적**: 국민연금 가입 사업장의 규모, 지역, 업종별 분포 및 고용 추이를 한눈에 파악할 수 있는 대시보드 구축
- **핵심 가치**: 데이터 기반의 경제 활동 모니터링 및 시각적 인사이트 제공
- **주요 타겟**: 데이터 분석가, 정책 결정자, 비즈니스 전략 담당자

## 2. 디자인 시스템 (Style Guide)
기존 EDA 리포트의 톤앤매너를 유지하며 현대적인 **Bento Grid** 스타일을 적용합니다.

- **Font**: 'Pretendard', sans-serif
- **Color Palette**:
  - `Background`: `#f0f2f5` (Light Gray)
  - `Primary (Dark)`: `#1a1a2e`
  - `Accent Yellow`: `#e8ff3b`
  - `Accent Coral`: `#ff6b6b`
  - `Accent Teal`: `#4ecdc4`
  - `Card Background`: `white` (Radius: 20px, Shadow: Light)

## 3. 대시보드 레이아웃 (Bento Grid 구성)
화면은 4x4 또는 4xN 그리드 시스템으로 구성하며, 각 카드는 데이터의 중요도에 따라 그리드 점유율(Span)을 다르게 가져갑니다.

### Row 1: Key Performance Indicators (KPI)
- **전체 데이터 규모**: 100K (Dark Card)
- **평균 가입자 수**: 41.2명 (Accent Yellow)
- **평균 보험료**: 16M (Dark Card)
- **고용 안정성 지표**: 신규/상실 비율 1.2 (Accent Teal)

### Row 2: 분포 및 통계 인사이트
- **주요 사업장 샘플 Table**: 사업장명, 가입자, 보험료, 시도 정보를 포함한 리스트 (Span 3)
- **가입 상태**: Active 99% (Accent Coral, Span 1)

### Row 3 & 4: 핵심 시각화 (Charts)
- **가입자 수 분포**: 10인 미만 영세 사업장 집중도 시각화 (`vis1_subscribers_dist.png` 참고)
- **지역별 분포**: 수도권 집중도(50% 이상) 및 지역별 편차 시각화 (`vis3_region_dist.png` 참고)
- **업종별 TOP 20**: 서비스 및 소매업 비중 시각화 (`vis2_industry_count.png` 참고)
- **연도별 추이**: 신규 적용 사업장의 증가세 시각화 (`vis4_yearly_new.png` 참고)

## 4. 인터랙티브 기능 요구 사항
1. **필터링 기능**:
   - 시도별 필터 (서울특별시, 경기도 등)
   - 사업장 규모별 필터 (5인 이하, 10인 이하, 대규모 등)
   - 업종별 필터
2. **호버 액션**: 시각화 차트의 데이터 포인트 호버 시 상세 수치 툴팁 표시
3. **반응형 디자인**: 모바일 및 태블릿 환경에서도 그리드가 적절히 재배치되는 레이아웃 구현

## 5. 기술 스택 제안 (Implementation Task)
이 프롬프트를 사용하여 다음과 같은 환경에서 대시보드를 구현하십시오.

- **Architecture**: Single HTML File (Index.html)
- **Styling**: Vanilla CSS (Modern CSS Grid layout)
- **Visualization**: Chart.js (CDN 활용)
- **Icons**: Lucide Icons (CDN 활용)
- **Fonts**: Google Fonts (Pretendard 지원 폰트 또는 시스템 폰트)

---

## [Final Instruction for AI]
> 상기 기획 내용을 바탕으로, **단일 HTML 파일로 구성된 국민연금 가입 사업장 대시보드**를 구현해 주세요. 별도의 빌드 과정 없이 브라우저에서 바로 실행 가능해야 하며, `EDA_Report.marp.md`에서 사용된 Bento Grid 스타일의 시각적 완성도를 극대화해야 합니다. 외부 라이브러리는 CDN을 통해 로드하고, 내부 JS로 가상의 데이터를 처리하거나 인터랙티브 요소를 제어하도록 작성해 주세요. 시각화 영역에는 Chart.js를 활용하여 리포트의 주요 지표들을 미려하게 표현해 주시기 바랍니다.
