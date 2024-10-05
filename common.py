from typing import List, Callable


def solve(solver: Callable[[List[str]], List[str]]) -> None:
    with open("../../input.txt", "r") as file:
        lines = file.readlines()
        input_lines = list(map(lambda x: x.strip(), lines))

    output_lines = solver(input_lines)

    with open("../../output.txt", "w") as file:
        for line in output_lines:
            file.write(f"{line}\n")
