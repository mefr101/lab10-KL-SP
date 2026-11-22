# https://github.com/mefr101/lab10-KL-SP
# Partner 1: Kanu Lala
# Partner 2: Stephen Passetti

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

    # Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(-4, -6), 24)

    def test_divide(self):
        self.assertEqual(divide(2, 4), 2)
        self.assertEqual(divide(-1, 5), -5)
        self.assertEqual(divide(-4, 8), -2)

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

    # Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, -12), 13)
        self.assertEqual(hypotenuse(-6, -8), 10)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)


if __name__ == "__main__":
    unittest.main()
