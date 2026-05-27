---
marp: true
theme: default
paginate: true
header: "화장품 및 수출입 실적 데이터"
footer: "Data Analysis Report"
size: 16:9
---

<style>
/* 07 - Swiss International Style */
section {
  background-color: #FFFFFF;
  color: #111111;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  border-left: 16px solid #E8000D;
  position: relative;
}
section::after {
  content: '';
  position: absolute;
  bottom: 40px;
  right: 40px;
  width: 80px;
  height: 80px;
  border: 6px solid #E8000D;
  border-radius: 50%;
}
header, footer {
  font-family: 'Space Mono', 'Courier New', monospace;
  font-size: 14px;
  letter-spacing: 2px;
  color: #888888;
}
h1 {
  font-weight: 800;
  font-size: 54px;
  color: #111111;
  border-bottom: 3px solid #DDDDDD;
  padding-bottom: 20px;
  margin-bottom: 30px;
  letter-spacing: -1px;
}
h2 {
  font-weight: 700;
  font-size: 40px;
  color: #111111;
  letter-spacing: -0.5px;
}
h3 {
  color: #E8000D;
  font-weight: 700;
  font-size: 28px;
}
p, li {
  color: #444444;
  font-size: 22px;
  line-height: 1.6;
}
strong {
  color: #111111;
}
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 20px;
}
th {
  background-color: #111111;
  color: #FFFFFF;
  padding: 12px;
  font-weight: 600;
}
td {
  border-bottom: 1px solid #DDDDDD;
  padding: 12px;
  color: #444444;
}
</style>

# 화장품 및 수출입 실적 데이터
## 종합 탐색적 데이터 분석(EDA) 보고서 (2018~2025)

---

## 1. 기본 데이터 탐색 (Basic Data Exploration)

- **데이터 크기 (Shape):** 284행(Row), 9열(Column) (2018~2025 연도별 수출금액 병합)
- **중복 데이터 (Duplicates):** 0건
- **결측치 및 데이터 타입 (Info):** 
  - 2018-2022 데이터와 최신 2023-2025 데이터 병합 완료
  - 2023-2025 데이터(천 달러)를 USD 단위로 변환 후 결합
  - 결측치는 0으로 대치, 모든 연도 열은 정수형(int64) 유지

---

## 데이터 미리보기 (Head 5)

| 인덱스 | 국가명 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 가나 | 33,449 | 23,738 | 126,101 | 90,519 | 122,100 | 196,000 | 244,000 | 767,000 |
| 1 | 가봉 | 22 | 0 | 363 | 10 | 1,091 | 1,000 | 14,000 | 10,000 |
| 2 | 가이아나 | 0 | 0 | 1,643 | 5,505 | 14,150 | 13,000 | 23,000 | 157,000 |
| 3 | 감비아 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | 건지 | 0 | 0 | 0 | 0 | 0 | 0 | 1,000 | 5,000 |

---

## 2. 기술 통계 분석 및 심층 인사이트

**총 8년(2018-2025) 기간의 K-뷰티 수출 통계 분석 결과, 극적인 체질 개선 확인**

### 💡 탈중국화(De-sinicization)와 북미/글로벌 시장의 폭발적 성장
- 중국: 2021년 48.8억 달러 정점 $\rightarrow$ 2025년 16.5억 달러로 추락
- 미국: 2021년 8.4억 달러 $\rightarrow$ 2025년 17.5억 달러 폭발적 증가
- **결과: 2025년 미국이 중국을 제치고 K-뷰티 최대 수출국 1위 등극**
- 일본(8.8억), 베트남, 러시아 등 견고한 실적으로 중국발 리스크 상쇄

---

## 2. 기술 통계 분석 및 심층 인사이트 (계속)

### 💡 전체 수출 규모의 V자 반등과 사상 최대 실적 경신
- 2021년 이후 하락세: 2022년(79.5억) $\rightarrow$ 2023년(71.8억)
- 2024년 급반등: 85.7억 달러 달성
- **2025년 역대 최고 실적:** 94.2억 달러 돌파
- K-뷰티 경쟁력이 특정 국가 의존을 넘어 글로벌 메가 트렌드로 안착함

---

## 2. 기술 통계 분석 및 심층 인사이트 (계속)

### 💡 수출 저변의 확대와 양극화의 부분적 완화
- 관리 국가 수 증가: 212개국 $\rightarrow$ 284개국
- 무실적(0원) 국가 감소: 2018년 123개국 $\rightarrow$ 2025년 88개국 (신흥 시장 개척)
- 수출액 중앙값(Median) 급증: 2022년 1.2만 달러 $\rightarrow$ 2025년 9만 달러
- 소규모 수출 국가들의 질적·양적 동반 성장 증명

---

## 3. 범주형 및 텍스트 데이터 분석

**284개 국가명 대상 TF-IDF 분석 (2023-2025 통합 특징)**

| Keyword | TF-IDF Sum | Keyword | TF-IDF Sum |
|---|---|---|---|
| 군도 | 7.000 | 사모아 | 2.000 |
| 세인트 | 4.000 | 아랍에미리트 | 2.000 |
| 제도 | 3.338 | 버진아일랜드 | 2.000 |
| 불령 | 2.098 | 가이아나 | 1.726 |
| 네덜란드 | 2.000 | 폴리네시아 | 1.726 |

**해석:** '군도', '세인트', '제도', '불령' 등 도서/자치령 명칭 상위권. 군소 시장의 데이터 편입 효과.

<div style="text-align: center;">
  <img src="../images/merged_fig_00_tfidf.png" alt="TF-IDF" width="400px">
</div>

---

## 4. 데이터 시각화 및 심층 분석

### 1) 통합 연도별 화장품 총 수출금액

| 연도 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| 수출액 | 91.7억 | 79.5억 | 71.8억 | 85.7억 | 94.2억 |

<div style="text-align: center;">
  <img src="../images/merged_fig_01_total_exports.png" alt="총 수출금액" width="700px">
</div>

**해석:** 2021년 정점 이후 V자 골짜기(2023)를 거쳐 2025년 94억 달러를 상회하는 역대 최고치 달성.

---

## 4. 데이터 시각화 및 심층 분석

### 2) 2025년 최신 수출금액 로그 분포

| 최솟값 | 50%(중앙값) | 75% | 최댓값 |
|---|---|---|---|
| 0 | 90,500 | 4,840,750 | 1,748,808,000 |

<div style="text-align: center;">
  <img src="../images/merged_fig_02_export_dist_2025.png" alt="2025년 로그 분포" width="700px">
</div>

**해석:** 중간 규모 구간에 밀집한 국가 증가. 종 모양(Bell-shape)에 가까워지며 시장 생태계의 허리가 탄탄해짐.

---

## 4. 데이터 시각화 및 심층 분석

### 3) 통합 연도별 수출금액 분포 변화 (Boxplot)

<div style="text-align: center;">
  <img src="../images/merged_fig_03_boxplot_years.png" alt="연도별 박스플롯" width="700px">
</div>

**해석:** 박스 내부 중앙선의 꾸준한 상승. 2023년 이후 하단 꼬리가 짧아져 하위권 국가들의 수입 규모 확대를 방증.

---

## 4. 데이터 시각화 및 심층 분석

### 4) 2025년 화장품 수출액 Top 10 국가

| 1위 미국 | 2위 중국 | 3위 일본 | 4위 홍콩 | 5위 베트남 |
|---|---|---|---|---|
| 17.5억 | 16.5억 | 8.8억 | 6.0억 | 4.1억 |

<div style="text-align: center;">
  <img src="../images/merged_fig_04_top10_2025.png" alt="Top 10 국가 2025" width="700px">
</div>

**해석:** 미국(17.5억)이 중국(16.5억)을 제치고 K-뷰티 수출 1위 등극. 북미/아시아의 균형 잡힌 포트폴리오 구축.

---

## 4. 데이터 시각화 및 심층 분석

### 5) 8개년 연도별 수출금액 상관관계 히트맵

<div style="text-align: center;">
  <img src="../images/merged_fig_05_corr.png" alt="상관관계 히트맵" width="600px">
</div>

**해석:** 2018년과 2025년의 상관계수는 0.77 수준으로 하락. 8년 간 미국 1위 등극 등 시장 구조와 순위가 격변했음을 보여줌.

---

## 4. 데이터 시각화 및 심층 분석

### 6) 2024 vs 2025 최신 산점도

<div style="text-align: center;">
  <img src="../images/merged_fig_06_scatter.png" alt="24 vs 25 산점도" width="600px">
</div>

**해석:** 기준선(y=x) 위에 분포한 점이 다수(성장 국가 다수). 특히 우상단에서 미국과 중국의 순위 교차가 치열하게 나타남.

---

## 4. 데이터 시각화 및 심층 분석

### 7) 2022 대비 2025년 장기 수출 성장률 분포

| 1분위수(25%) | 50%(중앙값) | 3분위수(75%) |
|---|---|---|
| -100.0% | +113.0% | +375.2% |

<div style="text-align: center;">
  <img src="../images/merged_fig_07_growth.png" alt="성장률 분포" width="600px">
</div>

**해석:** 중앙값이 113%에 달해 절반 이상의 국가에서 3년 만에 수출액 2배 이상 증가. 일부는 500% 이상 폭발적 성장.

---

## 4. 데이터 시각화 및 심층 분석

### 8) 상위 5개국 연도별 격변 추이 (미국 vs 중국)

| 연도 | 2021 | 2023 | 2025 |
|---|---|---|---|
| 미국 | 8.4억 | 10.2억 | 17.5억 |
| 중국 | 48.8억 | 23.8억 | 16.5억 |

<div style="text-align: center;">
  <img src="../images/merged_fig_08_top5_trend.png" alt="상위 5개국 추이" width="600px">
</div>

**해석:** 중국의 급격한 우하향과 미국의 가파른 우상향. 2024-2025년 구간에서 두 국가의 골든크로스(데드크로스) 현상 발생.

---

## 4. 데이터 시각화 및 심층 분석

### 9) 2025년 누적 점유율 - 다변화의 증명

<div style="text-align: center;">
  <img src="../images/merged_fig_09_cum_share.png" alt="2025년 누적 점유율" width="700px">
</div>

**해석:** 과거 1국(중국) 의존(45%)에서 탈피. 2025년 1위 미국 18.5%, 2위 중국 17.5%로 상위 10개국이 비교적 고르게 파이를 나누는 선진국형 무역 구조.

---

## 4. 데이터 시각화 및 심층 분석

### 10) 연도별 실적 없는(0원) 국가 수 감소 추이

| 2018 | 2021 | 2023 | 2025 |
|---|---|---|---|
| 123 | 97 | 112 | 88 |

<div style="text-align: center;">
  <img src="../images/merged_fig_10_zero_counts.png" alt="실적 없음 그래프" width="700px">
</div>

**해석:** 2018년 123개국에서 2025년 역대 최저인 88개국으로 감소. 글로벌 커버리지가 지속적으로 넓어지고 있는 긍정적 시그널.
