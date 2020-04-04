import os
import hashlib
from flask import Flask, render_template, request
from lib.sqlite3_helper import Sqlite3Helper

app = Flask(__name__)

@app.context_processor
def add_staticfile():
    def staticfile_cp(fname):
        path = os.path.join(app.root_path, 'static', fname)
        mtime =  str(int(os.stat(path).st_mtime))
        return '/static/' + fname + '?v=' + str(mtime)
    return dict(staticfile=staticfile_cp)

@app.route('/')
def index():
    return render_template('index.html', title='トップページ')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email=request.form["email"]
        password=request.form["password"]
        is_auth=auth(email, password)
        return render_template(
            'login.html', 
            title='ログインページ',
            message='認証に{}'.format('成功しました' if is_auth == True else '失敗しました')
        )
    else:
        return render_template(
            'login.html',
            title='ログインページ',
            message=''
        )

def auth(key, password):
    # 実行ファイルのカレントパスを取得
    current_path = os.path.dirname(__file__)
    # DB パスを生成
    db_path = os.path.join(current_path, 'TEST.db')
    
    # sqlite3 ヘルパークラスを生成
    db_helper = Sqlite3Helper()
    try:
        # DB 接続
        db_helper.connect(db_path)

        auth={
            'email': key,
            'password': Sqlite3Helper.getHashPassword(password)
        }
        sql='''
            SELECT count(1)
            FROM users
            WHERE email = '{email}'
            AND password = '{password}'
        '''.format(**auth)
        # print(sql)
        row=db_helper.inner_select_record(sql)
        if row[0] == 1:
            return True
        return False 

    except Exception as e:
        print('Error!! : ', e)

if __name__ == '__main__':
    app.run(debug=True)
