#!/usr/bin/env python3

numbers = list(range(1, 5))

numbers_v2 = []

for i in numbers:
    numbers_v2.append(i * 2)

numbers_v3 = list(map(lambda i: i * 2, numbers))

print(f"numbers = {numbers}")
print(f"numbers_v2 = {numbers_v2}")
print(f"numbers_v3 = {numbers_v3}")

numbers_2 = list(range(5, 8))

print(f"numbers = {numbers}")
print(f"numbers_2 = {numbers_2}")
result = list(map(lambda x, y: x + y, numbers, numbers_2))
print(f"result = {result}")
