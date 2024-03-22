# Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

myList = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

x = sorted(myList, key=lambda el: el["color"])

print(x)
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]

y = sorted(myList, key=lambda el: el["make"])

print(y)
# [{'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

z = sorted(myList, key=lambda el: el["model"])

print(z)
# [{'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Nokia', 'model': 216, 'color': 'Black'}]