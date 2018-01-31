#!/usr/bin/python3

# Упражнение 6 
# Задание 6

# Заполнить список из шести элементов квадратными корнями произвольных
# целочисленных значений. Вывести список на экран через запятую.

import random


roots = [random.randint(0,10000) ** 0.5 for i in range(6)]
def float_as_str(x): return '{:.2f}'.format(x)
print('Когни: ' + ', '.join(map(float_as_str, roots)))
