#!/usr/bin/env python3

import random


def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == '__main__':
    lst_length = int(input('insert list length ==>'))

    lst = [random.randint(0, 100) for i in range(lst_length)]
    print(lst)
    sorted_list = bubble_sort(lst)
    print(f"sorted_list ==> {sorted_list}")
