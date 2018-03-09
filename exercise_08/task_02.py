#!/usr/bin/python3

# Упражнение 8
# Задание 2

# Дано натуральное число n. Выведите все числа от 1 до n. Без использования циклов.


import functions

str = input('Введи натуральное число: ')
n = functions.check_and_get_int(str)
if not n['is_int']:
    print('Ты ввел что-то не то!')
    exit()
def print_and_dec(value: int, max: int):
    if value == 1:
        print('{:d}'.format(max))
    else:
        value -= 1
        print('{:d} '.format(max - value), end='')
        print_and_dec(value, max)
print_and_dec(n['value'], n['value'])
