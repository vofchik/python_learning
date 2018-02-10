#!/usr/bin/python3

# Упражнение 10
# Задание 6

# Пользователь вводит два целых числа x и y  > 1 (проверки на числа, целые, > 1).
# Нужно создать матрицу размером (x, y). Т.е. один список размером x, состоящий из списков размером y.
# Заполнить матрицу случайными числами в диапазоне от 0 до 1000.
# Найти номера столбцов, в которых содержатся числа в интервале от 90 до 100.


import re
import random

str = input('Введи два целых числа >1 через пробел: ')
if bool(re.match('^[1-9][0-9]*\ [1-9][0-9]*$', str)):
    x, y = map(int, str.split(' '))
    m = [[random.randint(0, 1000) for _ in range(y)] for _ in range(x)]
    exists = [0] * y
    print('Матрица:')
    for i in range(x):
        for j in range(y):
            print('{:4d}'.format(m[i][j]), end = ' ' if (j < y - 1) else '\n')
            if 90 <= m[i][j] <= 100:
                exists[j] = 1
    if 1 in exists:
        print('Номера столбцов:', end ='')
        for j in range(y):
            if exists[j]: print(' {:d}'.format(j + 1), end = '')
    else:
        print('Столбцов нет')
else:
    print('Дружище, похоже ты ввел какую-то хуйню, а не два целых числа >1 через пробел!')

