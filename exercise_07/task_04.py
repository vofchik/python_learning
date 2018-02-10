#!/usr/bin/python3

# Упражнение 7
# Задание 4

# Написать функцию, принимающую длину стороны квадрата и рассчитывающую периметр квадрата, его площадь и диагональ.
# Сделать два и более варианта функции, которые должна отличаться количеством возвращаемых переменных.
# Не забыть про проверки входных данных в самой функции.


def calculate_square1(a: float, exception_if_fail: bool = 1) -> (float, float, float):
    """Возвращает периметр квадрата, его площадь и диагональ

    При некорректном вводе если exception_if_fail установлен в 1 вызывает исключение ValueError,
    иначе возвращает кортеж нулей"""
    if not isinstance(a, float) and not isinstance(a, int):
        if exception_if_fail: raise TypeError('The argument must be float!')
        a = 0.0
    if a <= 0.0:
       if exception_if_fail: raise ValueError('The argument must be greater than zero!')
       return 0.0, 0.0, 0.0
    return 4 * a, a * a, a * 2 ** 0.5
