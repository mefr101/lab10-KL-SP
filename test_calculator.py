import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def log(a ,b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid base or argument for logarithm.")
    return math.log(b , a)

def exp(a, b):
    return a ** b

def subtract(a, b):
    return sub(a , b)

def multiply(a, b):
    return mul(a, b)

def logarithm(a, b):
    return log(a, b)

def eponent(a, b):
    return exp(a , b)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
