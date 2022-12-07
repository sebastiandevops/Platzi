#!/usr/bin/env python3

import random


def binary_search(lst, start, end, element):
    print(f'Searching for {element} between {lst[start]} and {lst[end - 1]}')
    if start > end:
        return False

    half = (start + end) // 2
    if lst[half] == element:
        return True
    elif lst[half] < element:
        return binary_search(lst, half + 1, end, element)
    else:
        return binary_search(lst, start, half - 1, element)


if __name__ == '__main__':
    lst_length = int(input('insert list length ==>'))
    element = int(input('insert element to search ==>'))

    lst = sorted([random.randint(0, 100) for i in range(lst_length)])
    finded = binary_search(lst, 0, len(lst), element)
    print(lst)
    print(f'The element {element} {"is" if finded else "is not"} in lst')
