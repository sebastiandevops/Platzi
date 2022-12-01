#!/usr/bin/env python3

import functools

numbers = list(range(1, 5))


def accum(counter, item):
    print(f"counter = {counter}")
    print(f"item = {item}")
    return counter + item


result = functools.reduce(accum, numbers)
print(f"result = {result}")
