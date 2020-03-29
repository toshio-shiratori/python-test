import os
import sqlite3
import hashlib

def run(dbname):
    # 実行ファイルのカレントパスを取得
    current_path = os.path.dirname(__file__)
    
    # TEST.dbを作成する
    # すでに存在していれば、それにアスセスする。
    db_path = os.path.join(current_path, dbname)
    print('DB-Path: {}'.format(db_path))
    conn = sqlite3.connect(db_path)

    # テーブル作成
    create_users_table(conn, new=True)

    # 初期データ投入
    user_info={
        'name': 'shira',
        'email': 'toshio.shiratori@gmail.com',
        'password': 'password'
    }
    insert_user(conn, user_info)

    # データベースへのコネクションを閉じる。(必須)
    conn.close()

def create_users_table(conn, new):
    # sqlite を操作するカーソルオブジェクトを作成
    cur = conn.cursor()

    # users テーブルの作成
    if new == True:
        # テーブルが存在した場合、削除して作り直し
        sql = '''
            DROP TABLE IF EXISTS users
        '''
        sql_execute(cur, sql)
        sql = '''
            CREATE TABLE users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name STRING,
                email STRING,
                password STRING
            )
        '''
    else:
        # テーブルが存在した場合、なにもしない
        sql = '''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name STRING,
                email STRING,
                password STRING
            )
        '''
    sql_execute(cur, sql)

    # データベースへコミット。これで変更が反映される。
    conn.commit()

def insert_user(conn, info):
    # パスワードのハッシュ化
    password=hashlib.sha256(info['password'].encode('utf-8')).hexdigest()

    # sqlite を操作するカーソルオブジェクトを作成
    cur = conn.cursor()

    sql = '''
        INSERT INTO users(
            name,
            email,
            password
        ) VALUES (
            '{0}',
            '{1}',
            '{2}'
        )
    '''.format(info['name'], info['email'], password)
    sql_execute(cur, sql)

    # データベースへコミット。これで変更が反映される。
    conn.commit()

def sql_execute(cur, sql):
    # print(sql)
    cur.execute(sql)

if __name__ == '__main__':
    run('TEST.db')
