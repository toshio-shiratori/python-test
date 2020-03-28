from flask import Flask, escape
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page.'

@app.route('/user/<username>')
def show_username(username):
    return 'User: %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post: %d' % post_id

@app.route('/path/<path:subpath>')
def show_path(subpath):
    return 'SubPath: %s' % escape(subpath)

if __name__ == '__main__':
    app.run()
