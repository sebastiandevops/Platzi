#!/usr/bin/env python3

import random

countries = ['col', 'mex', 'bol', 'per']

# population = {}

# for country in countries:
#     population[country] = random.randint(1, 100)

# print(population)
population_v2 = {country: random.randint(1, 100) for country in countries}

print("population_v2: {}".format(population_v2))

result = {country: population for (country, population) in population_v2.items() if population > 50}
print(f"result: {result}")

text = 'Hola, soy Sebastián'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(f"unique: {unique}")

frequency = {c: text.count(c) for c in text if c in 'aeiou'}
print(f"frequency: {frequency}")
