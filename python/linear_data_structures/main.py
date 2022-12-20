#!/usr/bin/env python3

from cube import Cube


def cubeChallenge():
    cube = Cube(3, 3, 3)

    for row in range(cube.get_height()):
        for column in range(cube.get_width()):
            for box in range(cube.get_depth()):
                cube[row][column][box] = f'[row {row}, '\
                        f'col {column}, box {box}]'
    print(cube)


def run():
    cubeChallenge()


if __name__ == '__main__':
    run()
