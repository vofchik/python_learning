#!/usr/bin/python3

# Упражнение 9
# Задание 6

# Программа должна подсчитать количество строк, слов и букв в переданном ей файле.
#
# Имя файла должно передаваться в качестве первого аргумента после имени самого скрипта. Например, вызов скрипта в Linux
# через командную оболочку выглядит примерно так:
#
# python3 words.py text.txt


import sys
from typing import List
import string

def replace_delimiters(x: string) -> string:
    '''Заменяет небуквы и не цифры точками'''
    return x if x.isalnum() else '.'

def remove_empty(x: List) -> bool:
    '''Удаляет пустые элементы списка'''
    return False if x == '' else True

if len(sys.argv) != 2:
    print('Incorrect number of arguments!')
    print('Example: python3 task_06.py text.txt')
    exit()

try:
    file = open(sys.argv[1])
except:
    print('File open error!')
    exit()
strings_count = words_count = letters_count = 0
for str in file:
    strings_count += 1
    str = ''.join(list(map(replace_delimiters, str)))
    words = str.split('.')
    words = list(filter(remove_empty, words))
    words_count += len(words)
    str = str.replace('.','')
    letters_count += len(str)

file.close()
print('Результат анализа файла \'{}\':'.format(sys.argv[1]))
print('строк: {:d}: '.format(strings_count))
print('слов: {:d}: '.format(words_count))
print('букв: {:d}: '.format(letters_count))

