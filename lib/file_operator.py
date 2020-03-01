import os
import sys
from abc import ABCMeta, abstractmethod

# 抽象ファイル操作クラス
class FileOperator(metaclass=ABCMeta):
    def __init__(self):
        self.input_encoding = 'utf8'    # utf8 or cp932
        self.input_format = 'text'      # text only
        self.output_encoding = 'utf8'   # utf8 or cp932
        self.output_format = 'text'     # text only

    def input(self, path, fname):
        # フルパス生成
        file_path = os.path.join(path, fname)
        print('入力ファイル名：' + file_path)
        # ファイル読込
        return self.read(file_path)

    def output(self, df, path, fname):
        # ディレクトリが存在しない場合は作成
        if os.path.exists(path) != True:
            os.mkdir(path)
        # フルパス生成
        file_path = os.path.join(path, fname)
        print('出力ファイル名：' + file_path)
        # ファイル書込
        return self.write(df, file_path)

    @abstractmethod
    def read(self, file_path):
        raise NotImplementedError()

    @abstractmethod
    def write(self, df, file_path):
        raise NotImplementedError()

    @abstractmethod
    def getOutputFileName(self):
        raise NotImplementedError()

    def setOutputEncoding(self, encoding):
        self.output_encoding = encoding

    def setOutputFormat(self, format):
        self.output_format = format

    def generateParams(self, current_path):
        # コマンド引数からパラメータ取得
        args = sys.argv
        if len(args) <= 1:
            print('入力ファイル名の指定は必須です。')
            sys.exit()
        input_fname = args[1]
        if len(args) >= 3:
            self.output_encoding = args[2]
        if len(args) >= 4:
            self.output_format = args[3]

        # パラメータ生成
        params = {
            'input': {
                'path': os.path.join(current_path, 'input'),
                'fname': input_fname
            },
            'output': {
                'path': os.path.join(current_path, 'output'),
                'fname': self.getOutputFileName(),
                'encoding': self.output_encoding,
                'format': self.output_format
            }
        }
        return params
