#!/usr/bin/env python3

import random


def insertion_sort(lst):
    index = len(lst)
    count = 0

    for index in range(1, len(lst)):
        count += 1
        value = lst[index]
        position = index

        while position > 0 and lst[position - 1] > value:
            lst[position] = lst[position - 1]
            position -= 1

        lst[position] = value
    print(f'It takes {count} iterations to sort the list')
    return lst


if __name__ == '__main__':
    lst_length = int(input('insert list length ==>'))

    lst = [random.randint(0, 100) for i in range(lst_length)]
    print(lst)
    sorted_list = insertion_sort(lst)
    print(f"sorted_list ==> {sorted_list}")
