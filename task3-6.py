'''
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''

from random import randint

new_list = [randint(1, 100) for el in range(20)]

summ = 0
print(new_list) #для проверки

max(new_list)
index_of_max = new_list.index(max(new_list))
index_of_min = new_list.index(min(new_list))

if index_of_min <= index_of_max:
    for i in range(index_of_min+1, index_of_max):
        summ += new_list[i]
else:
    for i in range(index_of_max+1, index_of_min):
        summ += new_list[i]

print(f'Сумма между минимальным и максимальным = {summ}')
