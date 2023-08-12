#!/usr/bin/python3

# Importing specific functions from calculator_1.py
from calculator_1 import add, subtract, multiply, divide

# Define variables a and b
a = 10
b = 5

# Call each of the imported functions using the variables a and b
result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)

# Print the results
print("The sum of", a, "and", b, "is:", result_add)
print("The difference between", a, "and", b, "is:", result_subtract)
print("The product of", a, "and", b, "is:", result_multiply)
print("The division of", a, "by", b, "is:", result_divide)
