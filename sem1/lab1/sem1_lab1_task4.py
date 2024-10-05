from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Функция выполняет линейный поиск значения V в массиве чисел
    """

    # Парсим первую строку в массив чисел
    numbers = list(map(int, input_lines[0].split()))

    # Парсим значение V из второй строки
    V = int(input_lines[1].strip())

    # Инициализируем список индексов, где найдено значение V
    indices = []

    # Проходим по массиву чисел и ищем V
    for i, num in enumerate(numbers):
        if num == V:
            indices.append(i + 1)  # Индексы начинаются с 1

    # Если значение V не найдено
    if not indices:
        return ["-1"]

    # Если значение V найдено один раз
    if len(indices) == 1:
        return [str(indices[0])]

    # Если значение V найдено несколько раз
    result = f"Number occurs {len(indices)} times at indices: {','.join(map(str, indices))}"

    return [str(indices[0]), " ".join(map(str, indices))]


solve(get_solution)
