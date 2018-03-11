#!/usr/bin/python3

# Упражнение 9
# Задание 7

# Сделать задачу 3 по словарям с текстом из файла song.txt


from typing import List
import string
import sys

def replace_delimiters(x: string) -> string:
    '''Заменяет небуквы и не цифры точками'''
    return x if x.isalnum() else '.'

def remove_empty(x: List) -> bool:
    '''Удаляет пустые элементы списка'''
    return False if x == '' else True

if len(sys.argv) != 2:
    print('Incorrect number of arguments!')
    print('Example: python3 task_07.py text.txt')
    exit()

try:
    file = open(sys.argv[1])
except:
    print('File open error!')
    exit()
dic = {}
for str in file:
    sentence = ''.join(list(map(replace_delimiters, str)))
    words = sentence.split('.')
    words = list(filter(remove_empty, words))
    for word in words:
        dic[word] = dic.get(word, 0) + 1
file.close()
words_with_counts = []
for key, value in dic.items():
    words_with_counts.append((len(words) - value, key))
words_with_counts.sort()
for couple in words_with_counts:
    print(couple[1])
