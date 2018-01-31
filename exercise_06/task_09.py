#!/usr/bin/python3

# Упражнение 6 
# Задание 9

# Посчитать количество слов в введёном с клавиатуры предложении.


import string

sentence = input('Введи предложение: ')
is_prev_delimiter = 1
count = 0
for i in range(len(sentence)):
    if is_prev_delimiter & sentence[i].isalnum(): count += 1
    is_prev_delimiter = not sentence[i].isalnum()
print('Количество слов через цикл: {:d}'.format(count))
def replace_delimiters(x): return x if x.isalnum() else '.'
sentence = ''.join(list(map(replace_delimiters, sentence)))
words = sentence.split('.')
def remove_empty(x): return 0 if x == '' else 1
words = list(filter(remove_empty, words))
print('Количество слов через еблю со списками: {:d}'.format(len(words)))
