#!/usr/bin/env python3

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    n = int(input('Write a number: '))
    print(fibonacci(n))
