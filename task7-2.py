'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
'''

import random

my_list = [i for i in range(0, 50)]
random.shuffle(my_list)
print(my_list)


def merge_sort(list):
    if len(list) == 1 or len(list) == 0:
        return
    middle = len(list) // 2
    left_piece = list[:middle]
    right_piece = list[middle:]
    merge_sort(left_piece)
    merge_sort(right_piece)
    result_list = [0] * (len(left_piece) + len(right_piece))
    n = 0
    l = 0
    r = 0
    while r < len(right_piece) and l < len(left_piece):
        if right_piece[r] < left_piece[l]:
            result_list[n] = right_piece[r]
            r += 1
        else:
            result_list[n] = left_piece[l]
            l += 1
        n += 1
    while l < len(left_piece):
        result_list[n] = left_piece[l]
        l += 1
        n += 1
    while r < len(right_piece):
        result_list[n] = right_piece[r]
        r += 1
        n += 1
    for i in range(len(list)):
        list[i] = result_list[i]


merge_sort(my_list)
print(my_list)
