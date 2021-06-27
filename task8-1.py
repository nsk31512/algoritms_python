'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''

import random

N = random.randrange(2, 10)

matrix_graf = [[0 for _ in range(N)] for _ in range(N)]

for i in range(len(matrix_graf)):
    for j in range(len(matrix_graf)):
        # все, что выше главной диагонали не заполняется, т.к. получится что они здороваются дважды
        if i <= j:
            continue
        else:
            matrix_graf[i][j] = 1
#вывод графа
for item in matrix_graf:
    print(item)

count_of_greetings = 0
for item in matrix_graf:
    for el in item:
        count_of_greetings += el

print(count_of_greetings)
