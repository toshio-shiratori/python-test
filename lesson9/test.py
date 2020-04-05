import tkinter

# ウインドウの作成
root = tkinter.Tk()
root.title(u"lesson 9-1.")
root.geometry("360x120")

# 入出力エリア
label = tkinter.Label(text='Hello World.')
label.place(x=10, y=10)

if __name__ == '__main__':
    # ウインドウの描画
    root.mainloop()
