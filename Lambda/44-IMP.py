# Write a Python program to convert string elements to integers inside a given tuple using lambda.
# Original tuple values:
# (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
# New tuple values:
# ((233, 33), (1416, 55), (2345, 34))

tuplex = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

x = tuple(tuple(int(i) for i in tuple(filter(lambda e: e.isdigit(), el))) for el in tuplex)

print(x)
# ((233, 33), (1416, 55), (2345, 34))

#//////////////////////////////////////////////////////////////////////////////////////////

# Using map() function

tuplex = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

x = tuple(tuple(map(lambda i: int(i), tuple(filter(lambda e: e.isdigit(), el)))) for el in tuplex)

print(x)
# ((233, 33), (1416, 55), (2345, 34))

#/////////////////////////////////////////////////////////////////////////////////////////////

tuplex = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

x = tuple(map(lambda el: (int(el[0]), int(el[2])), tuplex))

print(x)
# ((233, 33), (1416, 55), (2345, 34))