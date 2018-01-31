#!/usr/bin/python3

# Упражнение 6 
# Задание 1

# Заполнить список из шести элементов произвольными целочисленными значениями.
# Вывести список на экран.


import re

string = input('Введи шесть целочисленных значений через пробел: ')
try:
    strings = string.split(' ')
    numbers = []
    if len(strings) != 6: raise ValueError('The number of arguments is not equal to six!')
    for i in range(6):
        if not bool(re.match('(\-?[1-9][0-9]*)|0$',strings[i])): raise ValueError('The argument is not a number!')
        numbers.append(int(strings[i]))
except (TypeError, ValueError):
    print('Дружище, похоже ты ввел какую-то хуйню, а не шесть целочисленных значений через пробел!')
    exit()
print('Введенный список: [' + ', '.join(map(str, numbers)) + ']')
