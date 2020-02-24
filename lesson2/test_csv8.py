import os
import pandas as pd
import csv

def csv_input(path):
    file_name = path + '/sample_sjis-line100.xlsx'
    # pandas の関数で読み込み
    df = pd.read_excel(
        file_name,
        dtype = object, # 全ての列を文字列にする
    )
    return df

def csv_output(path, df):
    # ディレクトリが存在しない場合は作成
    if os.path.exists(path) != True:
        os.mkdir(path)
    file_name = path + '/sample_sjis-line100.csv'
    # CSV ファイル出力
    print(file_name)
    df.to_csv(
        file_name,
        index = False,              # インデックスを出力しない
        encoding = 'cp932',         # 文字コードを SJIS にする
        quoting = csv.QUOTE_ALL,    # すべてをタブルクオートさせて出力
    )

# 実行ファイルのカレントパスを取得
current_path = os.path.dirname(__file__)
# ファイル入力
df = csv_input(current_path)

# 出力先パスを生成
output_path = current_path + '/output'
# ファイル出力
csv_output(output_path, df)
