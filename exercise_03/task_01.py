#!/usr/bin/python3

# Упражнение 3 
# Задание 1

# Вычислить модуль числа без использования библиотечных функций.
number = input('Введи число: ')
try:
  number = float(number)
  if number < 0:
     number = -number
except:
  print('Дружище, похоже ты ввел какую-то хуйню, а не число!')
  exit()  
print('Модуль числа {:.2f}'.format(number))

