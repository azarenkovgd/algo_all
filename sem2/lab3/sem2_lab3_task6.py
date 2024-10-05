from collections import deque
from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Кратчайший путь между двумя городами в неориентированном графе.
    """

    # Разбираем первую строку, получаем количество вершин и ребер
    n, m = map(int, input_lines[0].split())

    # Инициализируем список смежности для представления графа
    graph = [[] for _ in range(n + 1)]  # Используем n + 1 для удобства индексации вершин с 1

    # Заполняем граф на основе последующих m строк
    for i in range(1, m + 1):
        a, b = map(int, input_lines[i].split())
        graph[a].append(b)
        graph[b].append(a)

    # Извлекаем вершины u и v, между которыми нужно найти кратчайший путь
    u, v = map(int, input_lines[m + 1].split())

    # Массив для хранения расстояний от вершины u до всех остальных
    distance = [-1] * (n + 1)
    distance[u] = 0  # Расстояние до себя равно нулю

    # Очередь для обхода графа в ширину (BFS)
    queue = deque()
    queue.append(u)

    # BFS для поиска кратчайшего пути
    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    # Получаем длину кратчайшего пути до вершины v
    result = distance[v]

    # Если пути нет, distance[v] останется равным -1

    # Возвращаем результат в виде списка строк
    return [str(result)]


solve(get_solution)
