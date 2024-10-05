from common import solve


def get_solution(input_lines: list[str]) -> list[str]:
    """
    Задача: Реализовать множество с операциями добавления, удаления и проверки существования элемента.
    На вход поступает список строк с командами, на выходе список ответов для операций проверки (команда '?').
    """

    key_set = set()

    result = []

    for line in input_lines[1:]:

        operation, value_str = line.split()

        value = int(value_str)

        if operation == "A":
            key_set.add(value)

        elif operation == "D":
            key_set.discard(value)

        elif operation == "?":
            if value in key_set:
                result.append("Y")
            else:
                result.append("N")

    return result


solve(get_solution)
