from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Рассчитывает количество отрезков, содержащих каждую из заданных точек.
    """

    # Чтение первой строки и разбор количества отрезков и точек
    s, p = map(int, input_lines[0].split())

    # Инициализация списков для начала и конца отрезков
    starts = []
    ends = []

    # Чтение отрезков
    for i in range(1, s + 1):
        a, b = map(int, input_lines[i].split())
        starts.append(a)
        ends.append(b)

    # Чтение точек
    points = list(map(int, input_lines[s + 1].split()))

    # Сортировка начала и конца отрезков
    starts.sort()
    ends.sort()

    # Инициализация списка для результатов
    result = []

    # Функция для подсчета количества элементов <= x с использованием бинарного поиска
    def count_leq(arr: List[int], x: int) -> int:
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= x:
                left = mid + 1
            else:
                right = mid
        return left

    # Подсчет для каждой точки количества содержащих отрезков
    for x in points:
        # Количество отрезков с началом <= x
        cnt_start = count_leq(starts, x)

        # Количество отрезков с концом < x
        cnt_end = count_leq(ends, x - 1)

        # Количество отрезков, содержащих точку x
        count = cnt_start - cnt_end

        # Добавление результата в список
        result.append(str(count))

    # Возвращение результата в виде списка строк
    return [" ".join(result)]


solve(get_solution)
