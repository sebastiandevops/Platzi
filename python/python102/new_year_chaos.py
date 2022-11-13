#!/usr/bin/env python3

import pdb


def minimumBribes(q):
    # Write your code here

    c = 0
    my_index = 1
    bribes = 0
    for i in q:
        if abs(i - my_index) > 2:
            print("Too chaotic")
            return
        else:
            if (i - my_index) > 0:
                bribes += i - my_index
            c += 1
            my_index += 1
    print(bribes)


if __name__ == '__main__':
    # pdb.set_trace()
    q = [2, 1, 5, 3, 4]
    r = [2, 5, 1, 3, 4]
    minimumBribes(q)
    minimumBribes(r)
