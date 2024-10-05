import bisect
from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Решает задачу управления структурой данных для добавления, удаления элементов
    и нахождения k-го максимума.
    """

    n = int(input_lines[0])  # Читаем количество команд
    commands = input_lines[1:]  # Остальные строки - команды

    sorted_list = []  # Список для хранения элементов в отсортированном порядке
    output = []  # Список для хранения результатов команд типа 0

    for command in commands:
        parts = command.split()
        if len(parts) == 2:
            ci, ki = parts
            ki = int(ki)
        else:
            ci = parts[0]
            ki = None

        if ci in ["+1", "1"]:
            # Добавляем элемент ki в отсортированный список
            bisect.insort_left(sorted_list, ki)

        elif ci == "-1":
            # Удаляем элемент ki из отсортированного списка
            index = bisect.bisect_left(sorted_list, ki)
            if index < len(sorted_list) and sorted_list[index] == ki:
                sorted_list.pop(index)

        elif ci == "0":
            # Находим ki-й максимум
            # Так как список отсортирован по возрастанию, k-й максимум - это элемент с индекс -k
            kth_max = sorted_list[-ki]
            output.append(str(kth_max))

    return output


solve(get_solution)
