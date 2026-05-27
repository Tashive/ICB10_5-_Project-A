# [프롬프트] 국민연금 가입 사업장 데이터 분석 HTML 대시보드 구축 계획

본 문서는 `nps-company` 프로젝트의 EDA 결과물을 바탕으로, 별도의 서버 없이 웹 브라우저에서 즉시 실행 가능한 **HTML 정적 페이지 기반의 인터랙티브 대시보드**를 구축하기 위한 상세 기획 프롬프트입니다.

---

## 1. 프로젝트 개요
- **목표**: 58만 건의 데이터 인사이트를 담은 고품질 단일 HTML 대시보드 개발.
- **주요 타겟**: 보고서 수신자, 데이터 이해관계자 (설치 없이 브라우저로 열람).
- **디자인 컨셉**: 프리미엄 다크 테마, Glassmorphism UI, 네온 포인트 컬러 (`#38bdf8`).

## 2. 기술 스택 요구사항
- **Language**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Tailwind CSS (CDN 사용 권장)
- **Icons**: Lucide Icons 또는 FontAwesome (CDN)
- **Visualization**: 
  - Chart.js (차트 및 그래프)
  - Simple Heatmaps or SVG Maps (지역별 시각화)
- **Data**: JSON 형식으로 스크립트 내 내장하거나 별도 JSON 파일 로드.

## 3. 데이터 및 핵심 지표 (Reference: `eda_report.md`)
- **KPI 데이터**:
  - 전체 사업장: 582,825개
  - 평균 가입자: 19.56명
  - 가입 유지율: 94.2%
  - 법인/개인 비중: 법인(52.5만), 개인(5.7만)
- **이미지 리소스**: `../images/` 폴더 내의 정적 이미지들을 레이아웃에 배치.

## 4. 대시보드 레이아웃 설계

### Section 1: Header & Key Metrics
- 좌측에 제목(NPS Data Insight)과 로고 배치.
- 우측에 4개의 **Glass-Card 스타일 KPI** 카드 배치:
  - 총 사업장 / 평균 가입자 / 평균 고지금액 / 가입 유지율.

### Section 2: 메인 그리드 (3단 구성)
- **좌측 컬럼 (Summary & Distribution)**:
  - 가입자 수 분포 (이미지 또는 Chart.js 히스토그램).
  - 사업장 가입 상태 비중 (도넛 차트).
- **중앙 컬럼 (Primary Insights)**:
  - 가입자 수 vs 고지금액 산점도 (이미지).
  - 업종별 평균 가입자 Top 10 (가로 막대 차트).
- **우측 컬럼 (Trends & Keywords)**:
  - 지역별 고용 현황 (지도 이미지 또는 SVG 맵).
  - TF-IDF 키워드 클라우드 (이미지).

### Section 3: 상세 분석 테이블 (Bottom)
- 주요 업종별 통계 데이터를 담은 세련된 다크 테마 데이터 테이블.

## 5. UI/UX 세부 지침
- **Background**: `bg-slate-950` (매우 어두운 남색)
- **Glassmorphism**: `bg-white/5 backdrop-blur-md border border-white/10` 적용.
- **Typography**: Inter 또는 Pretendard 폰트 사용.
- **Responsiveness**: 모바일 대응을 위한 Flex/Grid 반응형 레이아웃.
- **Interaction**: 카드 호버 시 스케일 업 효과, 버튼 클릭 시 탭 전환(필요 시).

## 6. 구현 단계별 가이드
1. **HTML 골격 작성**: 기본적인 섹션 구분 및 Tailwind CSS 연동.
2. **Glass-Card 컴포넌트 제작**: 카드 스타일 및 KPI 수치 배치.
3. **이미지 및 차트 통합**: `../images/` 경로의 파일들을 적재적소에 배치하고 Chart.js로 동적 요소 추가.
4. **JS 인터랙션**: 탭 전환(개요/산업/지역) 기능을 구현하여 정보 밀도 조절.
5. **최종 폴리싱**: 애니메이션 효과(`framer-motion` 라이브러리 유사 효과) 및 폰트 세밀 조정.

---
**주의사항**: 본 대시보드는 정적 파일(Self-contained)로서의 가치를 위해 외부 의존성을 최소화하고, `images/` 폴더 내의 분석 결과물을 시각적 핵심으로 사용해야 함.
