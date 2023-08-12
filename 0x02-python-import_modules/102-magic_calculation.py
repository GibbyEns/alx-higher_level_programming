#!/usr/bin/python3

import dis

def my_function(a, b):
    return a + b * 2

# Disassemble the function and print the bytecode
dis.dis(my_function)
