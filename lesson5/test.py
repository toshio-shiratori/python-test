import os
import sys
from lib import csv_operator

def main(input_fname):
    # 実行ファイルのカレントパスを取得
    current_path = os.path.dirname(__file__)

    # CSV 操作クラスを生成
    csv = csv_operator.CsvOperator()

    # 入力先パスを生成
    input_path = os.path.join(current_path, 'input')

    # ファイル入力
    df = csv.input(input_path, input_fname)

    # 出力先パスを生成
    output_path = os.path.join(current_path, 'output')

    # ファイル出力
    csv.output(df, output_path, 'sample.csv')

if __name__ == '__main__':
    args = sys.argv
    print(args[0])  # lesson5/test.py
    print(args[1])  # sample_utf8.csv
    main(args[1])
