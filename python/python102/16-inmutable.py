#!/usr/bin/env python3

items = [{'product': 'camisa',
          'price': 100},
         {'product': 'pantalones',
          'price': 300},
         {'product': 'pantalones 2',
          'price': 200}]

prices = list(map(lambda item: item['price'], items))
print(f"prices = {prices}")


def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item


new_items = list(map(add_taxes, items))

print(f"new_items = {new_items}")
print(f"old_items = {items}")
