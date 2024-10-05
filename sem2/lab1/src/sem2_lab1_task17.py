from typing import List

from common import solve

MOD = 10**9


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Определяет количество телефонных номеров заданной длины, которые можно набрать ходом коня на клавиатуре.
    """
    n = int(input_lines[0])

    # Определяем переходы для каждого ключа
    moves: dict[str, List[str]] = {
        "1": ["6", "8"],
        "2": ["7", "9"],
        "3": ["4", "8"],
        "4": ["3", "9", "0"],
        "5": [],
        "6": ["1", "7", "0"],
        "7": ["2", "6"],
        "8": ["1", "3"],
        "9": ["2", "4"],
        "0": ["4", "6"],
    }

    # Начальные цифры (не 0 и не 8)
    initial_digits: List[str] = ["1", "2", "3", "4", "5", "6", "7", "9"]

    # Инициализируем динамическое программирование
    dp_prev: dict[str, int] = {digit: 1 for digit in initial_digits}

    # Обрабатываем номера длины от 2 до N
    for _ in range(2, n + 1):
        dp_current: dict[str, int] = {digit: 0 for digit in moves.keys()}

        for digit, count in dp_prev.items():
            for next_digit in moves[digit]:
                dp_current[next_digit] = (dp_current[next_digit] + count) % MOD

        dp_prev = dp_current

    # Вычисляем итоговую сумму по всем возможным цифрам
    total = sum(dp_prev.values()) % MOD

    return [str(total)]


if __name__ == "__main__":
    solve(get_solution)
