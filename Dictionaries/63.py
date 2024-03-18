# Write a Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list.
# Sample Output:
# Russell
# 2

from functools import reduce
from operator import getitem

users = {
    'Carla': {
        'name': {
            'first': 'Carla ',
            'last': 'Russell'
        },
        'postIds': [1, 2, 3, 4, 5]
    }
}

def func(d, selectors):
    # Use 'reduce' to successively apply 'getitem' with each element in 'selectors' on the dictionary 'd'.
    # This effectively drills down into the dictionary using the sequence of selectors.
    # NOTE: getitem() is same as a[b].
    return reduce(getitem, selectors, d)


print(func(users, ['Carla', 'name', 'last'])) # Russell
print(func(users, ['Carla', 'postIds', 1])) # 2
