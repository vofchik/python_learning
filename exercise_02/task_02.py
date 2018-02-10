#!/usr/bin/python3

# Упражнение 1 
# Задание 2

# Программа, которая считывает два числа и выводит их сумму
import re
str = input('Не будь долбоебом, введи два целых числа через пробел: ')
digits = str.split(' ')
if len(digits) == 2 and bool(re.match('^[0-9\-][0-9]+$',digits[0])
) and bool(re.match('^[0-9\-][0-9]+$',digits[1])):
  print('{} + {} = {}'.format(digits[0],digits[1],int(digits[0]) + int(digits[1])))

