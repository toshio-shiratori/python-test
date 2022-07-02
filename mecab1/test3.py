import MeCab
tokenizer = MeCab.Tagger('-d /var/lib/mecab/dic/mecab-ipadic-neologd')

sentence = '朝顔が綺麗ですね'
node = tokenizer.parseToNode(sentence)
while node:
    # 名詞のみ表示
    if 36 <= node.posid <=67:
        print('-----形態素の文字列情報')
        print(node.surface)
        print('-----CSVで表記された素性情報')
        print(node.feature)
        items = node.feature.split(',')
        items_dic = [
            '品詞',
            '品詞細分類1',
            '品詞細分類2',
            '品詞細分類3',
            '活用型',
            '活用形',
            '基本形',
            '読み',
            '発音',
        ]
        for index in range(0, len(items)):
            print('  %d:[%s] %s' % (index, items_dic[index], items[index]))
    node = node.next
