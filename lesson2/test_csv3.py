import os
import pandas as pd

def csv_output():
    path = os.path.dirname(__file__)
    # pandas の関数で読み込み
    df = pd.read_csv(path + '/sample_utf8.csv')
    print(df)

csv_output()
