# Write a Python program to find the length of a dictionary of values.

myDict1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

l = {v: len(v) for v in myDict1.values()}

print(l)
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}

#///////////////////////////////

l = dict([v, len(v)] for v in myDict1.values())

print(l) 
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}

#///////////////////////////////

l = dict((v, len(v)) for v in myDict1.values())

print(l) 
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}

#///////////////////////////////////////////////////////////////////////////////////////////

myDict2 = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

l = {v: len(v) for v in myDict2.values()}
print(l)
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}

l = dict([v, len(v)] for v in myDict2.values())
print(l)
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}

l = dict((v, len(v)) for v in myDict2.values())
print(l)
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}