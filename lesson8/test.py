import os
import hashlib
from flask import Flask, render_template, request
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
        # app.logger.debug('Auth=%s', 'OK' if is_auth == True else 'NG')
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
    # app.logger.debug('key=%s', key)
    # app.logger.debug('password=%s', password)
    account_list={
        'toshio.shiratori@gmail.com': hashlib.sha256('password'.encode('utf-8')).hexdigest()
    }
    if account_list.get(key) == hashlib.sha256(password.encode('utf-8')).hexdigest():
        # app.logger.debug('password=%s', account_list.get(key))
        return True
    return False 

if __name__ == '__main__':
    app.run(debug=True)
