from typing import List, Dict

from common import solve

""" 
Функция get_solution принимает список строк, представляющих входные данные, 
и возвращает список строк с результатом – количеством компонент сильной связности.
"""


# Функция для выполнения DFS и заполнения порядка завершения
def dfs_first(u: int, visited: List[bool], stack: List[int], adj: Dict[int, List[int]]) -> None:
    visited[u] = True

    for v in adj[u]:
        if not visited[v]:
            dfs_first(v, visited, stack, adj)

    stack.append(u)


# Функция для выполнения DFS на транспонированном графе
def dfs_second(u: int, visited: List[bool], adj_transpose: Dict[int, List[int]]) -> None:
    visited[u] = True

    for v in adj_transpose[u]:
        if not visited[v]:
            dfs_second(v, visited, adj_transpose)


def get_solution(input_lines: List[str]) -> List[str]:
    # Разбор первой строки для получения количества вершин и ребер
    n, m = map(int, input_lines[0].split())

    # Создание списка смежности для графа
    adj: Dict[int, List[int]] = {i: [] for i in range(1, n + 1)}

    # Заполнение списка смежности ребрами из входных данных
    for line in input_lines[1 : m + 1]:
        u, v = map(int, line.split())
        adj[u].append(v)

    # Транспонирование графа
    adj_transpose: Dict[int, List[int]] = {i: [] for i in range(1, n + 1)}

    for u in adj:
        for v in adj[u]:
            adj_transpose[v].append(u)

    # Первый проход DFS для заполнения стека
    stack: List[int] = []
    visited: List[bool] = [False] * (n + 1)

    for u in range(1, n + 1):
        if not visited[u]:
            dfs_first(u, visited, stack, adj)

    # Второй проход DFS на транспонированном графе
    visited = [False] * (n + 1)
    count = 0

    while stack:
        u = stack.pop()

        if not visited[u]:
            dfs_second(u, visited, adj_transpose)
            count += 1

    # Возврат результата в виде списка строк
    return [str(count)]


solve(get_solution)
