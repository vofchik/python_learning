#!/usr/bin/python3

# Упражнение 8
# Задание 3

# Дано натуральное число N. Выведите все его цифры по одной, в обратном порядке, разделяя их пробелами или новыми
# строками. При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется).


import functions

str = input('Введи натуральное число: ')
n = functions.check_and_get_int(str)
if not n['is_int']:
    print('Ты ввел что-то не то!')
    exit()
def print_and_dec(value: int):
    if value <= 9:
        print('{:d}'.format(value))
    else:
        digit = value % 10
        print('{:d} '.format(digit), end='')
        print_and_dec(value // 10)
print_and_dec(n['value'])
