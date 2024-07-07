from fractions import Fraction

import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        #test adding integer list
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        #test adding fraction list
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
