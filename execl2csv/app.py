import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from lib.excel_operator import ExcelOperator
from lib.csv_operator import CsvOperator
import pandas as pd

class Excel2CsvApp(ttk.Frame):
    """Excel2Csvアプリ"""

    def __init__(self, master=None):
        super().__init__(master)

        # 変換データ
        self.df = None

        # Frame自身もトップレベルウィジェットに配置
        self.grid(row=0, column=0)

        # ウィンドウ自体の引き伸ばし設定
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # ウィジェットの作成
        self.create_widgets()

    def create_widgets(self):
        """ウィジェットの作成"""

        # 入力フレームの作成
        input_frame = ttk.Frame(self, padding=10)
        input_frame.grid(row=0)

        # 入力ウィジェットの作成
        self.create_input_widgets(input_frame)

        # 出力フレームの作成
        output_frame = ttk.Frame(self, padding=(0,5))
        output_frame.grid(row=1)

        # 出力ウィジェットの作成
        self.create_output_widgets(output_frame)

        # # 横の引き伸ばし設定
        # for col in range(4):
        #     self.columnconfigure(col, weight=1)

        # # 縦の引き伸ばし設定。
        # for row in range(3):
        #     self.rowconfigure(row, weight=0)

    def create_input_widgets(self, frame):
        """入力ウィジェットの作成"""
        # 参照ボタンの作成
        button1 = ttk.Button(frame, text=u'参照', command=lambda : self.button1_clicked(file1))
        button1.grid(row=0, column=3)

        # ラベルの作成
        # 「ファイル」ラベルの作成
        s = StringVar()
        s.set('ファイル>>')
        label1 = ttk.Label(frame, textvariable=s)
        label1.grid(row=0, column=0)

        # 参照ファイルパス表示ラベルの作成
        file1 = StringVar()
        file1_entry = ttk.Entry(frame, textvariable=file1, width=50)
        file1_entry.grid(row=0, column=2)

    def create_output_widgets(self, frame):
        """出力ウィジェットの作成"""
        # Startボタンの作成
        button2 = ttk.Button(frame, text='CSVファイル作成', command=lambda : self.button2_clicked())
        button2.grid(row=0, column=0)

        # Cancelボタンの作成
        button3 = ttk.Button(frame, text='終了', command=quit)
        button3.grid(row=1, column=0)

    # 参照ボタンのイベント
    # button1クリック時の処理
    def button1_clicked(self, file1):
        fTyp = [("","*")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        file1.set(filepath)

        if len(filepath) > 0:
            # ファイル操作クラスを生成
            __file = ExcelOperator()
            self.df = __file.direct_input(filepath)

    # button2クリック時の処理
    def button2_clicked(self):
        if self.df.empty:
            messagebox.showerror('エラー', u'Excel ファイルが選択されていません。')
            return

        df = self.df
        __file = CsvOperator()
        file2 = '/home/toshio/work/github/python-test/execl2csv/output/sample_sjis-line100.csv'
        __file.direct_output(df, file2)

        with open(file2, 'r') as f:
            lines = f.readlines()

        messagebox.showinfo('FileReference Tool', u'出力ファイルの内容は↓↓\n' + ''.join(lines))
        # print(df)

def main():
    root = Tk()
    root.title('ExcelをCSVに変換')
    root.geometry('640x800')
    Excel2CsvApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
