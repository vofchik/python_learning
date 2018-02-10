#!/usr/bin/python3

# Упражнение 7
# Задание 6

# Работаем с чужим кодом. В коде из файла
# https://github.com/groall/python_learning/blob/master/lesson_04_cycles/task03.py нужно заменить повторяющееся
# с циклах действие суммирования на вызов функции, функция должна работать с глобальной переменной sumNumbers.

def add_to_memory(x: int):
    """Прибавляет значение к глобальной переменной sumNumbers.

    Ничего не возвращает."""
    global sumNumbers
    sumNumbers += x


x = input('Введите целое положительное число: ')

if not x.isdigit():
    print("Вы ввели не число")
    exit()

xInt = int(x)
if xInt < 1:
    print("Число не положительное")
    exit()

sumNumbers = 0
for i in range(1, xInt):
    add_to_memory(i)

print("Сумма", sumNumbers)

sumNumbers = 0
i = 1
while i < xInt:
    add_to_memory(i)
    i += 1

print("Сумма", sumNumbers)