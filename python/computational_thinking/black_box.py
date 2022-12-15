#!/usr/bin/env python3

import unittest


def my_sum(num_1, num_2):
    return num_1 + num_2


class BlackBoxTest(unittest.TestCase):

    def test_sum_two_positive_integers(self):
        num_1 = 10
        num_2 = 5

        result = my_sum(num_1, num_2)
        self.assertEqual(result, 15)

    def test_sum_two_negative_integers(self):
        num_1 = -10
        num_2 = -7

        result = my_sum(num_1, num_2)
        self.assertEqual(result, -17)


if __name__ == "__main__":
    unittest.main()
