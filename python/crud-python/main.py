#!/usr/bin/env python3

import os
import csv

CLIENT_TABLE = '/home/sebastian/estudio/Platzi/python/crud-python/.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writter = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writter.writerows(clients)
    os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)


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
    print(' uid |     name    |   company   |    email    |    position  ')
    print('*' * 60)

    for idx, client in enumerate(clients):
        print("{uid} | {name} | {company} | {email} | {position}".format(
            uid=idx,
            name=client["name"],
            company=client["company"],
            email=client["email"],
            position=client["position"]))


def update_client(client_id, updated_client):
    """ Function to update client name

    Args:
        client_name (str): Old name of the client to update.
        updated_client (str): New name of the client.
    """
    global clients
    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client is not in client\'s list')


def delete_client(client_id):
    """ Function to delete client.

    Args:
        client_name (str): Client to delete.
    """
    global clients
    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break


def search_client(client_name):
    """Function to search for client in clients list.

    Args:
        client_name (str): Client name to search for.

    Returns: True if client is found, False otherwise.

    """
    global clients
    for client in clients:
        if client['name'] != client_name:
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


def _get_client_from_user():
    """Function to get client name from user input

    Returns: client_name input

    """
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    return client


if __name__ == '__main__':
    _initialize_clients_from_storage()

    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
    elif command == "L":
        list_clients()
    elif command == "D":
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
    elif command == "U":
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
    elif command == "S":
        client_name = _get_client_field('name')
        found = search_client(client_name)
        if found:
            print("The client is in the client\'s list")
        else:
            print(f'{client_name} is not in our client\'s list.')
    else:
        print("Invalid command")

    _save_clients_to_storage()
