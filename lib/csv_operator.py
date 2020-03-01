import os
import pandas as pd
import csv

# CSV 操作クラス
class CsvOperator:
    output_encoding = 'cp932'   # cp932 or utf8
    output_format = 'csv'       # CSV or TSV

    def input(self, path, fname):
        # フルパス生成
        file_path = os.path.join(path, fname)
        print('入力ファイル：' + file_path)
        # ファイル読込
        return self.read(file_path)

    def output(self, df, path, fname):
        # ディレクトリが存在しない場合は作成
        if os.path.exists(path) != True:
            os.mkdir(path)
        # フルパス生成
        file_path = os.path.join(path, fname)
        print('出力ファイル：' + file_path)
        # ファイル書込
        return self.write(df, file_path)

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

    def setOutputEncoding(self, encoding):
        self.output_encoding = encoding

    def setOutputFormat(self, format):
        self.output_format = format
