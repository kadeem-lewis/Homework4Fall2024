""" Main module to handle command line arguments and call the calculator module """

import sys
from fractions import Fraction
from calculator import Calculator


def calculate_and_print(a, b, operation_name):
    """Calculate the result of the operation and print the result"""
    operation_mappings = {
        "add": Calculator.add,
        "subtract": Calculator.subtract,
        "multiply": Calculator.multiply,
        "divide": Calculator.divide,
    }

    # Unified error handling for decimal conversion
    try:
        # if math.isnan(a) or math.isnan(b):
        #     raise TypeError(f"Invalid number input: {a} or {b} is not a valid number.")
        a_decimal, b_decimal = map(Fraction, [a, b])
        result = operation_mappings.get(
            operation_name
        )  # Use get to handle unknown operations
        if result:
            print(
                f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}"
            )
        else:
            print(f"Unknown operation: {operation_name}")
    except ValueError:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:  # Catch-all for unexpected errors
        print(f"An error occurred: {e}")


def main():
    """Main function to handle command line arguments"""
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)


if __name__ == "__main__":
    main()
