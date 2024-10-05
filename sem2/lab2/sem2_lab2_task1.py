from typing import List, Dict

from common import solve


class TreeNode:
    """Класс для представления узла бинарного дерева."""

    def __init__(self, key: int, left: int, right: int):
        self.key = key
        self.left = left
        self.right = right


def build_tree(n: int, nodes_info: List[List[int]]) -> Dict[int, TreeNode]:
    """
    Строит дерево из предоставленной информации о узлах.
    """
    tree = {}

    for i in range(n):
        key, left, right = nodes_info[i]
        tree[i] = TreeNode(key, left, right)

    return tree


def inorder_traversal(node_index: int, tree: Dict[int, TreeNode], result: List[int]) -> None:
    """
    Выполняет центрированный обход дерева.
    """
    if node_index == -1:
        return

    # Рекурсивно обходим левое поддерево
    inorder_traversal(tree[node_index].left, tree, result)

    # Добавляем ключ текущего узла
    result.append(tree[node_index].key)

    # Рекурсивно обходим правое поддерево
    inorder_traversal(tree[node_index].right, tree, result)


def preorder_traversal(node_index: int, tree: Dict[int, TreeNode], result: List[int]) -> None:
    """
    Выполняет прямой обход дерева.
    """
    if node_index == -1:
        return

    # Добавляем ключ текущего узла
    result.append(tree[node_index].key)

    # Рекурсивно обходим левое поддерево
    preorder_traversal(tree[node_index].left, tree, result)

    # Рекурсивно обходим правое поддерево
    preorder_traversal(tree[node_index].right, tree, result)


def postorder_traversal(node_index: int, tree: Dict[int, TreeNode], result: List[int]) -> None:
    """
    Выполняет обратный обход дерева.
    """
    if node_index == -1:
        return

    # Рекурсивно обходим левое поддерево
    postorder_traversal(tree[node_index].left, tree, result)

    # Рекурсивно обходим правое поддерево
    postorder_traversal(tree[node_index].right, tree, result)

    # Добавляем ключ текущего узла
    result.append(tree[node_index].key)


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Решает задачу обхода бинарного дерева тремя способами: in-order, pre-order, post-order.
    """
    n = int(input_lines[0])

    nodes_info = []
    for i in range(1, n + 1):
        parts = list(map(int, input_lines[i].split()))
        nodes_info.append(parts)

    tree = build_tree(n, nodes_info)

    in_order = []
    inorder_traversal(0, tree, in_order)

    pre_order = []
    preorder_traversal(0, tree, pre_order)

    post_order = []
    postorder_traversal(0, tree, post_order)

    # Формируем строки для вывода
    in_order_str = " ".join(map(str, in_order))
    pre_order_str = " ".join(map(str, pre_order))
    post_order_str = " ".join(map(str, post_order))

    return [in_order_str, pre_order_str, post_order_str]


solve(get_solution)
