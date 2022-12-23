#!/usr/bin/env python3

from linked_list import SinglyLinkedList


def create_singly_linked_list():
    words = SinglyLinkedList()
    words.append('egg')
    words.append('ham')
    words.append('spam')
    current = words.tail

    print('### Single linked list data ###')
    while current:
        print(current.data)
        current = current.next

    print('### Iter method ###')
    for word in words.iter():
        print(word)

    print('### Search method ###')
    words.search('spam')

    print('### Clear method ###')
    words.clear()

    print('### Single linked list data ###')
    if current:
        print(current.data)
        current = current.next
    else:
        print("No data found")


def run():
    create_singly_linked_list()


if __name__ == '__main__':
    run()
