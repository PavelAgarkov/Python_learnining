"""Декоратор для аутентификации"""
from flask import session
from functools import wraps


def check_logged_id(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # код до декорируемой функции
        if 'logged_in' in session:
            # вызов декорируемой функции
            return func(*args, **kwargs)
        # код вместо вызова декорируемой функции
        return 'You are NOT logged in.'
    # возврат обертки над декорируемой функцией
    return wrapper
