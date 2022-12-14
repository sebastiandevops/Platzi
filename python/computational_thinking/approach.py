#!/usr/bin/env python3

target = int(input('Choose a number: '))
epsilon = 0.01
step = epsilon ** 2
answer = 0.0

while abs((answer ** 2) - target) >= epsilon and answer <= target:
    print(f"Epsilon = {abs((answer ** 2) - target)}, answer = {answer}")
    answer += step

if abs((answer ** 2) - target) >= epsilon:
    print(f"Could not find {target} square root.")
else:
    print(f"{target} square root is {answer}")
