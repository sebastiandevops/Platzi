#!/usr/bin/env python3


try:
    print(0 / 0)
    assert 1 != 1, 'Uno no es igual que uno'
    age = 10
    if age < 18:
        raise Exception('No se permite menores de edad')
except AssertionError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
except Exception as error:
    print(error)

print('Hola2')

print('Hola')
