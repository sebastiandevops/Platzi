#!/usr/bin/env python3

from node import Node

node1 = None
node2 = Node("A", None)
node3 = Node("B", node2)


def show_relations():
    """Script to show relationships between nodes."""
    print("### Memory allocation of nodes ###")
    print(f"node2: {node2}")
    print(f"node3: {node3}")

    print("### Node data and relationships ###")
    print(f"node2: {node2.data} ==> {node3.next}")
    print(f"node3: {node3.data} ==> {node3.next}")

    print("### The next node data ###")
    print(node3.next.data)

    print("### Node1 creation, node data and relationship with node3 ###")
    node1 = Node("C", node3)

    print(f"node1: {node1.data} ==> {node1.next}")


def create_nodes():
    """Script to creat nodes."""
    print("### Nodes intance that will be asigned "
          "to one value on memory: node2 ###")
    for node in range(5):
        head = Node(node, node2)
        print(f"head: {head.data} ==> {head.next}")


def run():
    show_relations()
    create_nodes()


if __name__ == '__main__':
    run()
