from collections import deque
from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Находит максимумы в каждом окне заданной ширины в массиве чисел.
    """

    # Парсинг входных данных
    n: int = int(input_lines[0].strip())

    array: List[int] = list(map(int, input_lines[1].strip().split()))

    m: int = int(input_lines[2].strip())

    # Инициализация деки для хранения индексов элементов
    dq: deque = deque()

    result: List[int] = []

    for i in range(n):
        # Удаление индексов элементов, которые вышли за пределы окна
        while dq and dq[0] <= i - m:
            dq.popleft()

        # Удаление индексов элементов, меньших текущего элемента
        while dq and array[i] >= array[dq[-1]]:
            dq.pop()

        # Добавление текущего индекса в деку
        dq.append(i)

        # Добавление максимума текущего окна в результат
        if i >= m - 1:
            result.append(array[dq[0]])

    # Преобразование результатов в строку
    output: List[str] = [" ".join(map(str, result))]

    return output


solve(get_solution)
