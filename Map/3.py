# Write a Python program to listify the list of given strings individually using Python map.

colors = ['Red', 'Blue', 'Black', 'White', 'Pink']

newList = list(map(lambda el: list(el), colors))

print(newList)
# [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]

#///////////////////////////////////////////////////////////////////////////////////////////

colors = ['Red', 'Blue', 'Black', 'White', 'Pink']

newList = list(map(list, colors))

print(newList)
# [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]