import pandas as pd
import os

file_path = r'c:\Users\tasha\Desktop\ICB10\project_a\data\수출입 실적(품목별+국가별)_20260506.csv'
out_path = r'c:\Users\tasha\Desktop\ICB10\project_a\data\csv_head2.txt'

encodings = ['utf-8', 'cp949', 'euc-kr', 'utf-8-sig']
df = None

for enc in encodings:
    try:
        df = pd.read_csv(file_path, encoding=enc, nrows=10)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(f"Successfully decoded with {enc}\n")
            f.write("Columns:\n")
            f.write(str(list(df.columns)) + "\n\n")
            f.write("Head:\n")
            f.write(df.head().to_string())
        print(f"Success with {enc}")
        break
    except Exception as e:
        print(f"Failed with {enc}: {e}")
