"""
17.3. Processing JSON results

json.dumps() takes a python object, typically a dictionary or a list, and returns a string, in JSON format.

It has a few other parameters. Two useful parameters are sort_keys and indent. When the value True is passed for the sort_keys parameter, the keys of dictionaries are output in alphabetic order with their values. The indent parameter expects an integer. When it is provided, dumps generates a string suitable for displaying to people, with newlines and indentation for nested lists or dictionaries. For example, the following function uses json.dumps to make a human-readable printout of a nested data structure.
"""
import json


def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2': {'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))
