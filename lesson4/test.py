import os
import sys # sys.exit() で処理を終わらすのに使用する
from lib import excel_operator

def main():
    # 実行ファイルのカレントパスを取得
    current_path = os.path.dirname(__file__)

    # CSV 操作クラスを生成
    excel = excel_operator.ExcelOperator()

    # 入力先パスを生成
    input_path = os.path.join(current_path, 'input')

    # ファイル入力
    df = excel.input(input_path, 'sample.xlsx')

    # 出力先パスを生成
    output_path = os.path.join(current_path, 'output')

    # ファイル出力
    excel.output(df, output_path, 'sample.xlsx')

if __name__ == '__main__':
    main()
