#!/usr/bin/env python3

import random


def lineal_search(lst, element):
    match = False

    for elem in lst:
        if elem == element:
            match = True
            break
    return match


if __name__ == '__main__':
    lst_length = int(input('insert list length ==>'))
    element = int(input('insert element to search ==>'))

    lst = [random.randint(0, 100) for i in range(lst_length)]
    finded = lineal_search(lst, element)
    print(lst)
    print(f'The element {element} {"is" if finded else "is not"} in lst')
