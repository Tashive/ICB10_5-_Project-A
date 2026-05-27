# 국민연금 고용 데이터 대시보드 (Static HTML) 생성 프롬프트

이 프롬프트는 아래의 **실제 분석 데이터**를 활용하여 전문가 수준의 정적 HTML 대시보드를 생성하기 위한 것입니다.

## 1. 분석 데이터 (JSON)
AI는 아래 데이터를 JavaScript 상수로 정의하여 시각화에 활용해야 합니다.

```json
{
  "summary": {
    "total_establishments": 582825,
    "avg_subscribers": 19.56,
    "median_subscribers": 6,
    "avg_monthly_payment": 7154520,
    "new_acquisition_mean": 0.86,
    "lost_subscriber_mean": 0.71
  },
  "regional_distribution": [
    {"region": "경기", "count": 157651},
    {"region": "서울", "count": 131717},
    {"region": "경남", "count": 32900},
    {"region": "부산", "count": 31701},
    {"region": "경북", "count": 28732},
    {"region": "인천", "count": 28516},
    {"region": "충남", "count": 25295},
    {"region": "전남", "count": 22166},
    {"region": "충북", "count": 19625},
    {"region": "대구", "count": 19306},
    {"region": "대전", "count": 14381},
    {"region": "광주", "count": 14060},
    {"region": "울산", "count": 10771},
    {"region": "제주", "count": 7824},
    {"region": "세종", "count": 3414}
  ],
  "top_industries": [
    {"name": "BIZ_NO미존재사업장", "count": 78991},
    {"name": "배관 및 냉ㆍ난방 공사업", "count": 14840},
    {"name": "응용 소프트웨어 개발", "count": 13949},
    {"name": "비주거용 건물 임대업", "count": 9196},
    {"name": "상품 종합 도매업", "count": 9100},
    {"name": "유리 및 창호 공사업", "count": 9076},
    {"name": "일반의원", "count": 8797},
    {"name": "한식 일반 음식점업", "count": 8225},
    {"name": "실내 장식/목공사", "count": 8127},
    {"name": "미장/타일/방수공사", "count": 7709}
  ],
  "avg_payment_by_region": [
    {"region": "서울", "payment": 10942600},
    {"region": "울산", "payment": 8640900},
    {"region": "대전", "payment": 7442420},
    {"region": "충남", "payment": 6649770},
    {"region": "세종", "payment": 6499450},
    {"region": "경기", "payment": 6454530}
  ],
  "company_type": {
    "법인": 525186,
    "개인": 57639,
    "avg_sub_corp": 20.06,
    "avg_sub_indiv": 14.95
  }
}
```

## 2. 기술 및 디자인 요구사항
- **기술 스택**: HTML5, CSS3 (Vanilla), JavaScript (ES6+), [Chart.js (CDN)](https://cdn.jsdelivr.net/npm/chart.js)
- **테마**: **Aurora Neon (Dark Mode)**
    - 배경: `#0a0a0a`
    - 카드 배경: `rgba(255, 255, 255, 0.05)` (Glassmorphism 적용)
    - 주요 색상: 네온 그린(`#00ff87`), 사이언(`#60efff`), 퍼플(`#a29bfe`)
- **레이아웃**: 
    - Responsive Grid (모바일 대응)
    - 상단 KPI 섹션 (4개 카드)
    - 중간 2컬럼 차트 섹션 (지역별 분포, 업종별 순위)
    - 하단 와이드 섹션 (지역별 평균 급여 비교)

## 3. 기능 요구사항
- **인터랙티브 차트**: 마우스 호버 시 상세 수치 툴팁 출력.
- **숫자 애니메이션**: 페이지 로드 시 KPI 숫자가 0부터 목표치까지 올라가는 효과.
- **필터 (Simulation)**: 지역 선택 시 해당 지역의 데이터가 강조되거나 차트가 업데이트되는 로직 구현.

## 4. 최종 출력물 가이드
AI는 단일 파일(`index.html`)로 구성된 완성된 코드를 출력해야 합니다. 모든 CSS와 JS는 HTML 내부에 포함(Inline)하거나 가독성을 위해 `<style>` 및 `<script>` 태그로 분리하여 작성합니다.

---
**작성일**: 2026-05-09
**담당**: Gemini CLI Analyst
