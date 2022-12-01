#!/usr/bin/env python3

def increment(x):
    return x + 1


increment_v2 = lambda x: x + 1


def high_order_func(x, func):
    return x + func(x)


high_order_func_v2 = lambda x, func: x + func(x)

result1 = high_order_func_v2(2, increment_v2)
print(f"result1 = {result1}")

result2 = high_order_func_v2(2, lambda x: x * 2)
print(f"result2 = {result2}")

result3 = high_order_func_v2(2, lambda x: x ** 2)
print(f"result3 = {result3}")
