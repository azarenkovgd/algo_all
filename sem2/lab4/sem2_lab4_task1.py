from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Находит все вхождения строки p в строку t и возвращает количество вхождений и их позиции.
    """
    p: str = input_lines[0]
    t: str = input_lines[1]

    occurrences: List[int] = []
    p_length: int = len(p)
    t_length: int = len(t)

    # Проходим по строке t, чтобы найти все вхождения p
    for i in range(t_length - p_length + 1):

        # Проверяем, совпадает ли подстрока с p
        if t[i : i + p_length] == p:

            # Добавляем позицию (1-индексация) в список вхождений
            occurrences.append(i + 1)

    # Формируем результат: количество вхождений и их позиции
    count: int = len(occurrences)
    positions: str = " ".join(map(str, occurrences))

    return [str(count), positions]


solve(get_solution)
