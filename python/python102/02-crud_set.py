#!/usr/bin/env python3

set_countries = {'col', 'mex', 'bol'}
size = len(set_countries)
print(size)

print('col' in set_countries)

set_countries.add('per')
print(set_countries)
print('per' in set_countries)

# Update set
set_countries.update({'ar', 'ecu', 'per'})
print(set_countries)

# Remove element from set
set_countries.remove('col')
print(set_countries)

# Remove element witout error if not exists
set_countries.discard('arg')
print(set_countries)

set_countries.clear()
print(set_countries)
