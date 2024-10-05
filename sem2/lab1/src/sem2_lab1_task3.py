from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Распределяет объявления по слотам для максимизации общего дохода.
    """

    # Чтение числа объявлений
    n = int(input_lines[0])

    # Чтение прибыли за клик для каждого объявления
    a = list(map(int, input_lines[1].split()))

    # Чтение ожидаемого количества кликов для каждого слота
    b = list(map(int, input_lines[2].split()))

    # Сортировка прибыли по убыванию
    a_sorted = sorted(a, reverse=True)

    # Сортировка кликов по убыванию
    b_sorted = sorted(b, reverse=True)

    # Вычисление максимальной суммы произведений
    total = 0
    for i in range(n):
        total += a_sorted[i] * b_sorted[i]

    return [str(total)]


if __name__ == "__main__":
    solve(get_solution)
