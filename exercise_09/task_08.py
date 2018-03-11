#!/usr/bin/python3

# Упражнение 9
# Задание 8

# С помощью словаря из файла codes.txt расшифровать текст
# 006005034028017006029034028017006006017036034028020021029034028017028017

from typing import List
import string
import sys

if len(sys.argv) != 2:
    print('Incorrect number of arguments!')
    print('Example: python3 task_08.py text.txt')
    exit()

try:
    file = open(sys.argv[1])
except:
    print('File open error!')
    exit()
dic = {}
for str in file:
    couple = str.split('\t')
    dic[couple[1].rstrip()] = couple[0]
file.close()
src = '006005034028017006029034028017006006017036034028020021029034028017028017'
dst = ''
for i in range(0, len(src), 3):
    key = src[i] + src[i + 1] + src[i + 2]
    dst += dic[key]
print(dst)