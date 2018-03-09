#!/usr/bin/python3

# Упражнение 8
# Задание 1.1

# Создайте функции:
# 
# * генерации двумерного массива случайных чисел с заданными размерами
# * поиска максимальныъ чисел в каждой строке двумерного массива (2 функции)
# * проверки любой переменной на то, что она содержит положительное целое число
# и приведение переменной к int
# Поместите полученные функции в отдельный модуль. 
# Итоговую программу оформите в отдельном модуле (файле). 

from typing import Dict, List
import random
import sys

def get_two_dimensional_array(m: int, n: int, min: int = 0, max: int = 100) -> List:
    """Возвращает двумерный массив m*n случайных чисел от min до max"""
    return [[random.randint(min, max) for _ in range(n)] for _ in range(m)]

def get_maximums_of_two_dimensional_array(a: List) -> List:
    """Возвращает список максимумов двумерного массива целых положительных чисел"""
    return list(map(max, a))

def check_and_get_int(x) -> Dict:
    """Проверяет является аргумент x положительным целым числом
    Возвращает словарь is_int: bool и value: int"""
    try:
        value = int(x)
        return {'is_int': True, 'value': value}
    except(TypeError, ValueError):
        return {'is_int': False, 'value': 0}

    def get_maximum_in_array(b: List):
        max = 0
        for e in b:
            if max < e: max = e
        return max
    maximums = list(map(get_maximum_in_array,a))
    return maximums


