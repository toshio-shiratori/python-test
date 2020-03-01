import os
import pandas as pd
from lib.file_operator import FileOperator

# Excel 操作クラス
class ExcelOperator(FileOperator):
    def __init__(self):
        super().__init__()
        self.input_format = 'excel'     # excel only
        self.output_format = 'excel'    # excel only

    def getOutputFileName(self):
        return 'sample.xlsx'

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
            index = False,  # インデックスを出力しない
        )
