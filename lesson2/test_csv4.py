import os
import pandas as pd

def csv_output():
    path = os.path.dirname(__file__)
    # pandas の関数で読み込み
    df = pd.read_csv(
        path + '/sample_sjis-line100.csv',
        # engine = "python", # 日本語 CSV ファイル名の読み込み
        encoding = "cp932", # Windows環境では文字コードは"cp932"
    )
    print(df)

csv_output()
