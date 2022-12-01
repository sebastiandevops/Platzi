#!/usr/bin/env python3

price = 100  # global within file


def increment_price():
    price = 200
    result = price + 10
    print(result)
    return result


print(f"price: {price}")
price2 = increment_price()
print(f"price2: {price2}")
