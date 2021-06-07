'''
2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3,
15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), т. к.
 именно в этих позициях первого массива стоят четные числа.
'''

from random import randint

first_list = [randint(1, 100) for el in range(20)]
second_list = []

for i in range(len(first_list)):
    if first_list[i] % 2 == 0:
        second_list.append(i)
print(second_list)
