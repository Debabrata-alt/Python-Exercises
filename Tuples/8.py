# Write a Python program to create the colon of a tuple.

tuplex = ("HELLO", 5, [], True)

listx = list(tuplex)

listx[2].append(50)

tuplex = tuple(listx)

print(tuplex) # ('HELLO', 5, [50], True)