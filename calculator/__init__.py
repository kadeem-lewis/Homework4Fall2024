"Main calculator code"
from fractions import Fraction


def add(addend_one: Fraction, addend_two: Fraction) -> Fraction:
    """Add two numbers"""
    return addend_one + addend_two


def subtract(minuend: Fraction, subtrahend: Fraction) -> Fraction:
    """Subtract two numbers"""
    return minuend - subtrahend


def multiply(multiplier: Fraction, multiplicand: Fraction) -> Fraction:
    """Multiply two numbers"""
    return multiplier * multiplicand


def divide(dividend: Fraction, divisor: Fraction) -> Fraction:
    """Divide two numbers"""
    return dividend / divisor
