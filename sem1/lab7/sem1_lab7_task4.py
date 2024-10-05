from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Функция для вычисления длины самой длинной общей подпоследовательности двух последовательностей.
    """

    n = int(input_lines[0])

    first_sequence = list(map(int, input_lines[1].split()))

    m = int(input_lines[2])

    second_sequence = list(map(int, input_lines[3].split()))

    # Инициализация массив для динамического программирования
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Заполнение массив
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first_sequence[i - 1] == second_sequence[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Длина самой длинной общей подпоследовательности
    lcs_length = dp[n][m]

    return [str(lcs_length)]


solve(get_solution)
