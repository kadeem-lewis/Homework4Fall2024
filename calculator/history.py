"""Module to hold the history of all calculations performed by the calculator."""

from typing import List
from calculator.calculation import Calculation


class History:
    """Class to hold the history of all calculations performed by the calculator."""

    history: List[Calculation] = []

    @classmethod
    def get_history(cls):
        """Return the history of all calculations."""
        return cls.history

    @classmethod
    def set_history(cls, history: List[Calculation]):
        """Set the history of all calculations."""
        cls.history.clear()
        cls.history.extend(history)

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def clear_history(cls):
        """Clear the history of all calculations."""
        cls.history.clear()

    @classmethod
    def get_last_calculation(cls):
        """Return the last calculation performed."""
        return cls.history[-1] if cls.history else None
