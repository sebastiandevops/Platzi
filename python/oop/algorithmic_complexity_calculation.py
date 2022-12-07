#!/usr/bin/env python3

import math


def num(n):
    return 1


def logarithm(n):
    return math.log10(n)


def lineal(n):
    return n


def n_logarithm(n):
    return n * math.log10(n)


def square(n):
    return n**2


def exponential(n):
    return 2**n


if __name__ == "__main__":
    n = [10, 100, 1000, 1000000]
    i = 0
    for numbers in n:
        print(num(n[i]))
        print(logarithm(n[i]))
        print(lineal(n[i]))
        print(n_logarithm(n[i]))
        print(square(n[i]))
        print(exponential(n[i]))
        print('\n')
        i += 1
