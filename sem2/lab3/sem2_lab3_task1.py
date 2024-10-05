from collections import deque
from typing import List

from common import solve

""" 
Функция проверяет, существует ли путь между двумя заданными вершинами в неориентированном графе.
Принимает список строк, представляющих входные данные, и возвращает список строк с результатом.
"""


def get_solution(input_lines: List[str]) -> List[str]:
    # Разбор первой строки для получения количества вершин и рёбер
    n, m = map(int, input_lines[0].split())

    # Инициализация списка смежности
    adjacency_list = {i: [] for i in range(1, n + 1)}

    # Построение графа из списка рёбер
    for i in range(1, m + 1):
        a, b = map(int, input_lines[i].split())
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

    # Получение вершин u и v для проверки пути
    u, v = map(int, input_lines[m + 1].split())

    queue = deque()
    visited = set()

    # Начало поиска с вершины u
    queue.append(u)
    visited.add(u)

    # Выполнение BFS для поиска пути до v
    while queue:
        current = queue.popleft()

        if current == v:
            return ["1"]

        for neighbor in adjacency_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Если путь не найден
    return ["0"]


solve(get_solution)
