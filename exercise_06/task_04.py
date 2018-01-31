#!/usr/bin/python3

# Упражнение 6 
# Задание 4

# Заполнить список из шести элементов произвольными целочисленными значениями.
# Найти максимальный элемент в списке, вывести его и его номер на экран. Два
# варианта вычисления максимального элемента: с приминением цикла и без него.


import random

numbers = [random.randint(0, 1000) for i in range(6)]
print('Список: [' + ', '.join(map(str, numbers)) + ']')
max_index = 0
max_number = numbers[0]
for i in range(1, 6):
    if (numbers[i] > max_number):
        max_number = numbers[i]
        max_index = i
print('Максимальный элемент с циклом: {:d}, его номер: {:d}'.format(max_number, max_index + 1))
max_number = max(numbers)
print('Максимальный элемент без цикла: {:d}, его номер: {:d}'.format(max_number, numbers.index(max_number) + 1))
