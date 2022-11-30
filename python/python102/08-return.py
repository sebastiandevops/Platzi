#!/usr/bin/env python3
def sum_with_range(min, max):
    """
        min (): Min number of range elements
        max (): Max number of range elements
    """
    print(f"min = {min} | max = {max}")
    sum = 0
    for x in range(min, max):
        sum += x
    return (sum)


result = sum_with_range(20, 30)
print(f"result = {result}")

result2 = sum_with_range(result, result + 10)
print(f"result2 = {result2}")

result3 = sum_with_range(1, 10)
print(f"result3 = {result3}")
