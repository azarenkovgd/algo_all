from common import solve


def get_solution(input_lines: list[str]) -> list[str]:
    """
    Сортирует заданный массив чисел с помощью сортировки слиянием без использования сигнальных значений.
    """

    # Преобразуем вторую строку в список целых чисел
    arr = list(map(int, input_lines[1].split()))

    # Выполняем сортировку слиянием
    merge_sort(arr)

    # Преобразуем отсортированный массив в строку с пробелами между числами
    output_line = " ".join(map(str, arr))

    # Возвращаем результат в виде списка строк
    return [output_line]


def merge_sort(arr: list[int]) -> None:
    """Рекурсивно разделяет массив и сортирует его части с помощью функции merge."""

    # Если массив состоит из одного элемента, то он уже отсортирован
    if len(arr) > 1:
        # Находим середину массива
        mid = len(arr) // 2

        # Делим массив на две половины
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивно сортируем каждую половину
        merge_sort(left_half)
        merge_sort(right_half)

        # Сливаем отсортированные половины
        merge(arr, left_half, right_half)


def merge(arr: list[int], left: list[int], right: list[int]) -> None:
    """Сливает два отсортированных массива в один без использования сигнальных значений."""

    # Инициализируем индексы для левого, правого и основного массива
    i = j = k = 0

    # Пока в обоих массивах есть элементы
    while i < len(left) and j < len(right):
        # Сравниваем элементы и добавляем меньший в основной массив
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Если в левом массиве остались элементы, добавляем их в основной массив
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Если в правом массиве остались элементы, добавляем их в основной массив
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


solve(get_solution)
