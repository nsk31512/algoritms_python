'''
3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
включительно.
'''
from random import randint, uniform, randrange


def list_to_var(my_list, par):
    a = None
    b = None
    if par == 'str':
        a = my_list[0]
        b = my_list[1]
    elif par == 'int':
        a = int(my_list[0])
        b = int(my_list[1])
    elif par == 'float':
        a = float(my_list[0])
        b = float(my_list[1])
    return a, b


str_int = input('Введите 2 целых числа через пробел: ').split()
str_float = input('Введите 2 вещественных числа через пробел: ').split()
str_char = input('Введите 2 случайных символа алфавита через пробел: ').split()

x, y = list_to_var(str_int, 'int')
print(f'Случайное целое число {randint(x, y)}')
x, y = list_to_var(str_float, 'float')
print(f'Случайное вещественное число {uniform(x, y)}')
x, y = list_to_var(str_char, 'str')
print(f'Случайный символ {chr(randrange(ord(x), ord(y)))}')



