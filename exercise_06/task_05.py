#!/usr/bin/python3

# Упражнение 6
# Задание 5

# Заполнить список из десяти элементов произвольными целочисленными значениями.
# Получить список из элементов певрого списка, стоящих на четных местах.


import random

numbers = [random.randint(0, 1000) for i in range(10)]
print('Cписок: [' + ', '.join(map(str, numbers)) + ']')
numbers1 = [numbers[i] for i in range(1, 10, 2)]
print('Четные элементы через цикл: [' + ', '.join(map(str, numbers1)) + ']')
b = 1
def even(x):
    global b
    if b:
        b = 0
        return 0
    else:
        b = 1
        return 1
numbers2 = list(filter(even, numbers))
print('Четные элементы через фильтр: [' + ', '.join(map(str, numbers2)) + ']')


