import os

def csv_output():
    path = os.path.dirname(__file__)
    # print('path: ' + path)
    f = open(path + '/sample_utf8.csv')
    # 一行ずつ読み込んで表示する
    for line in f.read().splitlines():
        print(line)

csv_output()
