#!/usr/bin/python3

# Упражнение 6 
# Задание 7

# Заполнить список из десяти элементов произвольными целочисленными значениями
# (без использования цикла). Удалить те элементы, значения которых не кратны 3.


import random
import re

string = input('Введи десять целочисленных значений через пробел: ')
if not bool(re.match('(((\-?[1-9][0-9]*)|0)\ ){9,9}(((\-?[1-9][0-9]*)|0))$',string)):
    print('Дружище, похоже ты ввел какую-то хуйню, а не десять целочисленных значений через пробел!')
    exit()
numbers = list(map(int, string.split(' ')))
print('Извини, ты зря вводил. Злой Саша сказал использовать генератор случайных чисел.')
def randint(x): return random.randint(0, 1000)
numbers = list(map(randint, [0] * 10))
def check(x): return x % 3 == 0
print('Cписок: [' + ', '.join(map(str, numbers)) + ']')
numbers = list(filter(check, numbers))
if len(numbers) == 0:
    print('Элементов кратных трем нет')
else:
    print('Элементы кратные трем: [' + ', '.join(map(str, numbers)) + ']')


