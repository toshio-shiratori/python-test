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

@app.route('/account', methods=['GET'])
def accounts():
    items=get_accounts()
    return render_template(
        'list.html', 
        title='アカウントの一覧ページ',
        items=items
    )

@app.route('/account/regist', methods=['GET', 'POST'])
def regist():
    if request.method == "POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        is_regist=regist_account(email, password, name)
        return render_template(
            'regist.html', 
            title='登録ページ',
            message='登録に{}'.format('成功しました' if is_regist == True else '失敗しました')
        )
    else:
        return render_template(
            'regist.html', 
            title='登録ページ',
            message=''
        )

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

def get_accounts():
    # sqlite3 ヘルパークラスを生成
    db_helper = Sqlite3Helper()
    try:
        # DB 接続
        db_helper.connect(get_dbname())

        # アカウント一覧の取得
        sql='''
            SELECT id, name, email FROM users
        '''
        rows=db_helper.inner_select_records(sql)
        items=[]
        for row in rows:
            item={
                'id': row[0],
                'name': row[1],
                'email': row[2],
            }
            items.append(item)
        return items

    except Exception as e:
        print('Error!! : ', e)
        return []

def auth(key, password):
    # sqlite3 ヘルパークラスを生成
    db_helper = Sqlite3Helper()
    try:
        # DB 接続
        db_helper.connect(get_dbname())

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
        return False 

def regist_account(email, password, name='guest'):
    # sqlite3 ヘルパークラスを生成
    db_helper = Sqlite3Helper()
    try:
        # DB 接続
        db_helper.connect(get_dbname())

        # アカウントのデータ挿入
        sql=getInsertSqlByUsers(
            email,
            password,
            name
        )
        db_helper.inner_insert_record(sql)

        # DB コミット
        db_helper.commit()

        return True

    except Exception as e:
        print('Error!! : ', e)
        return False 

def get_dbname():
    # 実行ファイルのカレントパスを取得
    current_path = os.path.dirname(__file__)
    # DB パスを生成して返す
    return os.path.join(current_path, 'TEST.db')

def getInsertSqlByUsers(email, password, name):
    dict={
        'name': name,
        'email': email,
        'password': Sqlite3Helper.getHashPassword(password)
    }
    sql = '''
        INSERT INTO users(
            name,
            email,
            password
        ) VALUES (
            '{name}',
            '{email}',
            '{password}'
        )
    '''.format(**dict)
    return sql

if __name__ == '__main__':
    app.run(debug=True)
