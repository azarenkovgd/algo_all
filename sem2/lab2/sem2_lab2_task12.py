from typing import List

from common import solve


class Node:
    """
    Класс для представления узла бинарного дерева поиска.
    """

    def __init__(self, key: int, left: int, right: int):
        self.key: int = key
        self.left: int = left
        self.right: int = right


# Функция для вычисления высоты поддерева
def compute_height(index: int, nodes: List[Node], balance_factors: List[int]) -> int:
    if index == 0:
        return 0

    # Получение соответствующего узла
    node = nodes[index - 1]

    # Рекурсивный вызов для левого поддерева
    left_height = compute_height(node.left, nodes, balance_factors)

    # Рекурсивный вызов для правого поддерева
    right_height = compute_height(node.right, nodes, balance_factors)

    # Вычисление баланс-фактора текущего узла
    balance_factors[index] = right_height - left_height

    # Вычисление высоты текущего поддерева
    current_height = 1 + max(left_height, right_height)

    return current_height


def get_solution(input_lines: List[str]) -> List[str]:
    # Парсинг количества вершин
    n = int(input_lines[0])

    if n == 0:
        return []

    # Создание списка узлов
    nodes: List[Node] = []

    for i in range(1, n + 1):
        parts: List[int] = list(map(int, input_lines[i].strip().split()))
        key, left, right = parts
        nodes.append(Node(key, left, right))

    # Массив для хранения баланс-факторов
    balance_factors = [0] * (n + 1)

    # Вычисление высот и баланс-факторов начиная с корня (вершина 1)
    compute_height(1, nodes, balance_factors)

    # Подготовка выходных данных
    output: List[str] = []

    for i in range(1, n + 1):
        output.append(str(balance_factors[i]))

    return output


solve(get_solution)
