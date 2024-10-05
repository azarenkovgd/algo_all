import unittest

from sem2.lab1.src.sem2_lab1_task1 import get_solution


class Sem2Lab1Task1Tests(unittest.TestCase):
    def test_first_case(self):
        self.assertEqual(get_solution(["3 50", "60 20", "100 50", "120 30"]), ["180.0000"])

    def test_second_case(self):
        self.assertEqual(get_solution(["1 10", "500 30"]), ["166.6667"])


if __name__ == "__main__":
    unittest.main(argv=["_"])
