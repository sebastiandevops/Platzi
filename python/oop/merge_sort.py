#!/usr/bin/env python3

import random


def merge_sort(lst):
    if len(lst) > 1:
        half = len(lst) // 2
        left = lst[:half]
        right = lst[half:]
        print(f"left: {left}, ***** right: {right}")
        # recursive call both sides
        merge_sort(left)
        merge_sort(right)
        # iterators for sublists
        i = 0
        j = 0
        # iterator for main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
        print(f"left: {left}, right: {right}")
        print(f"lst: {lst}")
        print('-' * 50)
    return lst


if __name__ == '__main__':
    lst_length = int(input('insert list length ==> '))

    lst = [random.randint(0, 100) for i in range(lst_length)]
    print(lst)
    print('_' * 20)
    sorted_list = merge_sort(lst)
    print(f"sorted_list ==> {sorted_list}")
