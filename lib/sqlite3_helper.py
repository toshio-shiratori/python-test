from lib.db_helper import DbHelper
import sqlite3

# sqlite3 ヘルパークラス
class Sqlite3Helper(DbHelper):
    def __init__(self, debug=False):
        super().__init__(debug)
        self.conn=None

    def inner_connect(self, connect_info):
        # DB を作成する
        # すでに存在していれば、それにアスセスする。
        db_path=connect_info['db_name']
        self.conn=sqlite3.connect(db_path)

    def inner_disconnect(self):
        self.conn.close()

    def inner_create_table(self, table, fields, replace):
        # sqlite を操作するカーソルオブジェクトを作成
        cur=self.conn.cursor()
        # パラメータ生成
        dict={
            'table': table,
            'fields': fields
        }
        # テーブルの作成
        if replace == True:
            # テーブルが存在した場合、削除して作り直し
            sql = '''
                DROP TABLE IF EXISTS {table}
            '''.format(**dict)
            self.sql_execute(cur, sql)
            sql = '''
                CREATE TABLE {table}(
                    {fields}
                )
            '''.format(**dict)
        else:
            # テーブルが存在した場合、なにもしない SQL です
            sql = '''
                CREATE TABLE IF NOT EXISTS {table}(
                    {fields}
                )
            '''.format(**dict)
        self.sql_execute(cur, sql)

    def inner_insert_record(self, sql):
        # sqlite を操作するカーソルオブジェクトを作成
        cur=self.conn.cursor()
        self.sql_execute(cur, sql)

    def inner_update_record(self, sql):
        # sqlite を操作するカーソルオブジェクトを作成
        cur=self.conn.cursor()
        self.sql_execute(cur, sql)

    def inner_select_record(self, sql):
        # sqlite を操作するカーソルオブジェクトを作成
        cur=self.conn.cursor()
        # print(sql)
        cur.execute(sql)
        return cur.fetchone()

    def inner_select_records(self, sql):
        # sqlite を操作するカーソルオブジェクトを作成
        cur=self.conn.cursor()
        # print(sql)
        cur.execute(sql)
        return cur.fetchall()

    def inner_commit(self):
        self.conn.commit()

    def inner_rollback(self):
        self.conn.rollback()

    def sql_execute(self, cur, sql):
        # print(sql)
        cur.execute(sql)
