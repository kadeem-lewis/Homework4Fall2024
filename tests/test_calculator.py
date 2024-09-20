"""My Calculator Test"""

from fractions import Fraction
from calculator import add, subtract, divide, multiply


def test_addition():
    """Test that addition function works"""
    assert add(Fraction(2), Fraction(2)) == 4


def test_subtraction():
    """Test that addition function works"""
    assert subtract(Fraction(2), Fraction(2)) == 0


def test_division():
    """Test that addition function works"""
    assert divide(Fraction(2), Fraction(2)) == 1


def test_multiplication():
    """Test that addition function works"""
    assert multiply(Fraction(2), Fraction(2)) == 4
