import os
import sys
from lib.csv_operator import CsvOperator

def main(params):
    # CSV 操作クラスを生成
    csv = CsvOperator()
    # ファイル入力
    df = csv.input(params['input']['path'], params['input']['fname'])
    # 出力ファイルのオプション指定
    csv.setOutputEncoding(params['output']['encoding'])
    csv.setOutputFormat(params['output']['format'])
    # ファイル出力
    csv.output(df, params['output']['path'], params['output']['fname'])

def generateParams():
    # 実行ファイルのカレントパスを取得
    current_path = os.path.dirname(__file__)

    # デフォルトパラメータ
    output_encoding = 'cp932'
    output_format = 'csv'

    # コマンド引数からパラメータ取得
    args = sys.argv
    input_fname = args[1]
    if len(args) >= 3:
        output_encoding = args[2]
    if len(args) >= 4:
        output_format = args[3]

    # パラメータ生成
    params = {
        'input': {
            'path': os.path.join(current_path, 'input'),
            'fname': input_fname
        },
        'output': {
            'path': os.path.join(current_path, 'output'),
            'fname': 'sample.csv',
            'encoding': output_encoding,
            'format': output_format
        }
    }
    return params

if __name__ == '__main__':
    params = generateParams()
    main(params)
