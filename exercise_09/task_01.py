#!/usr/bin/python3

# Упражнение 9
# Задание 1

# Создать словарь из слов, которые введёт пользователь. Ключи - слова, значения - их порядок расположения в исходном
# тексте. Например, текст я понял, что эти так быстро проходят.



from typing import List
import string

def replace_delimiters(x: string) -> string:
    '''Заменяет небуквы и не цифры точками'''
    return x if x.isalnum() else '.'

def remove_empty(x: List) -> bool:
    '''Удаляет пустые элементы списка'''
    return False if x == '' else True

sentence = input('Введи предложение: ')
sentence = ''.join(list(map(replace_delimiters, sentence)))
words = sentence.split('.')
words = list(filter(remove_empty, words))
dic = {}
for i in range(0, len(words)):
    dic[words[i]] = i + 1
print(dic)