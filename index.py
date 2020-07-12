# -*- coding: utf-8 -*-

# Работа со списком
nums = [1, 2, 3, 4]
# удаление последнего
nums.pop()
# удаление по ключу
nums.pop(1)
# вставка в конец списка другого список
nums.extend([3, 4])
# вставка в конец пустого списка
nums.append([])
# вставка перед ключом нового элемента
nums.insert(1, 'hi')

# пример операций со списком
phrase = "Don't panic!"
plist = list(phrase)
# print(phrase)
# print(plist)
# for i in range(4):
#     plist.pop()
# plist.pop(0)
# plist.remove("'")
# plist.extend([plist.pop(), plist.pop()])
# plist.insert(2, plist.pop(3))
# new_phrase = ''.join(plist)
# print(plist)
# print(new_phrase)

# Копирование объектов
first = [1, 2, 3, 4, 5]
# по умолчанию переменные присваиваются по ссылке, можно изменить это поведение
second = first.copy()
second.append(6)
first.pop()
# print(first, second)

# доступ к элеменут по индексу
print('\nДействия c индексами списка')
print(phrase, phrase[0], phrase[-1])

# нотация letters[start:stop:step]
# Срезы, при указании  stop индекс не входит в дмапазон, а исключается
print('\nДействия со срезами')
print(phrase, phrase[0:10:3])
print(phrase, phrase[3:])
print(phrase, phrase[:10])
print(phrase, phrase[::2])
print(phrase, phrase[-6:])

# шаг диапазона в списке
print('\nШаг диапазона в списке')
print(''.join(phrase[::-1]))
print(''.join(phrase[::-2]))
print(''.join(phrase[::2]))
print(''.join(phrase[::1]))

print('\nПолучения из среза')
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])
print(phrase, new_phrase)

# словарь
print('\nСловари')
hash = {
    'a': 1,
    'b': 2
}

for k in hash:
    # k - ключ, hash[k] - значение
    print(hash[k])

for key, value in sorted(hash.items()):
    print(key, value)

print('\nДинамическое добавление в словарь значения')
# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input("Provide a word to search for vowels: ")
# word_in_list = list(word)

# insides = {}

# for k in word_in_list:
#     if k in vowels:
#         #динамическое добавление в словарь значения
#         insides.setdefault(k, 0)
#         insides[k] = insides[k] + 1
# print(insides)

# if len(insides) == 0 :
#     print('Ничего не найдено')
# else :
#     print(insides)

print('\nМножества')

vowels = {'a', 'e', 'i', 'o', 'u'}
word = {'h', 'e', 'l', 'l', 'o'}

u = vowels.union(word)
diff = vowels.difference(word)
intersect = vowels.intersection(word)
sorted_list = sorted(list(diff))
print(u, diff, sorted_list, intersect)

# Кортежи
print('\nКортежи')

tuple_1 = ('a', 'e', 'i', 'o', 'u')
one_string = ('One')
tuple_2 = ('One',)
print(one_string, tuple_2)

# словарь словарей
dictionary = {'a': {'b': 1, 'c': 'hi'}}
print(dictionary['a']['b'])
