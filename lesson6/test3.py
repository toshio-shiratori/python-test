import os
import sys
from lib.excel_operator import ExcelOperator

def main(current_path):
    # ファイル操作クラスを生成
    __file = ExcelOperator()
    # コマンド引数からパラメータ生成
    params = __file.generateParams(current_path)
    # ファイル入力
    __df = __file.input(params['input']['path'], params['input']['fname'])
    # 出力ファイルのオプション指定
    # __file.setOutputEncoding(params['output']['encoding'])
    # __file.setOutputFormat(params['output']['format'])
    # ファイル出力
    __file.output(__df, params['output']['path'], params['output']['fname'])

if __name__ == '__main__':
    # 実行ファイルのカレントパスを取得
    current_path = os.path.dirname(__file__)
    main(current_path)
