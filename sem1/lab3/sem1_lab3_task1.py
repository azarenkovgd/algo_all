import random
from typing import List

from common import solve


def partition(arr: List[int], low: int, high: int) -> int:
    """
    Функция разделяет массив и возвращает индекс опорного элемента.
    """
    pivot = arr[high]
    i = low - 1

    # Проходим по элементам и переставляем их относительно опорного
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Перемещаем опорный элемент на правильную позицию
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def randomized_quicksort(arr: List[int], low: int, high: int) -> None:
    """
    Рекурсивная реализация рандомизированной быстрой сортировки.
    """
    if low < high:
        # Выбираем случайный опорный элемент
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        # Получаем позицию опорного элемента после разделения
        pi = partition(arr, low, high)

        # Рекурсивно сортируем левую часть
        randomized_quicksort(arr, low, pi - 1)

        # Рекурсивно сортируем правую часть
        randomized_quicksort(arr, pi + 1, high)


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Считывает массив чисел из входных строк, сортирует его с помощью
    рандомизированной быстрой сортировки и возвращает отсортированный массив.
    """
    n = int(input_lines[0])

    # Преобразуем строку чисел в список целых чисел
    arr = list(map(int, input_lines[1].split()))

    # Вызываем функцию быстрой сортировки
    randomized_quicksort(arr, 0, n - 1)

    # Преобразуем отсортированный список обратно в строку
    sorted_arr_str = " ".join(map(str, arr))

    return [sorted_arr_str]


solve(get_solution)
