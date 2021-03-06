# -*- coding: utf-8 -*-
import my_module
from csv_conversion import csv_dict_conversion

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


def apply(func: object) -> object:
    return func


def go(name):
    print(name)


closure = apply(go)
closure('all')

list1 = [1, 2, 3, 4, 5]


def list_func(*lis):
    for element in lis:
        print(element)


list_func(*list1)
list_func(4, 5, 6, 7, 8, 9)


def func_many_name_arguments(**args):
    for key, param in args.items():
        print(str(key) + '->' + str(param))


func_many_name_arguments(a=1, b='gh', c=list_func)

# try:
#     with open('my_file.txt') as fh:
#         file_data = fh.read()
#     print(file_data)
# except Exception as error:
#     # получение последнего исключения в текущем приложении
#     raise error
#     # err = sys.exc_info()
#     # for e in err:
#     #     print(e)
# a = 1;
# print(a)

csv_dict_conversion('file.csv')


# для изменяемых данных (структур: dict, list) переменная записывается по ссылке,
# в неизменяемые (обычные: str, int, bool)
b = [2]


def a(b):
    b[0] += 1


a(b)

print(b)
