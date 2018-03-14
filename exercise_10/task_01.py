#!/usr/bin/python3

# Упражнение 10
# Задание 1

# Имеется N человек и прямоугольная таблица А[1:N,1:N];элемент A[i,j] равен 1, если человек i знаком с человеком j,
# А[i,j] = =А[j,i]. Можно ли разбить людей на 2 группы, чтобы в каждой группе были только незнакомые люди.


import random
import re

str = input('Введи два числа (количество человек и вероятность знакомства в %) через пробел : ')
if not bool(re.match('[1-9]{1}[0-9]*\ [1-9]{1}[0-9]?$', str)):
    print('Ты ввел что-то не то!')
    exit()
(n, p) = tuple(map(int, str.split(' ')))

a = [[1] * n for i in range(n)]
for i in range (n):
    for j in range (i + 1, n):
        a[i][j] = 1 if random.randint(0,100) < p else 0
        a[j][i] = a[i][j]
print('Матрица знакомств:')
for i in range(n):
    print(a[i])
is_possible = True
# проверяем есть ли в строках больше 2-х единиц от диагонали
for i in range (0, n - 2):
    count = 0
    for j in range (i + 1, n):
        if a[i][j] == 1:
            count +=1
    if count >= 2:
        is_possible = False
# проверяем есть ли в столбцах больше 2-х единиц до диагонали
for j in range (2, n):
    count = 0
    for i in range (0, j):
        if a[i][j] == 1:
            count +=1
    if count >= 2:
        is_possible = False
print('Разбить людей на 2 группы ', end='')
if is_possible:
    print('можно')
else:
    print('нельзя')


