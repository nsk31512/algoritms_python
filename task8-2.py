'''
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые
необходимо обойти.
'''

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph, start):
    lenght = len(graph)
    is_visited = [False] * lenght
    cost = [float('inf')] * lenght
    parent = [-1] * lenght
    list_of_vertexes = [] #список для пройденных вершин

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start


        min_cost = float('inf')
        for i in range(lenght):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                #добавляем пройденные вершины, чтобы не дублировались
                if i not in list_of_vertexes:
                    list_of_vertexes.append(i)
                start = i

    return cost, list_of_vertexes


s = int(input('От какой вершины идти: '))
cost, vertex = dijkstra(g, s)
print(f'Цена пути до каждой точки из точки {s} = {cost}. Список пройденных вершин: {vertex}')
