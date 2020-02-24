import os

def csv_output():
    path = os.path.dirname(__file__)
    f = open(path + '/sample_utf8.csv')
    # 一行ずつ読み込んで配列に格納する
    rows = []
    for line in f.read().splitlines():
        rows.append(line)

    for line in rows:
        print(line)

csv_output()
