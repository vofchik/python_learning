#!/usr/bin/python3

# Упражнение 6 
# Задание 8

# Заполнить список из десяти элементов произвольными целочисленными значениями.
# Затем четные элементы расположить в начале списка, нечетные - в конце.


import random

numbers = [random.randint(0, 1000) for i in range(10)]
print('Cписок: [' + ', '.join(map(str, numbers)) + ']')
numbers1 = [numbers[i] for i in (list(range(1,10,2))+list(range(0,10,2)))]
print('Cписок через цикл: [' + ', '.join(map(str, numbers1)) + ']')
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
b = 0
numbers2 += list(filter(even, numbers))
print('Cписок через фильтр: [' + ', '.join(map(str, numbers2)) + ']')
