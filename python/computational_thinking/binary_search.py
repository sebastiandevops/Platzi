#!/usr/bin/env python3

target = int(input('Choose a number: '))
epsilon = 0.01
lower = 0.0
greater = max(1.0, target)
answer = (lower + greater) / 2

while abs(answer ** 2 - target) >= epsilon:
    print(f"lower = {lower}, greater = {greater}, answer = {answer}")
    if answer ** 2 < target:
        lower = answer
    else:
        greater = answer

    answer = (greater + lower) / 2

print(f"{answer} is the square root of {target}.")
