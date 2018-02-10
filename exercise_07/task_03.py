#!/usr/bin/python3

# Упражнение 7
# Задание 3

# Использовать функции из задач 1, 2 для решения задания 2 из урока 2:
# Программа, которая считывает два числа и выводит их сумму


import task_01
import task_02

try:
    a,b = task_02.input_two_floats()
except ValueError as e:
    print('Ты ввел что-то не то! Возникла ошибка: {}'.format(e))
    exit()
print('Сумма введенных чисел {:.2f}'.format(task_01.sum_of_two_floats(a, b)))

