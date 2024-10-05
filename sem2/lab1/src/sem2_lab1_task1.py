from typing import List

from common import solve


def get_solution(input_data: List[str]) -> List[str]:
    """
    Решает задачу о дробном рюкзаке. Вычисляет максимальную стоимость предметов, которые можно поместить в рюкзак.
    """

    # Разбор первой строки для получения количества предметов и вместимости рюкзака
    first_line = input_data[0].strip().split()
    n = int(first_line[0])
    W = int(first_line[1])

    items = []

    # Считывание данных о каждом предмете
    for i in range(1, n + 1):
        p, w = map(int, input_data[i].strip().split())
        if w == 0:
            value_per_weight = 0
        else:
            value_per_weight = p / w
        items.append((value_per_weight, p, w))

    # Сортировка предметов по убыванию стоимости на единицу веса
    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0
    remaining_capacity = W

    # Выбор предметов для рюкзака
    for value_per_weight, p, w in items:
        if remaining_capacity == 0:
            break

        if w <= remaining_capacity:
            total_value += p
            remaining_capacity -= w
        else:
            fraction = remaining_capacity / w
            total_value += p * fraction
            remaining_capacity = 0

    # Форматирование результата с четырьмя знаками после запятой
    result = f"{total_value:.4f}"

    return [result]


if __name__ == "__main__":
    solve(get_solution)
