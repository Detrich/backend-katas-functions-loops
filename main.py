#!/usr/bin/env python3
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Detrich"


def add(x, y):
    """Add two integers. Handles negative values."""
    return x + y



def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    sum = 0
    for i in range(x):
        sum = add(sum, y)
    return sum




def power(x, n):
    """Raise x to power n, where n >= 0"""
    sum = x
    for i in range(n-1):
        sum = multiply(sum, x)
    return sum



def factorial(x):
    """Compute factorial of x, where x > 0"""
    if (x == 0 or x == 1):
        return 1
    for i in range(1 ,x):
        x = multiply(x , i)
    return x



def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    x = [0,1]
    for i in range(2,n+1):
        x.append(add(x[i-2], x[i-1]))
    return x[n-1]


if __name__ == '__main__':
    print(add(2,4))
    print(multiply(6,-8))
    print(power(2, 8))
    print(factorial(4))
    print(fibonacci(8))
