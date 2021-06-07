'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных
значения.
'''
from random import randint


def find_max_neg(my_list):
    right = my_list[-1]
    centr = int(len(my_list)/2)
    pos = my_list[centr]
    if right < 0:
        return right
    elif pos >= 0:
        return find_max_neg(my_list[0:centr])
    else:
        return find_max_neg(my_list[centr:-1])


new_list = [randint(-50, 50) for el in range(20)]
new_list.sort()
print(new_list) #для проверки правильного ответа
print(f'Максимальное отрицательно число в массиве = {find_max_neg(new_list)}')
