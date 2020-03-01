import os
import sys
from lib import csv_operator

def main(input_fname, output_encoding):
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

    # 出力ファイルのエンコード設定
    csv.setOutputEncoding(output_encoding)

    # ファイル出力
    csv.output(df, output_path, 'sample.csv')

if __name__ == '__main__':
    args = sys.argv
    input_fname = args[1]
    output_encoding = 'cp932'
    if len(args) >= 3:
        output_encoding = args[2]
    main(input_fname, output_encoding)
