import os
import pandas as pd
import csv
from lib.file_operator import FileOperator

# CSV 操作クラス
class CsvOperator(FileOperator):
    def __init__(self):
        super().__init__()
        self.output_encoding = 'utf8'   # utf8 or cp932
        self.output_format = 'csv'      # csv or tsv

    def getOutputFileName(self):
        return 'sample.csv'

    def read(self, file_path):
        # pandas の関数で読み込み
        df = pd.read_csv(
            file_path,
            dtype = object, # 全ての列を文字列にする
        )
        return df

    def write(self, df, file_path):
        print('出力ファイル（文字コード）：{}'.format(self.output_encoding))
        print('出力ファイル（フォーマット）：{}'.format(self.output_format))
        if self.output_format == 'tsv':
            sep = '\t'
        else:
            sep = ','
        # CSV ファイル出力
        df.to_csv(
            file_path,
            index = False,                      # インデックスを出力しない
            encoding = self.output_encoding,    # 文字コードを内部エンコーディング指定
            quoting = csv.QUOTE_ALL,            # すべてをタブルクオートさせて出力
            sep = sep,                          # 区切り文字
        )
