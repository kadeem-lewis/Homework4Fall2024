# Project Install Instructions

## Install

1. clone
2. `pip3 install -r requirements.txt`

## Testing

```bash
pytest # Runs the tests without pylint or coverage
pytest --pylint # Runs tests with pylint static code analysis
pytest --pylint --cov # Runs tests, pylint, and coverage to check if you have all your code tested.

```


## The objective of this homework assignment is to create your own 

Your goal in this homeowrk is to design your own calculator from scratch using the techniuqes that you can figure out based on my examples.  Your calculator needs to do the following:

- [x] Add, Subtract, Multiply, and Divide
- [x] Throw exception for divide by zero and test that the exception is thrown
- [x] Use at least one class, at least one static method, at least one class method.
- [x] It needs to  store a history of calculations, so that you can retrieve the last calculation, add a calculation, 
- [x] It needs to have 100% test coverage, pass pylint, and you need to do your best to not repeat any lines of code.  
- [x]  You should use type hints for input parameter types and return types.
- [x]  Implement a pytest fixture to test the 

## Grading:

- [x]  20  Points for (add subtract, multiply, divide) 
- [x]  10 Points for exception throwing and testing on divide by zero
- [x]  30 points each for using static, class, and instance methods correctly
- [x]  5 Points for having a calculation class that stores the arithmetic operation in a instance property.
- [x]  15 Points for having a calculation history to store calculation instances
- [x]  10 Points for having the convenience methods on the calculations class to manage the history
- [x]  10 Points for using parameterized test data