# https://github.com/mefr101/lab10-KL-SP
# Partner 1: KL
# Partner 2: SP

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid base or argument for logarithm.")
    return math.log(b, a)


def exponent(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


# Compatibility aliases
sub = subtract
mul = multiply
div = divide
log = logarithm
exp = exponent
