import json
from pprint import pprint
from textwrap import indent
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
# print(json.dumps(my_mapping, indent=3, sort_keys = True))

pprint(my_mapping)
print(my_mapping)

# Note this only works with dicts containing
# primitive types (check out the "pprint" module)
