from flask import Flask, render_template, request
from Classes.UseDatabase import UseDatabase
import my_module

app = Flask(__name__)
# добавление в конфиги приложения подключения к бд
app.config['pg_dbconfig'] = {'database': 'test',
                             'user': 'pavel',
                             'password': '11',
                             'host': 'localhost',
                             'port': '5432'
                             }


# запись в файл
# def log_request(req: 'flask_request', res: str) -> None:
#     with open('vsearch.log', 'a') as log:
#         print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

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


@app.route('/my-module', methods=['POST'])
def my() -> str:
    title = 'Here'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = my_module.get1(phrase + letters)
    log_request(request, results)
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
def view_the_log() -> str:
    # чтение из файла
    # contents = []
    # with open('vsearch.log') as log:
    #     for line in log:
    #         contents.append([])
    #         split = line.split('|')
    #         for item in split:
    #             contents[-1].append(escape(item))
    with UseDatabase(app.config['pg_dbconfig']) as cursor:
        _SQL = """select * from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results', 'ts')

    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents, )


if __name__ == '__main__':
    app.run(debug=True)
