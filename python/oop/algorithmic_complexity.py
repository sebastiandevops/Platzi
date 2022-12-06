#!/usr/bin/env python3

import time
import sys


def factorial(n):
    response = 1

    while n > 1:
        response *= n
        n -= 1
    return response


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    n = 10000
    sys.setrecursionlimit(n + 10)

    startingTime = time.time()
    factorial(n)
    endTime = time.time()
    print(f"Execution time with bucle\t{endTime - startingTime}")

    startingTime = time.time()
    factorial_recursive(n)
    endTime = time.time()
    print(f"Excecution time with recursive\t{endTime - startingTime}")
