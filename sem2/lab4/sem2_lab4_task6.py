from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Функция get_solution вычисляет Z-функцию для заданной строки.
    Принимает список строк из input.txt и возвращает список строк для output.txt.
    """

    s = input_lines[0]
    n = len(s)
    z = [0] * n

    # Инициализация левого и правого краев окна
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            # Используем ранее вычисленные значения для ускорения
            z[i] = min(r - i + 1, z[i - l])

        # Расширяем окно, если возможно
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        # Обновляем левый и правый края окна
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    # Преобразуем результаты в строку, разделенную пробелами
    z_values = " ".join(map(str, z[1:]))

    return [z_values]


solve(get_solution)
