#!/usr/bin/python3

# Упражнение 9
# Задание 5

# Вводится имя файла. Требуется проверить, что его расширение входит в список допустимых (png, jpg, jpeg, gif, svg').

extensions = ('png', 'jpg', 'jpeg', 'gif', 'svg')
str = input('Введите имя файла: ')
extension = str.split('.').pop()
print('Расширение файла \'{}\' '.format(extension), end='')
if extension not in extensions:
    print('не ', end='')
print('входит в список допустимых (png, jpg, jpeg, gif, svg)',)
