import os
from lib.db_helper import DbHelper
from lib.sqlite3_helper import Sqlite3Helper

def run(params):
    # sqlite3 ヘルパークラスを生成
    db_helper = Sqlite3Helper(params['debug'])

    try:
        # DB 接続
        db_helper.connect(params['dbname'])

        replace=False
        # テーブルを再作成するか？
        if params['cmd'] == DbHelper.CMD_INIT_DB:
            replace=True
            print('DB の初期化を行います。')

        # テーブル作成
        table, fields = getCreateTableParamsByUsers()
        db_helper.create_table(table, fields, replace)

        # アカウントのデータ挿入
        if params['cmd'] == DbHelper.CMD_ADD_USER:
            sql=getInsertSqlByUsers(
                params['email'],
                params['password'],
                params['name']
            )
            db_helper.inner_insert_record(sql)

        # アカウントのパスワード変更
        if params['cmd'] == DbHelper.CMD_CHANGE_PASSWORD:
            sql=getUpdatePasswordSqlByUsers(
                params['email'],
                params['password']
            )
            db_helper.inner_update_record(sql)

        # DB コミット
        db_helper.commit()

        # アカウント一覧の表示
        if params['cmd'] == DbHelper.CMD_SHOW_USER:
            sql='''
                SELECT id, name, email FROM users
            '''
            rows=db_helper.inner_select_records(sql)
            print('{}\t{}\t{}'.format('id', 'name', 'email'))
            print('{}\t{}\t{}'.format('------', '------', '---------------------'))
            for row in rows:
                for item in row:
                    print('{}\t'.format(item), end='')
                print()

        # アカウントの認証
        if params['cmd'] == DbHelper.CMD_AUTH:
            auth={
                'email': params.get('email'),
                'password': DbHelper.getHashPassword(params.get('password'))
            }
            sql='''
                SELECT count(1)
                FROM users
                WHERE email = '{email}'
                AND password = '{password}'
            '''.format(**auth)
            # print(sql)
            row=db_helper.inner_select_record(sql)
            result='認証 NG'
            if row[0] == 1:
                result='認証 OK'
            print(result)

        # DB クローズ
        db_helper.disconnect()

    except Exception as e:
        print('Error!! : ', e)

def getCreateTableParamsByUsers():
    table='users'
    fields='''
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name STRING,
        email STRING UNIQUE,
        password STRING
    '''
    return table, fields

def getInsertSqlByUsers(email, password, name='guest'):
    dict={
        'name': name,
        'email': email,
        'password': DbHelper.getHashPassword(password)
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

def getUpdatePasswordSqlByUsers(email, password):
    dict={
        'email': email,
        'password': DbHelper.getHashPassword(password)
    }
    sql = '''
        UPDATE users SET password = '{password}'
        WHERE email = '{email}'
    '''.format(**dict)
    return sql

if __name__ == '__main__':
    # 実行ファイルのカレントパスを取得
    current_path = os.path.dirname(__file__)
    # DB パスを生成
    db_path = os.path.join(current_path, 'TEST.db')
    # パラメータ取得
    params=DbHelper.generateParams()
    params['dbname']=db_path
    params['debug']=False
    # メイン処理の実行
    # print('パラメータ：', params)
    run(params)
