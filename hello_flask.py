import html

from flask import Flask, render_template, request, redirect, escape
import my_module
import psycopg2

app = Flask(__name__)


# def log_request(req: 'flask_request', res: str) -> None:
#     with open('vsearch.log', 'a') as log:
#         print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

def log_request(req: 'flask_request', res: str) -> None:
    connect = psycopg2.connect(database='test', user='pavel',
                               password='11', host='localhost',
                               port="5432")
    cursor = connect.cursor()
    _Insert_SQL = """insert into log
                        (phrase, letters, ip, browser_sty, results, ts)
                        values
                        (%s, %s, %s, %s, %s, now())"""
    cursor.execute(_Insert_SQL, (req.form['phrase'],
                                 req.form['letters'],
                                 req.remote_addr,
                                 req.user_agent.browser,
                                 res,))
    connect.commit()
    cursor.close()
    connect.close()


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
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')

    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents, )


if __name__ == '__main__':
    app.run(debug=True)
