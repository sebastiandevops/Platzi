#!/usr/bin/env python3

from contextlib import contextmanager


class File(object):
    def __init__(self, filename, method):
        self.file_obj = open(filename, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print('Exception has been handled')
        self.file_obj.close()
        return True


@contextmanager
def open_file(name):
    f = open(name)
    try:
        yield f
    finally:
        f.close()


if __name__ == '__main__':
    print('\n******** Write object example **********\n')
    with File('./test.txt', 'w') as opened_file:
        opened_file.write('Hello!')
    print('\n****** Handle exception example ********\n')
    with File('./test.txt', 'w') as opened_file:
        opened_file.undefined_function('Hello!')
    print('\n******* @contextmanager example ********\n')
    with open_file('./test.txt') as f:
        f.read()
