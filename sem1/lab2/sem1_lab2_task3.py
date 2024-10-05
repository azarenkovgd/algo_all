from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Подсчитывает количество инверсий в заданном массиве чисел.
    """

    # Парсим количество элементов в массиве
    n = int(input_lines[0])

    # Парсим сам массив чисел
    array = list(map(int, input_lines[1].split()))

    # Вызываем функцию для подсчета инверсий
    inversions = count_inversions(array)

    # Возвращаем результат в виде списка строк
    return [str(inversions)]


def count_inversions(array: List[int]) -> int:
    """
    Использует сортировку слиянием для эффективного подсчета инверсий.
    """

    # Создаем вспомогательный массив для слияния
    temp_array = [0] * len(array)

    # Запускаем рекурсивную функцию сортировки слиянием
    return merge_sort(array, temp_array, 0, len(array) - 1)


def merge_sort(array: List[int], temp_array: List[int], left: int, right: int) -> int:
    # Инициализируем счетчик инверсий
    inv_count = 0

    # Базовый случай рекурсии
    if left < right:
        # Находим середину массива
        mid = (left + right) // 2

        # Рекурсивно сортируем левую половину и подсчитываем инверсии
        inv_count += merge_sort(array, temp_array, left, mid)

        # Рекурсивно сортируем правую половину и подсчитываем инверсии
        inv_count += merge_sort(array, temp_array, mid + 1, right)

        # Сливаем две половины и подсчитываем инверсии при слиянии
        inv_count += merge(array, temp_array, left, mid, right)

    return inv_count


def merge(array: List[int], temp_array: List[int], left: int, mid: int, right: int) -> int:
    # Инициализируем индексы для левой и правой половин
    i = left  # Начало левой половины
    j = mid + 1  # Начало правой половины
    k = left  # Начало вспомогательного массива
    inv_count = 0  # Счетчик инверсий

    # Сливаем левую и правую половины
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp_array[k] = array[i]
            i += 1
        else:
            temp_array[k] = array[j]
            # Элементы оставшиеся в левой половине являются инверсиями
            inv_count += mid - i + 1
            j += 1
        k += 1

    # Копируем оставшиеся элементы левой половины
    while i <= mid:
        temp_array[k] = array[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы правой половины
    while j <= right:
        temp_array[k] = array[j]
        j += 1
        k += 1

    # Копируем отсортированный сегмент обратно в оригинальный массив
    for idx in range(left, right + 1):
        array[idx] = temp_array[idx]

    return inv_count


solve(get_solution)
