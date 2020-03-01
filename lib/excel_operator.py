import os
import pandas as pd
import csv
from lib.csv_operator import CsvOperator

# Excel 操作クラス
class ExcelOperator(CsvOperator):
    def read(self, file_path):
        # pandas の関数で読み込み
        df = pd.read_excel(
            file_path,
            dtype = object, # 全ての列を文字列にする
        )
        return df

    def write(self, df, file_path):
        # ファイル出力
        df.to_excel(
            file_path,
            index = False,              # インデックスを出力しない
            # encoding = 'cp932',         # 文字コードを SJIS にする
            # quoting = csv.QUOTE_ALL,    # すべてをタブルクオートさせて出力
        )
