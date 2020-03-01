import os
import sys # sys.exit() で処理を終わらすのに使用する
from lib import csv_manager

def main():
    # 実行ファイルのカレントパスを取得
    current_path = os.path.dirname(__file__)

    # CSV 操作クラスを生成
    csv = csv_manager.CsvOperator()

    # 入力先パスを生成
    input_path = os.path.join(current_path, 'input')

    # ファイル入力
    df = csv.input(input_path, 'sample_utf8.csv')

    # 出力先パスを生成
    output_path = os.path.join(current_path, 'output')

    # ファイル出力
    csv.output(df, output_path, 'sample_sjis.csv')

if __name__ == '__main__':
    main()
