from typing import List, Optional

from common import solve


class TreeNode:
    """
    Узел двоичного дерева поиска.
    """

    def __init__(self, key: int):
        self.key: int = key
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class BinarySearchTree:
    """
    Реализация простого двоичного дерева поиска.
    """

    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, key: int) -> None:
        """Добавляет ключ в дерево, если его еще нет."""
        if self.root is None:
            self.root = TreeNode(key)
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = TreeNode(key)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = TreeNode(key)
                    return
                current = current.right
            else:
                # Ключ уже существует, ничего не делаем
                return

    def exists(self, key: int) -> bool:
        """Проверяет существование ключа в дереве."""
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return True
        return False

    def find_min(self, node: TreeNode) -> TreeNode:
        """Находит минимальный узел в поддереве."""
        while node.left:
            node = node.left
        return node

    def delete(self, key: int) -> None:
        """Удаляет ключ из дерева, если он существует."""
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_rec(node.left, key)
        elif key > node.key:
            node.right = self._delete_rec(node.right, key)
        else:
            # Узел найден
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Узел с двумя детьми
            temp = self.find_min(node.right)
            node.key = temp.key
            node.right = self._delete_rec(node.right, temp.key)

        return node

    def next(self, key: int) -> Optional[int]:
        """Находит минимальный элемент, строго больший заданного ключа."""
        current = self.root
        successor = None
        while current:
            if current.key > key:
                successor = current.key
                current = current.left
            else:
                current = current.right
        return successor

    def prev(self, key: int) -> Optional[int]:
        """Находит максимальный элемент, строго меньший заданного ключа."""
        current = self.root
        predecessor = None
        while current:
            if current.key < key:
                predecessor = current.key
                current = current.right
            else:
                current = current.left
        return predecessor


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Обрабатывает операции над двоичным деревом поиска и возвращает результаты операций exists, next, prev.
    """
    bst = BinarySearchTree()
    output: List[str] = []

    for line in input_lines:
        parts = line.strip().split()

        if not parts:
            continue

        operation = parts[0]

        x = int(parts[1])

        if operation == "insert":
            bst.insert(x)

        elif operation == "delete":
            bst.delete(x)

        elif operation == "exists":
            exists = bst.exists(x)
            output.append("true" if exists else "false")

        elif operation == "next":
            nxt = bst.next(x)
            output.append(str(nxt) if nxt is not None else "none")

        elif operation == "prev":
            prv = bst.prev(x)
            output.append(str(prv) if prv is not None else "none")

    return output


solve(get_solution)
