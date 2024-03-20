# Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values:
# (('333', '33'), ('1416', '55'))
# New tuple values:
# ((333, 33), (1416, 55))

tuplex = (('333', '33'), ('1416', '55'))

l = tuple(tuple(int(e) for e in el) for el in tuplex)

print(l)
# ((333, 33), (1416, 55))

#///////////////////////////////////////////////////////////////////////////////////////////

tuplex = (('333', '33'), ('1416', '55'))

x = tuple((int(el[0]), int(el[1])) for el in tuplex)

print(x)
# ((333, 33), (1416, 55))