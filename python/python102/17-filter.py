#!/usr/bin/env python3

numbers = list(range(1, 6))
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"new_numbers = {new_numbers}")
print(f"numbers = {numbers}")
