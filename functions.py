# -*- coding: utf-8 -*-
import my_module

# аннотация не язвляется обязательной и не проверяет типы
print('\nФункции')


def get(name: str = 'pav', age: int = 2) -> dict:
    """ строка комментариев"""
    return {'name': name, 'age': age}


# bool() возвращает True, если аргумент не пустой и False, если пустой или None

# val_1 = get('Pavel')
# val_2 = get('Tolya')
# print(val_1, val_2)

print(get(age=12, name='hop'))

# модули
print('\nМодули')

# 1. Для публикации своего модуля необходимо завести директорию с минимум
#   3-мя файлами README.txt setup.py и файлом
#       самого модуля
# from setuptools import setup
#
# setup(
#     name='my_module',
#     version='1.0',
#     description='The Head First Python Search Tools',
#     author='HF Python 2e',
#     author_email='hfpy2e@gmail.com',
#     url='headfirstlabs.com',
#     py_modules=['my_module'], тут указывать имя файла модуля
# )
#
# 2.Сборка дистрибутива пакета  -> python3 setup.py sdist <- в директории
#   пакета
# 3. Распаковка и установка
#   сформированного архива в как стороннего пакета интерпретатора
#       -> sudo python3 -m pip install <имя архива> <-

# установка фреймворка pytest для проверки кода на соответствие pep8

my_module.get1(123)
