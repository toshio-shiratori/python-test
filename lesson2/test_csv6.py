import os
import pandas as pd

def csv_output():
    path = os.path.dirname(__file__)
    # pandas の関数で読み込み
    df = pd.read_excel(
        path + '/sample_sjis-line100.xlsx',
        dtype = object, # 全ての列を文字列にする
    )
    print(df)

csv_output()
