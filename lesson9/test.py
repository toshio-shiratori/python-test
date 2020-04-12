import tkinter

# ウインドウの作成
root = tkinter.Tk()
root.title(u"lesson 9-1.")
root.geometry("640x480")

# 入出力エリア
label = tkinter.Label(text='Hello World.')
label.grid()

if __name__ == '__main__':
    # ウインドウの描画
    root.mainloop()
