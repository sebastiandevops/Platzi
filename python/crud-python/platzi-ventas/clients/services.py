#!/usr/bin/env python3

import csv
from clients.models import Client


class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writter = csv.DictWriter(f, fieldnames=Client.schema())
            writter.writerows(client.to_dict())
