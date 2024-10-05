import random
from typing import List

from sem1_lab3_task1 import randomized_quicksort


def generate_random_array(min_size: int = 10, max_size: int = 1000) -> List[int]:
    size = random.randint(min_size, max_size)
    arr = random.sample(range(-(10**9), 10**9), size)
    return arr


def test_randomized_quicksort(iterations: int = 100) -> None:
    for i in range(1, iterations + 1):
        arr = generate_random_array()

        arr_copy = arr.copy()

        randomized_quicksort(arr, 0, len(arr) - 1)

        expected = sorted(arr_copy)

        if arr != expected:
            print(f"Тест {i} не прошел.")
            print(f"Ожидалось: {expected}")
            print(f"Получено:  {arr}")
            return

    print("Все тесты прошли успешно!")


if __name__ == "__main__":
    test_randomized_quicksort()
