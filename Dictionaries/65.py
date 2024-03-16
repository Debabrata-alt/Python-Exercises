# Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key.
# Sample Output:
# Original list of dictionaries:
# [{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
# Convert a list of dictionaries into a list of values corresponding to the specified key:
# [18, 22, 20, 18]

myList = [{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]

l = list(el["age"] for el in myList)

print(l)
# [18, 22, 20, 18]

x = list(el.get("age") for el in myList)

print(x)
# [18, 22, 20, 18]