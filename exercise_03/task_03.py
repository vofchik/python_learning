#!/usr/bin/python3

# Упражнение 3 
# Задание 3

# Проверить, что хотя бы одно из чисел a или b оканчивается на 0.
a = input('Введи число a: ')
b = input('Введи число b: ')
try:
  temp = float(a)
  temp = float(b)
  if a[len(a)-1] == '0' or b[len(b)-1] == '0':
     print('Хотя бы одно из чисел оканчивается на 0')
  else:
     print('Ни одно из чисел не оканчивается на 0')
except:
  print('Дружище, похоже ты ввел какую-то хуйню, а не координаты!')


