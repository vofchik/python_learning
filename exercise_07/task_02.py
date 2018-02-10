#!/usr/bin/python3

# Упражнение 7
# Задание 2

# Написать функцию, возвращающую два введеных с клавиатуры числа.


import re

def input_two_floats(exception_if_fail: bool = 1) -> (float, float):
    """Возвращает два введеных с клавиатуры числа.

    При некорректном вводе если exception_if_fail установлен в 1 вызывает исключение ValueError,
    иначе возвращает кортеж нулей"""
    str = input('Введи два числа через пробел: ')
    if bool(re.match('[-+]?[0-9]*[.,]?[0-9]+(?:[eE][-+]?[0-9]+)?\ [-+]?[0-9]*[.,]?[0-9]+(?:[eE][-+]?[0-9]+)?$', str)):
        return tuple(map(float, str.split(' ')))
    else:
       if exception_if_fail: raise ValueError('Arguments must be two space-separated floats!')
       return 0.0, 0.0
