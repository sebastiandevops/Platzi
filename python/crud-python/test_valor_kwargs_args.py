#!/usr/bin/env python3
PASSWORD = '12345'


def test_valor_kwargs_args(*args, **kwargs):
    print(type(kwargs))
    print(kwargs)
    print('-----------')
    print(type(args))
    print(args)


def test_valor_kwargs(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print('%s = %s' % (key, value))


def test_valor_arg(n_arg, *args):
    print('Primer valor normal: ', n_arg)

    for arg in args:
        print('este es un valor de *args: ', arg)
    print(type(args))


def require_password(func):
    def wrapper():
        password = input('Password: ')
        if password == PASSWORD:
            return func()
        else:
            print('Invalid password')
    return wrapper


@require_password
def needs_password():
    print('Password ok')


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@upper
def say_my_name(name):
    return 'Hola, {}'.format(name)


if __name__ == '__main__':
    # test_valor_kwargs_args('flash', 'batman',
    #                        caricatura='batman', empresa='dc')
    # print('\n*****************************\n')
    # test_valor_kwargs(caricatura='Aquaman')
    # print('\n*****************************\n')
    # test_valor_arg('carlos', 'karla', 'paola', 'Elena')
    print('\n*****************************\n')
    # needs_password()
    print(say_my_name("Sebastián"))
