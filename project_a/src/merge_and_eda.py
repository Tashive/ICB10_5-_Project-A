import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

base_dir = r'c:\Users\tasha\Desktop\ICB10\project_a'
old_file = os.path.join(base_dir, 'data', '대한무역투자진흥공사_4대 소비재 국가별 수출금액 (화장품)_20221231.csv')
new_file = os.path.join(base_dir, 'data', '수출입 실적(품목별+국가별)_20260506.csv')
img_dir = os.path.join(base_dir, 'images')
out_file = os.path.join(base_dir, 'data', 'merged_eda_output.txt')
os.makedirs(img_dir, exist_ok=True)

# 1. Load Old Data
df_old = pd.read_csv(old_file, encoding='cp949')

# 2. Load New Data
df_new = pd.read_csv(new_file, encoding='utf-8')
df_new = df_new[df_new['기간'] != '총계'].copy()
df_new['기간'] = df_new['기간'].astype(str).str.strip()
df_new['수출 금액'] = pd.to_numeric(df_new['수출 금액'], errors='coerce').fillna(0)

# Multiply by 1000 to match old data scale (USD)
df_new['수출 금액'] = df_new['수출 금액'] * 1000

# Group and pivot
df_new_grouped = df_new.groupby(['국가', '기간'])['수출 금액'].sum().reset_index()
df_new_pivot = df_new_grouped.pivot(index='국가', columns='기간', values='수출 금액').fillna(0)

# Rename to match old data
df_new_pivot.index.name = '국가명'
df_new_pivot.reset_index(inplace=True)

# 3. Merge Data
df_merged = pd.merge(df_old, df_new_pivot, on='국가명', how='outer')
df_merged.fillna(0, inplace=True)

years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
# Ensure all year columns exist (some might be missing if data doesn't have it, but we expect up to 2025)
for y in years:
    if y not in df_merged.columns:
        df_merged[y] = 0

# Convert to int
df_merged[years] = df_merged[years].astype(np.int64)

# 4. EDA Output
with open(out_file, 'w', encoding='utf-8') as f:
    f.write("=== 2. Basic Data Exploration ===\n")
    f.write(f"Shape: {df_merged.shape}\n")
    f.write(f"Duplicates: {df_merged.duplicated().sum()}\n\n")
    f.write("Head(5):\n")
    f.write(df_merged.head(5).to_string() + "\n\n")
    f.write("Tail(5):\n")
    f.write(df_merged.tail(5).to_string() + "\n\n")
    
    import io
    buf = io.StringIO()
    df_merged.info(buf=buf)
    f.write("Info:\n" + buf.getvalue() + "\n\n")
    
    f.write("=== 3. Descriptive Statistics ===\n")
    f.write("Numerical Describe:\n")
    f.write(df_merged.describe().to_string() + "\n\n")
    f.write("Categorical Describe (국가명):\n")
    f.write(df_merged[['국가명']].describe().to_string() + "\n\n")
    
    # Text Analysis
    vectorizer = TfidfVectorizer(max_features=30)
    tfidf_matrix = vectorizer.fit_transform(df_merged['국가명'])
    feature_names = vectorizer.get_feature_names_out()
    sums = tfidf_matrix.sum(axis=0).A1
    tfidf_df = pd.DataFrame({'Keyword': feature_names, 'TF-IDF Sum': sums}).sort_values(by='TF-IDF Sum', ascending=False)
    f.write("=== 4. Text Analysis (TF-IDF) ===\n")
    f.write(tfidf_df.to_string() + "\n\n")

    plt.figure(figsize=(10,6))
    plt.bar(tfidf_df['Keyword'], tfidf_df['TF-IDF Sum'], color='skyblue')
    plt.xticks(rotation=45)
    plt.title("TF-IDF Keywords Frequency (Merged)")
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'merged_fig_00_tfidf.png'))
    plt.close()

    # Visualizations
    # 1. Total Exports
    total_exports = df_merged[years].sum()
    f.write("=== Table 1: Total Exports ===\n")
    f.write(total_exports.to_string() + "\n\n")
    plt.figure(figsize=(10,5))
    total_exports.plot(kind='bar', color='coral')
    plt.title('연도별 화장품 총 수출금액 (2018-2025)')
    plt.ylabel('수출금액')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'merged_fig_01_total_exports.png'))
    plt.close()

    # 2. 2025 Distribution
    f.write("=== Table 2: 2025 Export Quantiles ===\n")
    f.write(df_merged['2025'].quantile([0, 0.25, 0.5, 0.75, 0.9, 0.99, 1]).to_string() + "\n\n")
    plt.figure(figsize=(8,5))
    np.log1p(df_merged['2025']).plot(kind='hist', bins=30, color='lightgreen')
    plt.title('2025년 수출금액 분포 (Log Scale)')
    plt.xlabel('Log(수출금액 + 1)')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'merged_fig_02_export_dist_2025.png'))
    plt.close()

    # 3. Boxplot over years
    plt.figure(figsize=(10,5))
    np.log1p(df_merged[years]).boxplot()
    plt.title('연도별 수출금액 분포 변화 (Log Scale)')
    plt.ylabel('Log(수출금액 + 1)')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'merged_fig_03_boxplot_years.png'))
    plt.close()

    # 4. Top 10 in 2025
    top10_2025 = df_merged.nlargest(10, '2025')[['국가명', '2025']]
    f.write("=== Table 4: Top 10 Countries 2025 ===\n")
    f.write(top10_2025.to_string() + "\n\n")
    plt.figure(figsize=(10,6))
    plt.bar(top10_2025['국가명'], top10_2025['2025'], color='purple')
    plt.title('2025년 화장품 수출액 Top 10 국가')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'merged_fig_04_top10_2025.png'))
    plt.close()

    # 5. Correlation Heatmap
    corr = df_merged[years].corr()
    f.write("=== Table 5: Correlation ===\n")
    f.write(corr.to_string() + "\n\n")
    plt.figure(figsize=(8,6))
    plt.imshow(corr, cmap='coolwarm', vmin=0.8, vmax=1)
    plt.colorbar()
    plt.xticks(range(len(years)), years)
    plt.yticks(range(len(years)), years)
    for i in range(len(years)):
        for j in range(len(years)):
            plt.text(j, i, f"{corr.iloc[i, j]:.2f}", ha='center', va='center', color='black', fontsize=8)
    plt.title('연도별 상관관계')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'merged_fig_05_corr.png'))
    plt.close()

    # 6. Scatter 2024 vs 2025
    plt.figure(figsize=(8,6))
    plt.scatter(np.log1p(df_merged['2024']), np.log1p(df_merged['2025']), alpha=0.5)
    plt.plot([0, 15], [0, 15], 'r--')
    plt.title('2024 vs 2025 수출금액 (Log Scale)')
    plt.xlabel('Log(2024 + 1)')
    plt.ylabel('Log(2025 + 1)')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'merged_fig_06_scatter.png'))
    plt.close()

    # 7. Growth Rate 22 to 25
    # Let's compare 2022 (end of old data) with 2025
    df_merged['growth_22_25'] = np.where(df_merged['2022'] > 0, (df_merged['2025'] - df_merged['2022']) / df_merged['2022'] * 100, np.nan)
    f.write("=== Table 7: Growth 22-25 ===\n")
    f.write(df_merged['growth_22_25'].describe().to_string() + "\n\n")
    plt.figure(figsize=(8,5))
    df_merged['growth_22_25'].clip(-100, 500).plot(kind='hist', bins=30, color='teal')
    plt.title('2022 대비 2025 수출 성장률 분포 (Clip -100% ~ 500%)')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'merged_fig_07_growth.png'))
    plt.close()

    # 8. Top 5 Trend (2018-2025)
    top5_names = df_merged.nlargest(5, '2025')['국가명'].values
    top5_df = df_merged[df_merged['국가명'].isin(top5_names)].set_index('국가명')[years].T
    f.write("=== Table 8: Top 5 Trend ===\n")
    f.write(top5_df.to_string() + "\n\n")
    plt.figure(figsize=(10,6))
    top5_df.plot(marker='o')
    plt.title('상위 5개국 연도별 수출금액 추이 (2018-2025)')
    plt.ylabel('수출금액')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'merged_fig_08_top5_trend.png'))
    plt.close()

    # 9. Cumulative Share 2025
    sorted_2025 = df_merged.sort_values(by='2025', ascending=False)
    sorted_2025['cum_share'] = sorted_2025['2025'].cumsum() / sorted_2025['2025'].sum() * 100
    plt.figure(figsize=(10,6))
    plt.plot(range(1, 21), sorted_2025['cum_share'].head(20), marker='o', color='red')
    plt.title('2025년 수출금액 상위 20개국 누적 점유율')
    plt.xlabel('상위 국가 수 (순위)')
    plt.ylabel('누적 점유율 (%)')
    plt.ylim(0, 100)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'merged_fig_09_cum_share.png'))
    plt.close()

    # 10. Missing or zero values by year
    zero_counts = (df_merged[years] == 0).sum()
    f.write("=== Table 10: Zero/Missing values per year ===\n")
    f.write(zero_counts.to_string() + "\n\n")
    plt.figure(figsize=(8,5))
    zero_counts.plot(kind='line', marker='x', color='brown')
    plt.title('연도별 수출실적 없는(0원) 국가 수')
    plt.ylabel('국가 수')
    plt.ylim(0, max(zero_counts)*1.2)
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'merged_fig_10_zero_counts.png'))
    plt.close()

print("Merged EDA Python script completed.")
