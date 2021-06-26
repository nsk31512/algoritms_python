'''
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой — не больше медианы.
'''

import random

m = int(random.random() * 10)
my_list = [i for i in range(2 * m + 1)]
random.shuffle(my_list)
print(my_list)

sum = 0
for item in my_list:
    sum += item
median = int(sum / len(my_list))
print(median)
