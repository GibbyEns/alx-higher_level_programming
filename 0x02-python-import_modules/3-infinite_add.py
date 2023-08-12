#!/usr/bin/python3

import sys

def add_arguments(arguments):
    result = 0
    for arg in arguments:
        result += int(arg)
    return result

if __name__ == "__main__":
    # Get all command-line arguments except the script name (sys.argv[0])
    arguments = sys.argv[1:]

    # Call the function to add the arguments
    result = add_arguments(arguments)

    # Print the result followed by a new line
    print(result)

