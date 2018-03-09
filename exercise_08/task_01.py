#!/usr/bin/python3

# Упражнение 8
# Задание 1.2

# Создайте двумерный массив 10х10 из случайных чисел. Ввод размера массива сделать с клавиатуры.
# Вычислить максимальный элемент в каждой строке массива и вывести полученный список на экран.


import functions

str = input('Введи размерность двумерного массива (два числа) через пробел: ')
mn = str.split(' ')
m = functions.check_and_get_int(mn[0])
n = functions.check_and_get_int(mn[1])
if not m['is_int'] or not n['is_int']:
    print('Ты ввел что-то не то!')
    exit()
a = functions.get_two_dimensional_array(m['value'], n['value'])
maximums = functions.get_maximums_of_two_dimensional_array(a)
print(maximums)
