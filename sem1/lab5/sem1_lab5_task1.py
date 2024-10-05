from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Проверяет, является ли заданный массив неубывающей пирамидой.
    Возвращает "YES", если массив соответствует условиям, и "NO" в противном случае.
    """

    # Преобразование первой строки в целое число n
    n = int(input_lines[0])

    # Преобразование второй строки в список целых чисел
    array = list(map(int, input_lines[1].split()))

    # Итерация по каждому элементу массива для проверки условий кучи
    for i in range(1, n + 1):
        left_index = 2 * i
        right_index = 2 * i + 1

        # Проверка наличия левого потомка и сравнение значений
        if left_index <= n:
            if array[i - 1] > array[left_index - 1]:
                return ["NO"]

        # Проверка наличия правого потомка и сравнение значений
        if right_index <= n:
            if array[i - 1] > array[right_index - 1]:
                return ["NO"]

    # Если все условия выполнены, возвращаем "YES"
    return ["YES"]


solve(get_solution)
