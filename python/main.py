#!/usr/bin/env python3

import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def csv_reader(file_name):
    for row in open(os.path.join(__location__, "techcrunch.csv")):
        yield row


if __name__ == "__main__":
    csv_gen = csv_reader("./techcrunch.csv")
    row_count = 0

    for row in csv_gen:
        row_count += 1

    print(f"Row count is {row_count}")
