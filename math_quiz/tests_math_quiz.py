import unittest
from math_quiz import random_integer, random_operator, math_quiz_calculator


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if the selected operator is one of '+', '-', or '*'
        for _ in range(1000):  # Test a large number of random values
            operator = random_operator()
            self.assertIn(operator, {'+', '-', '*'})

    def test_math_quiz_calculator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (15, 5, '-', '15 - 5', 10),
                (20, 20, '*', '20 * 20', 400),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer= math_quiz_calculator(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
