from typing import List

from common import solve


def get_solution(input_lines: List[str]) -> List[str]:
    """
    Решает задачу выбора максимального количества непересекающихся лекций.
    """

    n = int(input_lines[0])

    # Создаем список пар (начало, конец) для каждой лекции
    lectures: List[tuple] = []

    for i in range(1, n + 1):
        start, end = map(int, input_lines[i].split())
        lectures.append((start, end))

    # Сортируем лекции по времени окончания
    lectures.sort(key=lambda x: x[1])

    # Инициализируем счетчик выбранных лекций и время окончания последней выбранной лекции
    count = 0
    last_end_time = -1

    # Проходим по отсортированным лекциям и выбираем непересекающиеся
    for lecture in lectures:
        start, end = lecture

        if start >= last_end_time:
            count += 1
            last_end_time = end

    return [str(count)]


solve(get_solution)
