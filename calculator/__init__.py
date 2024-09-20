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


class Calculator:
    """Class responsible for the calculator operations"""

    @staticmethod
    def add(var_one: Fraction, var_two: Fraction) -> Fraction:
        """Add two numbers"""
        return add(var_one, var_two)

    @staticmethod
    def subtract(minuend: Fraction, subtrahend: Fraction) -> Fraction:
        """Subtract two numbers"""
        return subtract(minuend, subtrahend)

    @staticmethod
    def multiply(multiplier: Fraction, multiplicand: Fraction) -> Fraction:
        """Multiply two numbers"""
        return multiply(multiplier, multiplicand)

    @staticmethod
    def divide(dividend: Fraction, divisor: Fraction) -> Fraction:
        """Divide two numbers"""
        return divide(dividend, divisor)


# Calculator is high level so it will need to have the operations in them so you can call Calculator.add() etc
# Each operation will call the static factory method in the Calculation class along with one of the operations
# The Calculation class needs to store the variables and operation because it needs to get added to history
# Operations stored the basic functions for arithmetic operations
# Calculation will
