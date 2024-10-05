from typing import List

from common import solve


def get_solution(input_data: List[str]) -> List[str]:
    """
    Реализует менеджер телефонной книги, который обрабатывает команды добавления, удаления и поиска номеров.
    """

    phone_book = {}
    results = []

    n = int(input_data[0])

    for i in range(1, n + 1):
        parts = input_data[i].split()
        command = parts[0]

        if command == "add":
            number = parts[1]
            name = parts[2]

            phone_book[number] = name

        elif command == "del":
            number = parts[1]

            phone_book.pop(number, None)

        elif command == "find":
            number = parts[1]

            result = phone_book.get(number, "not found")
            results.append(result)

    return results


solve(get_solution)
