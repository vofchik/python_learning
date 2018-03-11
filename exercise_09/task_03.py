#!/usr/bin/python3

# Упражнение 9
# Задание 3

# Дан текст:
# Eh bien, mon prince. Gênes et Lucques ne sont plus que des apanages, des поместья, de la famille Buonaparte.
# Non, je vous préviens que si vous ne me dites pas que nous avons la guerre, si vous vous permettez encore de pallier
# toutes les infamies, toutes les atrocités de cet Antichrist (ma parole, j'y crois) — je ne vous connais plus, vous
# n'êtes plus mon ami, vous n'êtes plus мой верный раб, comme vous dites

# Выведите все слова, встречающиеся в тексте, по одному на каждую строку.

# Слова должны быть отсортированы по убыванию их частоты появления в тексте, а при одинаковой частоте появления —
# в лексикографическом порядке.

# Указание. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости
# слова. Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота
# встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет
# сортировать список кортежей, при этом кортежи сравниваются по первому элементу, а если они равны — то по второму.
# Это почти то, что требуется в задаче.

from typing import List
import string

text = '''Eh bien, mon prince. Gênes et Lucques ne sont plus que des apanages, des поместья, de la famille Buonaparte. 
Non, je vous préviens que si vous ne me dites pas que nous avons la guerre, si vous vous permettez encore de pallier
toutes les infamies, toutes les atrocités de cet Antichrist (ma parole, j'y crois) — je ne vous connais plus, vous
n'êtes plus mon ami, vous n'êtes plus мой верный раб, comme vous dites'''

def replace_delimiters(x: string) -> string:
    '''Заменяет небуквы и не цифры точками'''
    return x if x.isalnum() else '.'

def remove_empty(x: List) -> bool:
    '''Удаляет пустые элементы списка'''
    return False if x == '' else True

sentence = ''.join(list(map(replace_delimiters, text)))
words = sentence.split('.')
words = list(filter(remove_empty, words))
dic = {}
for word in words:
    dic[word] = dic.get(word, 0) + 1
words_with_counts = []
for key, value in dic.items():
    words_with_counts.append((len(words) - value, key))
words_with_counts.sort()
for couple in words_with_counts:
    print(couple[1])
