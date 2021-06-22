from sys import getsizeof

#3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] win32

from random import randint
list_for_size = []

new_list = [randint(1, 100) for el in range(20)]

list_for_size.append(new_list)

summ = 0

index_of_max = new_list.index(max(new_list))
index_of_min = new_list.index(min(new_list))

list_for_size.append(index_of_max)
list_for_size.append(index_of_min)

if index_of_min <= index_of_max:
    for i in range(index_of_min+1, index_of_max):
        summ += new_list[i]
else:
    for i in range(index_of_max+1, index_of_min):
        summ += new_list[i]
list_for_size.append(summ)
'''
i = 1
for item in list_for_size:
    print(f'Размер переменной {i} - {getsizeof(item)}')
    i += 1'''

'''
Размер переменной 1 - 248
Размер переменной 2 - 28
Размер переменной 3 - 24
Размер переменной 4 - 28
Итого: 328
'''

list_for_size = []

new_list = [randint(1, 100) for el in range(20)]

list_for_size.append(new_list)

summ = 0

maximum = new_list[0]
minimum = new_list[-1]
for item in new_list:
    if item > maximum:
        maximum = item

    if item < minimum:
        minimum = item
list_for_size.append(maximum)
list_for_size.append(minimum)
index_of_max = new_list.index(maximum)
index_of_min = new_list.index(minimum)

list_for_size.append(index_of_max)
list_for_size.append(index_of_min)

if index_of_min <= index_of_max:
    for i in range(index_of_min+1, index_of_max):
        summ += new_list[i]
else:
    for i in range(index_of_max+1, index_of_min):
        summ += new_list[i]
list_for_size.append(summ)
'''
i = 1
for item in list_for_size:
    print(f'Размер переменной {i} - {getsizeof(item)}')
    i += 1'''

'''
Размер переменной 1 - 248
Размер переменной 2 - 28
Размер переменной 3 - 28
Размер переменной 4 - 28
Размер переменной 5 - 28
Размер переменной 6 - 28
Итого: 388
'''

list_for_size = []

new_list = [randint(1, 100) for el in range(20)]

list_for_size.append(new_list)

summ = 0

if new_list.index(min(new_list)) <= new_list.index(max(new_list)):
    for i in range(new_list.index(min(new_list))+1, new_list.index(max(new_list))):
        summ += new_list[i]
else:
    for i in range(new_list.index(max(new_list))+1, new_list.index(min(new_list))):
        summ += new_list[i]
list_for_size.append(summ)

i = 1
for item in list_for_size:
    print(f'Размер переменной {i} - {getsizeof(item)}')
    i += 1

'''
Размер переменной 1 - 248
Размер переменной 2 - 28
Итого: 276
'''

#Таким образом, меньше всего памяти занимает программа с использованием функций min и max без введения дополнительных переменных.