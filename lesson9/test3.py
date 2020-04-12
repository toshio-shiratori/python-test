import tkinter
from tkinter import ttk

class AccountApp(ttk.Frame):
    '''アカウント管理アプリ'''

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        '''ウィジェットの作成、配置'''
        # 1 列目
        ttk.Button(self, text='アカウント一覧').grid(column=0, row=0)
        # 2 列目
        ttk.Button(self, text='アカウント登録').grid(column=0, row=1)
        # 3 列目
        ttk.Button(self, text='ログイン').grid(column=0, row=2)
        # Frame自身もトップレベルウィジェットに配置
        self.grid(column=0, row=0)

        # 各列の引き伸ばし設定
        self.columnconfigure(0, weight=1)
        # 各行の引き伸ばし設定
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        # トップレベルのウィジェットも引き伸ばしに対応させる
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

def main():
    root = tkinter.Tk()
    root.title('トップページ')
    root.geometry('640x480')
    AccountApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
