#!/usr/bin/python3

# Упражнение 1 
# Задание 3

# Программа, которая считывает длины катетов прямоугольного треугольника и
# вычисляет длину его гипотенузы
len1 = input('Введи длину первого катета: ')
len2 = input('Введи длину второго катета: ')
try:
  len3 = (float(len1)**2+float(len2)**2)**0.5
except:
  print('Дружище, похоже ты ввел какую-то хуйню, а не длины катетов!')
  exit()  
print('Длина гипотенузы равна: {:.2f}'.format(len3))

