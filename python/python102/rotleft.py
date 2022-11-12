#!/usr/bin/env python3
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d


def rotLeft(a, d):
    # Write your code here
    return a[d:] + a[:d]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    d = 4
    print(*rotLeft(a, d))
