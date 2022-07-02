from fastapi import FastAPI
import MeCab

app = FastAPI()


@app.get("/mecab/{sentence}")
def analysis_sentence(sentence: str):
    tokenizer = MeCab.Tagger('-d /var/lib/mecab/dic/mecab-ipadic-neologd')
    node = tokenizer.parseToNode(sentence)

    count = 0
    words = []
    while node:
        # 名詞のみ取得
        if 36 <= node.posid <=67:
            count = count + 1
            items = node.feature.split(',')
            if len(items) > 7:
                kana = items[7]
            else:
                kana = '*'
            words.append({
                'name': node.surface,
                'kana': kana,
                'attribute': {
                    'id': node.posid,
                    'name': items[0],
                    'category1': items[1],
                    'category2': items[2]
                }
            })
        node = node.next
    print(words)
    result = words
    return {
        "sentence": sentence,
        "count": count,
        "words": words
    }
