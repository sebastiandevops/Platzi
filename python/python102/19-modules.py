#!/usr/bin/env python3

import sys
print(sys.path)

import re
text = 'My telephone number is 3172933325, my '\
       'country code is 57 and my luck number is 3'

print(text)
result = re.findall('[0-9]+', text)
print(type(text))
print(f"result = {result}")

import time
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(f"result = {result}")
print(f"timestamp = {timestamp}")

import collections
numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
counter = collections.Counter(numbers)
print(f"counter = {counter}")
