import os
import pandas as pd

def csv_output():
    path = os.path.dirname(__file__)
    # pandas の関数で読み込み
    df = pd.read_excel(
        path + '/sample_sjis-line100.xlsx',
    )
    print(df)

csv_output()
