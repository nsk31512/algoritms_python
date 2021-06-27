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
    path = [start, finish]  # путь от старта до финиша
    while start != finish:
        for i in range(start, len(graph)):
            vertex = graph[i]
            if finish in graph[start]:
                start = finish
                break
            if finish in vertex and i > start:
                path.insert(1, i)
                finish -= i
                i = start
                break
            elif i == len(graph) - 1:
                start = finish
                path = []
                break
    path = list(set(path))
    return path


new_graf = graf_generator()
#new_graf = [[1, 2], [3, 4, 5], [5], [4, 6], [], [], []] #этот граф для написания кода удобной проверки
print(new_graf)

start_vert = int(input('Введите стартовую точку: '))
finish_vert = int(input(f'Введите точку к которой нужно прийти. Не более глубины графа = {len(new_graf)-1}: '))
print (dfs(new_graf, start_vert, finish_vert))
