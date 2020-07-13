import psycopg2

# селект запрос
connect = psycopg2.connect(database='test', user='pavel',
                           password='11', host='localhost',
                           port="5432")
cursor = connect.cursor()
_SQL = """select table_name, column_name
            from information_schema.columns
            where table_schema='public' and table_name='log'"""
cursor.execute(_SQL)
rows = cursor.fetchall()
cursor.close()
connect.close()
print(rows)

# инсерт запрос
connect = psycopg2.connect(database='test', user='pavel',
                           password='11', host='localhost',
                           port="5432")
cursor = connect.cursor()
_Insert_SQL = """insert into log
                    (phrase, letters, ip, browser_sty, results, ts)
                    values
                    (%s, %s, %s, %s, %s, now())"""
cursor.execute(_Insert_SQL, ('galaxy', 'xyz', '127.0.0.1', 'Opera', '{"x", "y"}'))
# обязательно утверждать коммитом, т.к. по умолчанию открывается транзакция
connect.commit()
cursor.close()
connect.close()