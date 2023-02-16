#!/usr/bin/env python3

import sys

clients = [
    {
        "name": "Pablo",
        "company": "Google",
        "email": "pablo@google.com",
        "position": "Software engineer",
    },
    {
        "name": "Ricardo",
        "company": "Facebook",
        "email": "ricardo@facebook.com",
        "position": "Data Engineer",
    }
]


def create_client(client):
    """Function to create clients

    Args:
        client_name (str): Client name of the client to create
    """
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print("Client already in the client\'s list")


def list_clients():
    """ Function to list clients """
    for idx, client in enumerate(clients):
        print("{uid} | {name} | {email} | {position}".format(
            uid=idx,
            name=client["name"],
            company=client["company"],
            email=client["email"],
            position=client["position"]))


def update_client(client_name, updated_name):
    """ Function to update client name

    Args:
        client_name (str): Old name of the client to update.
        updated_name (str): New name of the client.
    """
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name
    else:
        print('Client is not in client\'s list')


def delete_client(client_name):
    """ Function to delete client.

    Args:
        client_name (str): Client to delete.
    """
    global clients
    if client_name in clients:
        clients.remove(client_name)
    else:
        print("Client is not in client\'s list")


def search_client(client_name):
    """Function to search for client in clients list.

    Args:
        client_name (str): Client name to search for.

    Returns: True if client is found, False otherwise.

    """
    global clients
    for client in clients:
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


def _get_client_field(field_name):
    """

    Args:
        field_name (str): user input to fill values.

    Returns: field filled

    """
    field = None
    while not field:
        field = input(f'Insert the client {field_name}: ')
    return field


def _get_client_name():
    """Function to get client name from user input

    Returns: client_name input

    """
    client_name = None
    while not client_name:
        client_name = input('Insert the client name: ')
        if client_name == 'exit':
            client_name = None
            break
    if not client_name:
        sys.exit()
    return client_name


if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            "name": _get_client_field("name"),
            "company": _get_client_field("company"),
            "email": _get_client_field("email"),
            "position": _get_client_field("position"),
        }
        create_client(client)
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
