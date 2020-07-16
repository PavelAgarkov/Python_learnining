from flask import Flask, render_template, request, session, copy_current_request_context

from Classes.UseDatabase import UseDatabase, ConnectionErrors, CredentialsErrors, SQLErrors

import my_module

from checker import check_logged_id

from threading import Thread

app = Flask(__name__)
# добавление в конфиги приложения подключения к бд
app.config['pg_dbconfig'] = {'database': 'test',
                             'user': 'pavel',
                             'password': '11',
                             'host': 'localhost',
                             'port': '5432'
                             }

app.secret_key = 'YouWillNeverGuessMySecretKey'


# запись в файл
# def log_request(req: 'flask_request', res: str) -> None:
#     with open('vsearch.log', 'a') as log:
#         print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/my-module', methods=['POST'])
def my() -> str:

    # декоратор для сохранения сонтекста запроса flask при вызове потока
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        with UseDatabase(config=app.config['pg_dbconfig']) as cursor:
            _Insert_SQL = """insert into log
                                 (phrase, letters, ip, browser_sty, results, ts)
                                 values
                                 (%s, %s, %s, %s, %s, now())"""
            cursor.execute(_Insert_SQL, (req.form['phrase'],
                                         req.form['letters'],
                                         req.remote_addr,
                                         req.user_agent.browser,
                                         res,))

    title = 'Here'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = my_module.get1(phrase + letters)
    try:
        # инициализация потока, который вызовет log_request с параметрами args=(request, results)
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print("logging failed with this error", str(err))

    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='welcome')


@app.route('/viewlog')
@check_logged_id
def view_the_log() -> str:
    # чтение из файла
    # contents = []
    # with open('vsearch.log') as log:
    #     for line in log:
    #         contents.append([])
    #         split = line.split('|')
    #         for item in split:
    #             contents[-1].append(escape(item))
    try:
        with UseDatabase(app.config['pg_dbconfig']) as cursor:
            _SQL = """select * from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results', 'ts')

        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents, )
    except ConnectionErrors as err:
        print('Is your database switched on? Error:', str(err))
    except CredentialsErrors as err:
        print('User-id/Password issues. Error:', str(err))
    except SQLErrors(Exception) as err:
        print('Is your query correct? Error:', str(err))
    return 'Error'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You logged in'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'you delete'


if __name__ == '__main__':
    app.run(debug=True)

# стр 444
