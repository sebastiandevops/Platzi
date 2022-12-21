#!/usr/bin/env python3


class Node():
    """
    Attributes:
        data: node data.
        next: None by default. Reference to the next node.
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
