from typing import List

from common import solve


def is_valid(sequence: str) -> bool:
    """
    Проверяет, является ли данная последовательность скобок правильной.
    """

    stack = []
    bracket_map = {")": "(", "]": "["}

    for char in sequence:
        if char in bracket_map.values():
            # Если символ открывающей скобки, добавляем его в стек
            stack.append(char)

        elif char in bracket_map:
            # Если символ закрывающей скобки, проверяем соответствие
            if not stack:
                return False

            top = stack.pop()

            if bracket_map[char] != top:
                return False

        else:
            # Если символ не скобка, игнорируем (по условию такие не встречаются)
            pass

    # Если стек пуст, все скобки сбалансированы
    return not stack


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Функция проверяет каждую скобочную последовательность из входного списка и возвращает список "YES" или "NO" в зависимости от того, является ли последовательность правильной.
    """

    results = []

    n = int(input_lines[0])

    for i in range(1, n + 1):
        sequence = input_lines[i].strip()

        if is_valid(sequence):
            results.append("YES")
        else:
            results.append("NO")

    return results


solve(get_solution)
