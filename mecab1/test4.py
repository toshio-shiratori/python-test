import MeCab
tokenizer = MeCab.Tagger('-d /var/lib/mecab/dic/mecab-ipadic-neologd')
# tokenizer = MeCab.Tagger()

sentence = '今日はクレアンスメアードの庭に咲く朝顔が綺麗ですね'
# sentence = 'カレー'
node = tokenizer.parseToNode(sentence)
index = 1
while node:
    # 名詞のみ表示
    if 36 <= node.posid <=67:
        print('----- No.%02d -----' % index)
        print('単語: %s' % node.surface)
        print('種別ID: %d' % node.posid)
        items = node.feature.split(',')
        # print('  %s' % node.feature)
        # print('  %d' % len(items))
        # items_dic = [
        #     '品詞',
        #     '品詞細分類1',
        #     '品詞細分類2',
        #     '品詞細分類3',
        #     '活用型',
        #     '活用形',
        #     '基本形',
        #     '読み',
        #     '発音',
        # ]
        print('品詞: %s' % items[0])
        print('分類1: %s' % items[1])
        print('分類2: %s' % items[2])
        if len(items) > 7:
            print('読み: %s' % items[7])
        else:
            print('読み: *')
        index = index + 1
    node = node.next
