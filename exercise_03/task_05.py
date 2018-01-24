#!/usr/bin/python3

# Упражнение 3
# Задание 5

# Проверить, что введеные три числа (длины сторон) могут образовать 
# треугольник.
a = input('Введи длину a: ')
b = input('Введи длину b: ')
c = input('Введи длину с: ')
try:
  a = float(a)
  b = float(b)
  c = float(c)
  if a >= b and a >= c and a < b + c or (b >= a and b >= c 
and b < a + c) or c >= a and c >= b and c < a + b:
    print('Треугольник возможен')
  else:
    print('Треугольник невозможен')
except:
  print('Дружище, похоже ты ввел какую-то хуйню, а не координаты!')
