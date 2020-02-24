def helloworld():
    f = open('data2.txt')
    # 一行ずつ読み込んで表示する
    for name in f.read().splitlines():
        message = 'Hello ' + name + ' !'
        print(message)

helloworld()
