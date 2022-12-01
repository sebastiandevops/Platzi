#!/usr/bin/env python3

def increment(x):
    return x + 1


increment_v2 = lambda x: x + 1

result = increment(10)
print(11)

result = increment_v2(20)
print(result)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'
text = full_name('sebastián', 'valencia sierra')
print(text)
