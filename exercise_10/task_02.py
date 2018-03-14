#!/usr/bin/python3

# Упражнение 10
# Задание 2

# Даны обозначения двух полей шахматной доски (например, A5 и C2). Найти минимальное число ходов, которые нужны
# шахматному коню для перехода с первого поля на второе.


import re

str = input('Введи два шахматных поля через пробел (например, \'A5 C2\'): ')
if not bool(re.match('[A-H]{1}[1-8]{1}\ [A-H]{1}[1-8]{1}$', str)):
    print('Ты ввел что-то не то!')
    exit()
str1, str2 = str.split(' ')
i1 = ord(str1[0]) - 65
j1 = int(str1[1]) - 1
i2 = ord(str2[0]) - 65
j2 = int(str2[1]) - 1

a = [[-1] * 8 for i in range(8)]
a[i1][j1] = 0
moves = [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]

def make_next_step(step:int, i:int, j:int):
    ''' Рекурсивно строит матрицу ходов коня из заданной точки'''
    global a
    step += 1
    for m in range(8):
        im = i + moves[m][0]
        jm = j + moves[m][1]
        if 0 <= im <= 7 and 0 <= jm <= 7:
            if a[im][jm] == -1 or a[im][jm] > step:
                a[im][jm] = step
                if step < 6:
                    make_next_step(step, im, jm)
make_next_step(0, i1, j1)
print('Минимальное число ходов: {:d}'.format(a[i2][j2]))
