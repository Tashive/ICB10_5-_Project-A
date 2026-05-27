import pandas as pd

file_path = r'c:\Users\tasha\Desktop\ICB10\project_a\data\대한무역투자진흥공사_4대 소비재 국가별 수출금액 (화장품)_20221231.csv'
df = pd.read_csv(file_path, encoding='cp949')

with open(r'c:\Users\tasha\Desktop\ICB10\project_a\data\csv_head.txt', 'w', encoding='utf-8') as f:
    f.write("=== HEAD ===\n")
    f.write(df.head(10).to_string())
    f.write("\n\n=== INFO ===\n")
    df.info(buf=f)
