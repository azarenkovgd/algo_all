from common import solve


def get_solution(lines: list[str]) -> list[str]:
    """
    Программа сортирует массив целых чисел методом вставки и выводит отсортированный массив.
    """

    n = int(lines[0])

    array = list(map(int, lines[1].split()))

    # Алгоритм сортировки вставками
    for i in range(1, n):
        # Элемент, который будем вставлять
        key = array[i]
        j = i - 1

        # Сдвигаем элементы, которые больше ключа, вправо
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        # Вставляем ключ на нужное место
        array[j + 1] = key

    # Преобразуем отсортированный массив обратно в строку с числами через пробел
    sorted_array_str = " ".join(map(str, array))

    # Возвращаем результат в виде списка строк (одна строка)
    return [sorted_array_str]


solve(get_solution)
