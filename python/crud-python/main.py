#!/usr/bin/env python3

clients = 'Pablo,Ricardo'


def create_client(client_name):
    """Function to create clients

    Args:
        client_name (str): Client name of the client to create
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
    """ Function to update client name

    Args:
        client_name (str): Old name of the client to update.
        updated_name (str): New name of the client.
    """
    global clients
    if client_name in clients:
        clients = clients.replace(client_name, updated_name)
    else:
        print('Client is not in client\'s list')


def delete_client(client_name):
    """ Function to delete client.

    Args:
        client_name (str): Client to delete.
    """
    global clients
    if client_name in clients:
        clients = clients.replace(client_name, "")
    else:
        print("Client is not in client\'s list")


def search_client(client_name):
    """Function to search for client in clients list.

    Args:
        client_name (str): Client name to search for.

    Returns: True if client is found, False otherwise.

    """
    clients_list = clients.split(',')
    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    """ Function to print welcome message """
    print("Welcome to Platzi Ventas")
    print("*" * 50)
    print("What would you like to do today?")
    print("[C]reate client")
    print("[L]ist clients")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")


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
    elif command == "L":
        list_clients()
    elif command == "D":
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == "U":
        client_name = _get_client_name()
        updated_name = input("Insert the new name: ")
        update_client(client_name, updated_name)
        list_clients()
    elif command == "S":
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print("The client is in the client\'s list")
        else:
            print(f'{client_name} is not in our client\'s list.')
    else:
        print("Invalid command")
