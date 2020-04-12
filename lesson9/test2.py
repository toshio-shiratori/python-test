import tkinter

def pushed(label):
    label['text'] = 'ボタンが押されました。'

# ウインドウの作成
root = tkinter.Tk()
root.title(u'lesson 9-1.')
root.geometry('640x480')

# 入出力エリア
label = tkinter.Label(root, text=u'Hello World.')
label.grid()

#ボタンを作る
button = tkinter.Button(root, text=u'ボタン', command= lambda : pushed(label))
button.grid()

if __name__ == '__main__':
    # ウインドウの描画
    root.mainloop()
