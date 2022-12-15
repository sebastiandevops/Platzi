#!/usr/bin/env python3
def factorial(n):
    """Gets n factorial
       n (int): int greater than 0
       returns n fact
    """
    print(f"n = {n}")
    if n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    n = int(input('Write an integer: '))
    print(factorial(n))
