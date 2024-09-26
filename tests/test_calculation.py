from fractions import Fraction
import pytest
from calculator import Calculation
from calculator.operations import add, subtract, divide, multiply


@pytest.mark.parametrize(
    "var_one, var_two, operation, expected",
    [
        (Fraction(10), Fraction(5), add, Fraction(15)),
        (Fraction(10), Fraction(5), subtract, Fraction(5)),
        (Fraction(10), Fraction(5), multiply, Fraction(50)),
        (Fraction(10), Fraction(5), divide, Fraction(2)),
        (Fraction(3.25), Fraction(3.25), add, Fraction(6.5)),
        (Fraction(3.25), Fraction(3.25), subtract, Fraction(0)),
        (Fraction(3.25), Fraction(3.25), multiply, Fraction(10.5625)),
        (Fraction(12), Fraction(5), divide, Fraction(12, 5)),
    ],
)
def test_calculation(var_one, var_two, operation, expected):
    """Test that calculation calculate function works"""
    assert Calculation(var_one, var_two, operation).calculate() == expected


def test_calculation_repr():
    """Test that calculation repr function works"""
    assert repr(Calculation(Fraction(2), Fraction(2), add)) == "Calculation(2, 2, add)"
