#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    n (int): The integer number for which the factorial is calculated.

    Returns:
    int: The factorial of the number 'n'.
    """
    if n == 0:
        return 1  # Base case: the factorial of 0 is 1
    else:
        return n * factorial(n-1)  # Recursive case: multiply n by the factorial of n-1

# Read an integer from command line argument, calculate its factorial, and print it
f = factorial(int(sys.argv[1]))
print(f)

