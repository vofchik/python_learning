#!/usr/bin/python3

# Упражнение 7
# Задание 5

# Написать функцию, приминмающую номер месяца и возвращающую время года, которому принадледжит месяц. Не забыть про
# проверки входных данных в самой функции. Вызвать функцию в цикле несколько раз для случайных значений номера месяца.


import random

def get_season(m: int, exception_if_fail: bool = 1) -> str:
    """Возвращающает время года, которому принадледжит месяц по номеру месяца.

    При некорректном вводе если exception_if_fail установлен в 1 вызывает исключение ValueError,
    иначе возвращает кортеж нулей"""
    if not isinstance(m, int):
        if exception_if_fail: raise TypeError('Argument must be an integer!')
        m = 0
    if (m == 12) or (1 <= m <= 2):
        return 'зима'
    elif 3 <= m <= 5:
        return 'весна'
    elif 6 <= m <= 8:
        return 'лето'
    elif 9 <= m <= 11:
        return 'осень'
    else:
        if exception_if_fail: raise ValueError('Argument must be number of a month!')
        return 'неизвестное'

for _ in range(10):
    m = random.randint(1, 12)
    print('Месяц номер: {:2d} Время года: {}'.format(m, get_season(m)))

