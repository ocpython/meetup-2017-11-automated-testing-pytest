from cannibal_numbers.cannibal_numbers import cannibal_calculator

import unittest


class TestCannibalNumbers(unittest.TestCase):

    def test_known_data_set(self):
        numbers = [21, 9, 5, 8, 10, 1, 3]
        queries = [10, 15]

        results = cannibal_calculator(numbers, queries)

        self.assertEquals(results, {10: 4, 15: 2})

    def test_duplicate_numbers(self):
        numbers = [3, 3, 3, 2, 2, 2, 1, 1, 1]
        queries = [4]

        results = cannibal_calculator(numbers, queries)

        self.assertEquals(results, {4: 4})

    def test_all_identical_integer(self):
        numbers = [3, 3, 3, 3]
        queries = [4]

        results = cannibal_calculator(numbers, queries)

        self.assertEquals(results, {4: 0})

    def test_number_not_consumed_more_than_once(self):
        numbers = [1, 2, 3, 4]
        queries = [5]

        results = cannibal_calculator(numbers, queries)

        self.assertEquals(results, {5: 1})


if __name__ == '__main__':
    unittest.main()
