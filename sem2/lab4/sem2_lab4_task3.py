from typing import List

from common import solve


def get_solution(input: List[str]) -> List[str]:
    """
    Реализует алгоритм Рабина-Карпа для поиска всех вхождений шаблона P в текст T.
    Возвращает количество вхождений и их начальные позиции.
    """

    # Извлечение паттерна P и текста T из входных данных
    P = input[0].rstrip("\n")
    T = input[1].rstrip("\n")

    len_P = len(P)
    len_T = len(T)

    # База и модуль для хеширования
    base = 256
    mod = 10**9 + 7

    # Предварительный расчет степени базы
    power = 1
    for _ in range(len_P - 1):
        power = (power * base) % mod

    # Вычисление хеша паттерна
    hash_P = 0
    for char in P:
        hash_P = (hash_P * base + ord(char)) % mod

    # Вычисление начального хеша окна текста
    hash_T = 0

    for char in T[:len_P]:
        hash_T = (hash_T * base + ord(char)) % mod

    result_positions: List[int] = []

    # Сравнение хешей и проверка подстроки на совпадение
    for i in range(len_T - len_P + 1):
        # Если хеши совпадают, проверить подстроки символ за символом
        if hash_T == hash_P:
            if T[i : i + len_P] == P:
                result_positions.append(i + 1)  # Нумерация с 1

        # Вычисление хеша следующего окна текста
        if i < len_T - len_P:
            hash_T = (hash_T - ord(T[i]) * power) % mod
            hash_T = (hash_T * base + ord(T[i + len_P])) % mod
            hash_T = (hash_T + mod) % mod  # Обеспечить положительное значение

    # Формирование выходных данных
    count = len(result_positions)
    positions_str = " ".join(map(str, result_positions))

    return [str(count), positions_str]


solve(get_solution)
