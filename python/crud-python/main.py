#!/usr/bin/env python3

clients = 'Pablo,Ricardo'


def create_client(client_name):
    """Function to create clients

    Args:
        client_name (): string name of the client to create
    """
    global clients
    if client_name not in clients:
        clients += ',' + client_name
    else:
        print("Client already in the client\'s list")


def list_clients():
    """ Function to list clients """
    print(clients)


def update_client(client_name, updated_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name, updated_name)
    else:
        print('Client is not in client\'s list')


def _print_welcome():
    """ Function to print welcome message """
    print("Welcome to Platzi Ventas")
    print("*" * 50)
    print("What would you like to do today?")
    print("[C]reate client")
    print("[D]elete client")
    print("[U]pdate client")


def _get_client_name():
    """Function to get client name from user input

    Returns: client_name input

    """
    return input('Insert the client name: ')


if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == "D":
        pass
    elif command == "U":
        client_name = _get_client_name()
        updated_name = input("Insert the new name: ")
        update_client(client_name, updated_name)
        list_clients()
    else:
        print("Invalid command")
