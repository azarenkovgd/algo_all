from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Вычисляет длину самой длинной общей подпоследовательности из трех последовательностей.
    """

    n = int(input_lines[0])

    first_sequence = list(map(int, input_lines[1].split()))

    m = int(input_lines[2])

    second_sequence = list(map(int, input_lines[3].split()))

    l = int(input_lines[4])

    third_sequence = list(map(int, input_lines[5].split()))

    # Инициализация 3D массива для динамического программирования
    dp = [[[0] * (l + 1) for _ in range(m + 1)] for __ in range(n + 1)]

    # Заполнение массива
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if first_sequence[i - 1] == second_sequence[j - 1] and first_sequence[i - 1] == third_sequence[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1

                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    # Получение результата из DP таблицы
    result = dp[n][m][l]

    return [str(result)]


solve(get_solution)
