# запись в сессию (аутентификация)

from flask import Flask, session
from checker import check_logged_id

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuessMySecretKey'


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'


@app.route('/page1')
# применение декоратора для аутентификации
@check_logged_id
def page1() -> str:
    return 'This is page 1.'


@app.route('/page2')
@check_logged_id
def page2() -> str:
    return 'This is page 2.'


@app.route('/page3')
@check_logged_id
def page3() -> str:
    return 'This is page 3.'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You logged in'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'you delete'


# @app.route('/status')
# def status() -> str:
#     if 'logged_in' in session:
#         return 'you are logged'
#     return 'you are not logged'


if __name__ == '__main__':
    app.run(debug=True)

# 422 стр
