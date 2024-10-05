from typing import List, Dict, Optional

from common import solve

NONE_VALUE = "<none>"


class ListNode:
    """
    Класс узла для связанного списка
    """

    def __init__(self, key: str, value: str):
        self.key: str = key
        self.value: str = value
        self.prev: Optional[ListNode] = None
        self.next: Optional[ListNode] = None


class AssociativeArray:
    """
    Класс ассоциативного массива с поддержкой порядка вставки
    """

    def __init__(self):
        self.map: Dict[str, ListNode] = {}
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None

    def put(self, key: str, value: str) -> None:
        if key in self.map:
            # Обновляем значение существующего ключа
            self.map[key].value = value
        else:
            # Создаем новый узел и добавляем в конец списка
            new_node = ListNode(key, value)

            if not self.head:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

            self.map[key] = new_node

    def get(self, key: str) -> str:
        if key in self.map:
            return self.map[key].value

        return NONE_VALUE

    def delete(self, key: str) -> None:
        if key not in self.map:
            return

        node = self.map.pop(key)

        # Удаляем узел из связанного списка
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def prev(self, key: str) -> str:
        if key not in self.map:
            return NONE_VALUE

        node = self.map[key]

        if node.prev:
            return node.prev.value

        return NONE_VALUE

    def next(self, key: str) -> str:
        if key not in self.map:
            return NONE_VALUE

        node = self.map[key]

        if node.next:
            return node.next.value

        return NONE_VALUE


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Реализует ассоциативный массив с операциями get, prev, next, put, delete.
    Обрабатывает список команд и возвращает результаты операций get, prev, next.
    """

    n = int(input_lines[0])
    aa = AssociativeArray()
    output = []

    for i in range(1, n + 1):
        parts = input_lines[i].split()
        command = parts[0]

        if command == "put":
            key = parts[1]
            value = parts[2]
            aa.put(key, value)

        elif command == "get":
            key = parts[1]
            result = aa.get(key)
            output.append(result)

        elif command == "delete":
            key = parts[1]
            aa.delete(key)

        elif command == "prev":
            key = parts[1]
            result = aa.prev(key)
            output.append(result)

        elif command == "next":
            key = parts[1]
            result = aa.next(key)
            output.append(result)

    return output


solve(get_solution)
