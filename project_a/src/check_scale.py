import pandas as pd

new_file = r'c:\Users\tasha\Desktop\ICB10\project_a\data\수출입 실적(품목별+국가별)_20260506.csv'
df_new = pd.read_csv(new_file, encoding='utf-8')

# Exclude '총계'
df_new = df_new[df_new['기간'] != '총계'].copy()
df_new['기간'] = df_new['기간'].astype(str)

print("Unique periods in new data:", df_new['기간'].unique())

# Top 5 countries by 수출 금액 in 2023
df_2023 = df_new[df_new['기간'] == '2023']
top5 = df_2023.nlargest(5, '수출 금액')[['국가', '수출 금액']]
print("\nTop 5 in 2023 (New data):")
print(top5)

# Load old data
old_file = r'c:\Users\tasha\Desktop\ICB10\project_a\data\대한무역투자진흥공사_4대 소비재 국가별 수출금액 (화장품)_20221231.csv'
df_old = pd.read_csv(old_file, encoding='cp949')

top5_old = df_old.nlargest(5, '2022')[['국가명', '2022']]
print("\nTop 5 in 2022 (Old data):")
print(top5_old)
