import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Setup directories
base_dir = r'c:\Users\tasha\Desktop\ICB10\project_a'
data_path = os.path.join(base_dir, 'data', '대한무역투자진흥공사_4대 소비재 국가별 수출금액 (화장품)_20221231.csv')
img_dir = os.path.join(base_dir, 'images')
os.makedirs(img_dir, exist_ok=True)
out_file = os.path.join(base_dir, 'data', 'eda_output.txt')

# Load data
df = pd.read_csv(data_path, encoding='cp949')

with open(out_file, 'w', encoding='utf-8') as f:
    f.write("=== 2. Basic Data Exploration ===\n")
    f.write(f"Shape: {df.shape}\n")
    f.write(f"Duplicates: {df.duplicated().sum()}\n\n")
    f.write("Head(5):\n")
    f.write(df.head(5).to_string() + "\n\n")
    f.write("Tail(5):\n")
    f.write(df.tail(5).to_string() + "\n\n")
    
    # Info
    import io
    buf = io.StringIO()
    df.info(buf=buf)
    f.write("Info:\n" + buf.getvalue() + "\n\n")
    
    f.write("=== 3. Descriptive Statistics ===\n")
    f.write("Numerical Describe:\n")
    f.write(df.describe().to_string() + "\n\n")
    f.write("Categorical Describe (국가명):\n")
    f.write(df[['국가명']].describe().to_string() + "\n\n")
    
    f.write("=== 4. Categorical & Text Data Analysis ===\n")
    f.write("Frequency of categorical (국가명 top 5):\n")
    f.write(df['국가명'].value_counts().head(5).to_string() + "\n\n")
    
    # TF-IDF on text
    vectorizer = TfidfVectorizer(max_features=30)
    tfidf_matrix = vectorizer.fit_transform(df['국가명'])
    feature_names = vectorizer.get_feature_names_out()
    sums = tfidf_matrix.sum(axis=0).A1
    tfidf_df = pd.DataFrame({'Keyword': feature_names, 'TF-IDF Sum': sums})
    tfidf_df = tfidf_df.sort_values(by='TF-IDF Sum', ascending=False)
    f.write("TF-IDF Top Keywords:\n")
    f.write(tfidf_df.to_string() + "\n\n")
    
    # TF-IDF plot
    plt.figure(figsize=(10,6))
    plt.bar(tfidf_df['Keyword'], tfidf_df['TF-IDF Sum'], color='skyblue')
    plt.xticks(rotation=45)
    plt.title("TF-IDF Keywords Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'fig_00_tfidf.png'))
    plt.close()

    years = ['2018', '2019', '2020', '2021', '2022']
    
    # Visualization 1: Total Exports per year
    total_exports = df[years].sum()
    f.write("=== Table 1: Total Exports ===\n")
    f.write(total_exports.to_string() + "\n\n")
    plt.figure(figsize=(8,5))
    total_exports.plot(kind='bar', color='coral')
    plt.title('연도별 화장품 총 수출금액')
    plt.ylabel('수출금액')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'fig_01_total_exports.png'))
    plt.close()
    
    # Visualization 2: Distribution of exports in 2022 (log)
    f.write("=== Table 2: 2022 Export Quantiles ===\n")
    f.write(df['2022'].quantile([0, 0.25, 0.5, 0.75, 0.9, 0.99, 1]).to_string() + "\n\n")
    plt.figure(figsize=(8,5))
    np.log1p(df['2022']).plot(kind='hist', bins=30, color='lightgreen')
    plt.title('2022년 수출금액 분포 (Log Scale)')
    plt.xlabel('Log(수출금액 + 1)')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'fig_02_export_dist_2022.png'))
    plt.close()
    
    # Visualization 3: Boxplots over years (log)
    f.write("=== Table 3: Yearly Stats ===\n")
    f.write(df[years].describe().to_string() + "\n\n")
    plt.figure(figsize=(8,5))
    np.log1p(df[years]).boxplot()
    plt.title('연도별 수출금액 분포 변화 (Log Scale)')
    plt.ylabel('Log(수출금액 + 1)')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'fig_03_boxplot_years.png'))
    plt.close()
    
    # Visualization 4: Top 10 countries in 2022
    top10_2022 = df.nlargest(10, '2022')[['국가명', '2022']]
    f.write("=== Table 4: Top 10 Countries 2022 ===\n")
    f.write(top10_2022.to_string() + "\n\n")
    plt.figure(figsize=(10,6))
    plt.bar(top10_2022['국가명'], top10_2022['2022'], color='purple')
    plt.title('2022년 화장품 수출액 Top 10 국가')
    plt.ylabel('수출금액')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'fig_04_top10_countries_2022.png'))
    plt.close()
    
    # Visualization 5: Correlation Heatmap
    corr = df[years].corr()
    f.write("=== Table 5: Correlation Matrix ===\n")
    f.write(corr.to_string() + "\n\n")
    plt.figure(figsize=(6,5))
    plt.imshow(corr, cmap='coolwarm', vmin=0.8, vmax=1)
    plt.colorbar()
    plt.xticks(range(len(years)), years)
    plt.yticks(range(len(years)), years)
    plt.title('연도별 수출금액 상관관계')
    for i in range(len(years)):
        for j in range(len(years)):
            plt.text(j, i, f"{corr.iloc[i, j]:.2f}", ha='center', va='center', color='black')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'fig_05_corr_heatmap.png'))
    plt.close()
    
    # Visualization 6: Scatter 2021 vs 2022
    f.write("=== Table 6: 2021 vs 2022 (Sample) ===\n")
    f.write(df[['국가명', '2021', '2022']].head().to_string() + "\n\n")
    plt.figure(figsize=(8,6))
    plt.scatter(np.log1p(df['2021']), np.log1p(df['2022']), alpha=0.5)
    plt.plot([0, 15], [0, 15], 'r--')
    plt.title('2021년 vs 2022년 수출금액 (Log Scale)')
    plt.xlabel('Log(2021 수출금액 + 1)')
    plt.ylabel('Log(2022 수출금액 + 1)')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'fig_06_scatter_2021_2022.png'))
    plt.close()
    
    # Visualization 7: Bottom 10 Non-Zero in 2022
    non_zero = df[df['2022'] > 0]
    bottom10 = non_zero.nsmallest(10, '2022')[['국가명', '2022']]
    f.write("=== Table 7: Bottom 10 (Non-Zero) 2022 ===\n")
    f.write(bottom10.to_string() + "\n\n")
    plt.figure(figsize=(10,6))
    plt.bar(bottom10['국가명'], bottom10['2022'], color='orange')
    plt.title('2022년 화장품 수출액 하위 10개국 (0원 초과)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'fig_07_bottom10_countries_2022.png'))
    plt.close()
    
    # Visualization 8: Growth Rate 2021 to 2022
    df['growth_21_22'] = np.where(df['2021'] > 0, (df['2022'] - df['2021']) / df['2021'] * 100, np.nan)
    f.write("=== Table 8: Growth Rate 21->22 Stats ===\n")
    f.write(df['growth_21_22'].describe().to_string() + "\n\n")
    plt.figure(figsize=(8,5))
    df['growth_21_22'].clip(-100, 300).plot(kind='hist', bins=30, color='teal')
    plt.title('2021 대비 2022 수출 성장률 분포 (Clip -100% ~ 300%)')
    plt.xlabel('성장률 (%)')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'fig_08_growth_rate.png'))
    plt.close()
    
    # Visualization 9: Top 5 Trend Line
    top5_names = top10_2022['국가명'].head(5).values
    top5_df = df[df['국가명'].isin(top5_names)].set_index('국가명')[years].T
    f.write("=== Table 9: Top 5 Trend ===\n")
    f.write(top5_df.to_string() + "\n\n")
    plt.figure(figsize=(8,5))
    top5_df.plot(marker='o')
    plt.title('상위 5개국 연도별 수출금액 추이')
    plt.ylabel('수출금액')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'fig_09_top5_trend.png'))
    plt.close()
    
    # Visualization 10: Cumulative Share 2022
    sorted_2022 = df.sort_values(by='2022', ascending=False)
    sorted_2022['cum_share'] = sorted_2022['2022'].cumsum() / sorted_2022['2022'].sum() * 100
    f.write("=== Table 10: Cumulative Share 2022 (Top 10) ===\n")
    f.write(sorted_2022[['국가명', '2022', 'cum_share']].head(10).to_string() + "\n\n")
    plt.figure(figsize=(10,6))
    plt.plot(range(1, 21), sorted_2022['cum_share'].head(20), marker='o', color='red')
    plt.title('2022년 수출금액 상위 20개국 누적 점유율')
    plt.xlabel('상위 국가 수 (순위)')
    plt.ylabel('누적 점유율 (%)')
    plt.ylim(0, 100)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'fig_10_cumulative_share.png'))
    plt.close()

    print("EDA Python script completed successfully.")
