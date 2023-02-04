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


def _print_welcome():
    print("Welcome to Platzi Ventas")
    print("*" * 50)
    print("What would you like to do today?")
    print("[C]reate client")
    print("[D]elete client")


if __name__ == '__main__':
    _print_welcome()
    command = input()

    if command == 'C':
        client_name = input("Which is the client name? ")
        create_client(client_name)
        list_clients()
    elif command == "D":
        pass
    else:
        print("Invalid command")
