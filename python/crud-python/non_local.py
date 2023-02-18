#!/usr/bin/env python3

x = 0


def outer():
    x = 1

    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


if __name__ == "__main__":
    outer()
    print("global:", x)
