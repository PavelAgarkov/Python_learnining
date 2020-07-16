import psycopg2

"""Класс протокола управления контекста для инициализации объекта запроса(курсора)"""


class ConnectionErrors(Exception):
    pass


class CredentialsErrors(Exception):
    pass


class SQLErrors(Exception):
    pass


class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        try:
            self.connection = psycopg2.connect(**self.configuration)
            self.cursor = self.connection.cursor()
            return self.cursor
        except psycopg2.OperationalError as e:
            raise ConnectionErrors(e)
        except psycopg2.ProgrammingError as e:
            raise CredentialsErrors(e)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        if exc_type is psycopg2.ProgrammingError:
            raise SQLErrors(exc_val)
        elif exc_type:
            raise exc_type(exc_val)