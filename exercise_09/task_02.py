#!/usr/bin/python3

# Упражнение 9
# Задание 2

# Дан список чисел, который может содержать до 100000 чисел (каждое число от 0 до 1000).
# Определите, сколько в нем встречается различных чисел.
# Эту задачу на Питоне можно решить в одну строчку, но нам нужно с помощью словаря.

import random

numbers = [random.randint(0, 1000) for _ in range(100000)]

dic = {}
for number in numbers:
    dic[number] = dic.get(number, 0) + 1
print(dic)