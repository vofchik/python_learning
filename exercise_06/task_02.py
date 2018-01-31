#!/usr/bin/python3

# Упражнение 6 
# Задание 2

# Заполнить список из четырёх элементов введёными строковыми значениями.
# Вывести список на экран.


import re

print('Введи четыре строки: ')
strings = []
for i in range(4):
   str = input()
   strings.append(str)
print('Введенный список: [\'' + '\', \''.join(strings) + '\']')

