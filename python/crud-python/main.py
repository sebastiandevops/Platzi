#!/usr/bin/env python3

clients = 'Pablo,Ricardo'


def create_client(client_name):
    """Function to create clients

    Args:
        client_name (): string name of the client to create
    """
    global clients
    clients += ',' + client_name


def list_clients():
    """ Function to list clients """
    global clients
    print(clients)


if __name__ == '__main__':
    list_clients()
    create_client("David")
    list_clients()
