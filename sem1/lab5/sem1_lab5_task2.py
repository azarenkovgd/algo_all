from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Вычисляет высоту произвольного дерева, заданного списком родительских узлов.
    Функция принимает список строк, представляющих содержимое input.txt, и возвращает список строк для output.txt.
    """

    # Чтение количества узлов
    n = int(input_lines[0])

    # Чтение родительских узлов и конвертация в список целых чисел
    parent = list(map(int, input_lines[1].split()))

    # Инициализация списка смежности для представления дерева
    children = [[] for _ in range(n)]

    root = -1

    for i in range(n):
        if parent[i] == -1:
            # Определение корневого узла
            root = i
        else:
            # Добавление дочернего узла к родителю
            children[parent[i]].append(i)

    # Инициализация переменной для хранения высоты дерева
    height = 0

    # Инициализация очереди для обхода дерева в ширину (BFS)
    queue = [(root, 1)]  # Кортеж содержит узел и его текущую глубину

    while queue:
        current_node, current_depth = queue.pop(0)

        # Обновление максимальной высоты
        if current_depth > height:
            height = current_depth

        # Добавление дочерних узлов в очередь с увеличенной глубиной
        for child in children[current_node]:
            queue.append((child, current_depth + 1))

    # Возвращение высоты дерева в виде списка строк
    return [str(height)]


solve(get_solution)
