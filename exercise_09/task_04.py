#!/usr/bin/python3

# Упражнение 9
# Задание 4

# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
#
# Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота равна
# 0, у любого другого элемента высота на 1 больше, чем у его родителя.
#
# Вам дано генеалогическое древо, определите высоту всех его элементов.
# Входные данные
#
# Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие родителя для
# каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.
#
# Выходные данные
#
# Программа должна вывести список всех элементов древа в лексикографическом порядке. После вывода имени каждого элемента
# необходимо вывести его высоту.
#
# Alexei Peter_I
# Anna Peter_I
# Elizabeth Peter_I
# Peter_II Alexei
# Peter_III Anna
# Paul_I Peter_III
# Alexander_I Paul_I
# Nicholaus_I Paul_I


from typing import Dict, List

def try_to_put_branch_to_branch(src: Dict, dst: Dict) -> bool:
    '''Пытается вставить дерево src в дерево dst, если получается возвращает True'''
    for name in src.keys():
        pass
    for key, value in dst.items():
        if key == name:
            if value == None:
                dst.update(src)
            else:
                value.update(src[name])
            return True
        if value != None:
            if try_to_put_branch_to_branch(src, value):
                return True
    return False

def calculate_weight(tree: Dict, weights: Dict, level: int = 0):
    '''Рассчитывает вес элементов для дерева tree в словаре weights'''
    for key, value in tree.items():
        weights[key] = level
        if value != None:
            calculate_weight(value, weights, level + 1)

try:
    n = int(input('Введите число элементов в генеалогическом древе: '))
    if n < 2: raise ValueError('Value must be greather than 1')
    print('Теперь введи {:d} строк вида имя_потомка имя_родителя'.format(n-1))
    couples = []
    for _ in range (1, n):
        str = input()
        couples.append(str)
except(TypeError, ValueError):
    print('Давай нормально вводить!')
    exit()

# make dic for branches
branches = {}
for couple_str in couples:
    couple = couple_str.split(" ")
    branches.setdefault(couple[1], {}).update({couple[0]: None})

# try to put one branch to others
while len(branches) > 1:
    children = branches.popitem()
    children = {children[0]: children[1]}
    success = False
    for key, value in branches.items():
        if try_to_put_branch_to_branch(children, value):
            success = True
    if not success:
        branches.update(children)

# calculate weight
weights = {}
calculate_weight(branches, weights)
for key in sorted(weights.keys()):
    print('{}: {:d}'.format(key, weights[key]))
