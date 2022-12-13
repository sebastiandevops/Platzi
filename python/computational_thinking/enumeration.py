#!/usr/bin/env python3

target = int(input('Choose an integer: '))
answer = 0

while answer ** 2 < target:
    print(f"answer = {answer}")
    answer += 1

if answer ** 2 == target:
    print(f"The square root of {target} is {answer}")
else:
    print(f"{target} not has a square root.")
