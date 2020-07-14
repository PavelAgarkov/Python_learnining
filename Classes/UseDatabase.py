import psycopg2

"""Класс протокола управления контекста для инициализации объекта запроса(курсора)"""


class UseDatabase:
    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.connection = psycopg2.connect(**self.configuration)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
