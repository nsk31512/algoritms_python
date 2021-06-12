'''
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех
 уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.

Задание 3-5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных
значения.
'''
from random import randint
import cProfile
import functools


def find_max_neg(start, end, my_range):
    new_list = [randint(start, end) for el in range(my_range)]
    new_list.sort()

    def _find_max_neg(my_list):
        right = my_list[-1]
        centr = int(len(my_list) / 2)
        pos = my_list[centr]
        if right < 0:
            return right
        elif pos >= 0:
            return _find_max_neg(my_list[0:centr])
        else:
            return _find_max_neg(my_list[centr:-1])
    _find_max_neg(new_list)


#"task4_1.find_max_neg(-50,50,50)"
#1000 loops, best of 5: 31 usec per loop

#"task4_1.find_max_neg(-500,500,500)"
#1000 loops, best of 5: 323 usec per loop

#"task4_1.find_max_neg(-5000,5000,5000)"
#1000 loops, best of 5: 3.47 msec per loop

#cProfile.run('find_max_neg(-50, 50, 50)')
#288 function calls (283 primitive calls) in 0.000 seconds
#6/1    0.000    0.000    0.000    0.000 task4_1.py:13(_find_max_neg)
#1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}

#cProfile.run('find_max_neg(-500, 500, 500)')
#2531 function calls (2523 primitive calls) in 0.001 seconds
#9/1    0.000    0.000    0.000    0.000 task4_1.py:13(_find_max_neg)
#1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}

#cProfile.run('find_max_neg(-5000000, 5000000, 5000000)')
#28386338 function calls (28386318 primitive calls) in 8.687 seconds
#21/1    0.097    0.005    0.097    0.097 task4_1.py:24(_find_max_neg)
#1    1.338    1.338    1.338    1.338 {method 'sort' of 'list' objects}

def find_max_neg2(start, end, my_range):
    new_list = [randint(start, end) for el in range(my_range)]
    max_neg = start
    for item in new_list:
        if item > max_neg and item >= 0:
            max_neg = item
    return max_neg

#"task4_1.find_max_neg2(-50,50,50)"
#1000 loops, best of 5: 27.9 usec per loop

#"task4_1.find_max_neg2(-500,500,500)"
#1000 loops, best of 5: 300 usec per loop

#"task4_1.find_max_neg2(-5000,5000,5000)"
#1000 loops, best of 5: 3.13 msec per loop

#cProfile.run('find_max_neg2(-50, 50, 50)')
#274 function calls in 0.000 seconds

#cProfile.run('find_max_neg2(-500, 500, 500)')
#2515 function calls in 0.001 seconds

#cProfile.run('find_max_neg2(-5000000, 5000000, 5000000)')
#28387867 function calls in 7.236 seconds

def find_max_neg3(start, end, my_range):
    new_list = [randint(start, end) for el in range(my_range)]
    max_neg = start
    for item in new_list:
        if item > max_neg and item >= 0:
            max_neg = item
            if max_neg == -1:
                break
    return max_neg

#"task4_1.find_max_neg3(-50,50,50)"
#1000 loops, best of 5: 27.7 usec per loop

#"task4_1.find_max_neg3(-500,500,500)"
#1000 loops, best of 5: 298 usec per loop

#"task4_1.find_max_neg3(-5000,5000,5000)"
#1000 loops, best of 5: 3.14 msec per loop

#cProfile.run('find_max_neg3(-50, 50, 50)')
#264 function calls in 0.000 seconds

#cProfile.run('find_max_neg3(-500, 500, 500)')
#2517 function calls in 0.001 seconds

#cProfile.run('find_max_neg3(-5000000, 5000000, 5000000)')
#28390878 function calls in 7.214 seconds

'''
Вывод: Несмотря на быстродействие бинарного поиска в первом алгоритме тратится время на сортировку, поэтому в данном 
случае наиболее предпочтительный третий вариант, в котором происходит перебор цикла и останавливается, как только 
максимальное число становится равным -1
'''