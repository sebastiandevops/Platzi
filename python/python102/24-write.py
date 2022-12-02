#!/usr/bin/env python3

with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write("nuevas cosas en este archivo.\n")
    file.write("otra linea\n")
    file.write("Mas lineas\n")
