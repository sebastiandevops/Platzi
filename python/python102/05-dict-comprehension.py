#!/usr/bin/env python3

import random
# dict = {}
# for i in range(1, 11):
#     dict[i] = i * 2

# print(dict)

# dict_v2 = {i: i * 2 for i in range(1, 11)}
# print(dict_v2)

# countries = ['col', 'mex', 'bol', 'per']

# population = {}

# for country in countries:
#     population[country] = random.randint(1, 100)

# print(population)
# population_v2 = {country: random.randint(1, 100) for country in countries}

# print("population_v2: {}".format(population_v2))

names = ['Nico', 'Zule', 'Santi']
ages = [12, 56, 98]

print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print("new_dict: {}".format(new_dict))

new_dict_v2 = {names[i]: ages[i] for i in range(len(names))}
print("new_dict_v2: {}".format(new_dict_v2))

new_dict_v3 = dict(zip(names, ages))
print("new_dict_v3: {}".format(new_dict_v3))
