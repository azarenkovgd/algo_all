from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    # Читаем количество элементов n из первой строки
    n = int(input_lines[0])

    # Преобразуем вторую строку в список целых чисел
    array = list(map(int, input_lines[1].split()))

    # Инициализируем массив для хранения новых позиций элементов
    positions = [0] * n

    # Начинаем сортировку вставками
    for i in range(n):
        key = array[i]  # Текущий элемент для вставки
        j = i - 1

        # Сохраняем текущий индекс элемента
        original_index = i

        # Перемещаем элементы, которые больше ключа, на одну позицию вперед

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]  # Сдвигаем элемент вправо
            j -= 1

        array[j + 1] = key  # Вставляем ключ на правильное место
        # Новая позиция элемента после вставки
        new_position = j + 1  # Индексы начинаются с 0
        positions[original_index] = new_position + 1  # Сохраняем новую позицию (с учетом индексации с 1)

    # Преобразуем список позиций и отсортированный массив в строки с пробелами
    positions_line = " ".join(map(str, positions))
    sorted_array_line = " ".join(map(str, array))

    # Возвращаем список строк для записи в output.txt
    return [positions_line, sorted_array_line]


solve(get_solution)
