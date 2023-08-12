#!/usr/bin/python3

import sys
from calculator_1 import add, subtract, multiply, divide

def my_calculator(a, operator, b):
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = subtract(a, b)
    elif operator == '*':
        result = multiply(a, b)
    elif operator == '/':
        result = divide(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    return result

if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Parse command-line arguments
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Call the calculator function
    result = my_calculator(a, operator, b)

    # Print the result
    print(f"{a} {operator} {b} = {result}")

