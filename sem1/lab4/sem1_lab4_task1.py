from typing import List

from common import solve


def get_solution(commands: List[str]) -> List[str]:
    """
    Функция реализует работу стека.
    Принимает массив строк с командами и возвращает массив строк с результатами операций извлечения.
    """

    stack = []
    results = []

    for command in commands[1:]:
        if command.startswith("+"):
            # Извлекаем число из команды и добавляем его в стек
            _, num_str = command.split()
            num = int(num_str)
            stack.append(num)

        elif command == "-":
            # Извлекаем верхний элемент из стека и добавляем его в результаты
            popped = stack.pop()
            results.append(str(popped))

    return results


solve(get_solution)
