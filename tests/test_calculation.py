from fractions import Fraction
from calculator import Calculation
from calculator.operations import add


def test_calculation():
    """Test that calculation calculate function works"""
    assert Calculation(Fraction(2), Fraction(2), add).calculate() == Fraction(4)


def test_calculation_repr():
    """Test that calculation repr function works"""
    assert repr(Calculation(Fraction(2), Fraction(2), add)) == "Calculation(2, 2, add)"
