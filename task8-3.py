'''
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''

import random


def graf_generator():
    size = random.randrange(4, 10)
    graf = [0 for _ in range(size)]
    for k in range(len(graf)):
        vertexes = [0 for _ in range(1, size)]
        for i in range(len(vertexes)):
            vertexes[i] = random.randrange(k, size)
        vertexes = list(set(vertexes))
        for item in vertexes:
            if item == k:
                vertexes.remove(item)
        graf[k] = vertexes
    return graf

def dfs(graph, start, finish):
    lenght = len(graph)
    is_visited = [False] * lenght
    parent = [-1] * lenght
    cost = 0

    for i in range(start, lenght):
        for j in range(len(graph[i])):
            if graph[i][j] == finish:
                cost = 1
                return cost


new_graf = graf_generator()
print(new_graf)

start_vert = int(input('Введите стартовую точку: '))
finish_vert = int(input(f'Введите точку к которой нужно прийти. Не более глубины графа = {len(new_graf)}: '))