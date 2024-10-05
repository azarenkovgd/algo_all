from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Определяет порядок строк после k фаз цифровой сортировки.
    """

    # Чтение первой строки для получения n, m и k
    first_line = input_lines[0].strip().split()
    n = int(first_line[0])  # Количество строк
    m = int(first_line[1])  # Длина каждой строки
    k = int(first_line[2])  # Количество фаз сортировки

    # Инициализация списка строк
    strings = ["" for _ in range(n)]

    # Формирование строк из вертикального ввода
    for i in range(m):
        current_line = input_lines[i + 1].strip()

        for j in range(n):
            strings[j] += current_line[j]

    # Индексы строк для сортировки
    indices = list(range(1, n + 1))

    # Выполнение k фаз цифровой сортировки
    for phase in range(1, k + 1):
        # Определение позиции символа для текущей фазы (с конца)
        pos = m - phase

        # Сортировка индексов на основе символа на позиции pos
        indices.sort(key=lambda x: strings[x - 1][pos])

    # Преобразование списка индексов в строку с пробелами
    result: str = " ".join(map(str, indices))

    # Возврат результата в виде списка строк
    return [result]


solve(get_solution)
