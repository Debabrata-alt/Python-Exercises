# Write a Python program to access only unique key value of a Python object.

import json

json_str = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'

py_obj = json.loads(json_str)

print(py_obj)
# {'a': 4, 'b': 2}

# NOTE: All duplicate "a"s got removed from the above result. why? Because dictionaries do not allow duplicate keys. 