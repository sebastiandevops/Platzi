#!/usr/bin/env python3

file = open('./text.txt')
# print(file.readlines())
# print(file.readline())

for line in file:
    print(line, end='')
file.close()

with open('./text.txt') as file:
    for line in file:
        print(line, end='')
