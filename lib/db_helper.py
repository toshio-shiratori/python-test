import os
import sys
import hashlib
from getpass import getpass
from abc import ABCMeta, abstractmethod

# 抽象 DB ヘルパークラス
class DbHelper(metaclass=ABCMeta):
    CMD_INIT_DB = 'init'
    CMD_ADD_USER = 'adduser'
    CMD_SHOW_USER = 'showuser'
    CMD_CHANGE_PASSWORD = 'chgpasswd'
    CMD_AUTH = 'auth'

    def __init__(self, debug=False):
        self.connect_info=None
        self.debug=debug

    def connect(self, dbname, dbuser=None, dbpwd=None, dbopt=None):
        self.connect_info={
            'db_name': dbname,
            'db_user': dbuser,
            'db_pwd': dbpwd,
            'db_opt': dbopt
        }
        if self.debug == True:
            print('DB 接続：', self.connect_info)
        return self.inner_connect(self.connect_info)

    def disconnect(self):
        if self.debug == True:
            print('DB 切断接続：', self.connect_info['db_name'])
        return self.inner_disconnect()

    def create_table(self, table, fields, replace=False):
        if self.debug == True:
            print('テーブル作成 ：', table)
            print('　再作成フラグ：', replace)
            print('　フィールド情報 ：', fields)
        return self.inner_create_table(table, fields, replace)

    def insert_record(self, sql):
        if self.debug == True:
            print('データ挿入 SQL：', sql)
        return self.inner_insert_record(sql)

    def update_record(self, sql):
        if self.debug == True:
            print('データ更新 SQL：', sql)
        return self.inner_update_record(sql)

    def select_records(self, sql):
        if self.debug == True:
            print('データ抽出 SQL：', sql)
        return self.inner_select_records(sql)

    def commit(self):
        if self.debug == True:
            print('コミット実行')
        return self.inner_commit()

    def rollback(self):
        if self.debug == True:
            print('ロールバック実行')
        return self.inner_rollback()

    @abstractmethod
    def inner_connect(self, connect_info):
        raise NotImplementedError()

    @abstractmethod
    def inner_disconnect(self):
        raise NotImplementedError()

    @abstractmethod
    def inner_create_table(self, table, fields, replace):
        raise NotImplementedError()

    @abstractmethod
    def inner_insert_record(self, sql):
        raise NotImplementedError()

    @abstractmethod
    def inner_update_record(self, sql):
        raise NotImplementedError()

    @abstractmethod
    def inner_select_record(self, sql):
        raise NotImplementedError()

    @abstractmethod
    def inner_select_records(self, sql):
        raise NotImplementedError()

    @abstractmethod
    def inner_commit(self):
        raise NotImplementedError()

    @abstractmethod
    def inner_rollback(self):
        raise NotImplementedError()

    @classmethod
    def getHashPassword(self, password):
        # パスワードをハッシュ化して返す
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    @classmethod
    def generateParams(self):
        # コマンド引数からパラメータを生成
        args=sys.argv
        if len(args) <= 1:
            # ヘルプ表示
            print('以下パラメータが指定できます。')
            print('\t{} : DB を初期化します。'.format(DbHelper.CMD_INIT_DB))
            print('\t{} : アカウントを追加します。'.format(DbHelper.CMD_ADD_USER))
            print('\t{} : アカウントの一覧を表示します。'.format(DbHelper.CMD_SHOW_USER))
            print('\t{} : アカウントのパスワードを変更します。'.format(DbHelper.CMD_CHANGE_PASSWORD))
            print('\t{} : アカウントの認証(メアド、パスワード)をします。'.format(DbHelper.CMD_AUTH))
            sys.exit()
        params={}
        if len(args) >= 2:
            params['cmd']=args[1]

        if params['cmd'] == DbHelper.CMD_ADD_USER:
            params['name']=input('ニックネーム：')
            params['email']=input('メールアドレス：')
            params['password']=getpass('パスワード：')

        if params['cmd'] == DbHelper.CMD_CHANGE_PASSWORD:
            params['email']=input('メールアドレス：')
            params['password']=getpass('パスワード：')

        if params['cmd'] == DbHelper.CMD_AUTH:
            params['email']=input('メールアドレス：')
            params['password']=getpass('パスワード：')

        return params
