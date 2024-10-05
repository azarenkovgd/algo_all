from collections import deque
from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Реализует очередь с операциями добавления, удаления и запроса минимального элемента.
    """

    # Чтение количества команд
    m = int(input_lines[0])

    # Инициализация основной очереди и очереди для минимальных элементов
    queue = deque()
    min_queue = deque()

    # Список для хранения результатов запросов
    results = []

    # Обработка каждой команды
    for line in input_lines[1 : m + 1]:
        parts = line.strip().split()

        if parts[0] == "+":
            number = int(parts[1])

            # Добавление элемента в основную очередь
            queue.append(number)

            # Удаление элементов из min_queue, которые больше добавляемого числа
            while min_queue and min_queue[-1] > number:
                min_queue.pop()

            # Добавление нового элемента в очередь минимумов
            min_queue.append(number)

        elif parts[0] == "-":
            # Извлечение элемента из основной очереди
            removed = queue.popleft()

            # Если извлеченный элемент равен текущему минимуму, удаляем его из min_queue
            if removed == min_queue[0]:
                min_queue.popleft()

        elif parts[0] == "?":
            # Добавление текущего минимума в результаты
            results.append(str(min_queue[0]))

    return results


solve(get_solution)
