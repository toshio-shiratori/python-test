import os
import pandas as pd
import csv

# CSV 操作クラス
class CsvOperator:
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
        # CSV ファイル出力
        df.to_csv(
            file_path,
            index = False,              # インデックスを出力しない
            encoding = 'cp932',         # 文字コードを SJIS にする
            quoting = csv.QUOTE_ALL,    # すべてをタブルクオートさせて出力
        )
