import unittest


def add_numbers(first_number, second_number):
    return first_number + second_number


def is_even(number):
    return number % 2 == 0


def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list")
    return sum(numbers) / len(numbers)


class TestMathFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    # TODO: Add tests for negative numbers and zero.
    # TODO: Add tests for is_even() and calculate_average().


if __name__ == "__main__":
    unittest.main()
