# https://github.com/mefr101/lab10-KL-SP
# Partner 1: KL
# Partner 2: SP

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    # Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(-4, -6), -10)

    def test_subtract(self):
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(-5, -3), -2)
        self.assertEqual(sub(0, 7), -7)

    # Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(10, 100), 2.0)
        self.assertAlmostEqual(log(5, 1), 0.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)


if __name__ == "__main__":
    unittest.main()
