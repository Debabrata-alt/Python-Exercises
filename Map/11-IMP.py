# Write a Python program to split a given dictionary of lists into list of dictionaries using the map function.

myDict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

def myFunc(myDict):
  result = map(dict, zip(*[[(key, val) for val in value] for key, value in myDict.items()]))
  return list(result)

print(myFunc(myDict))
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

#////////////////////////////////////////////////////////////////////////////////////////////

# Explanation of the above code:

myDict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

myList = [[(key, val) for val in value] for key, value in myDict.items()]

print(myList)
# [[('Science', 88), ('Science', 89), ('Science', 62), ('Science', 95)], [('Language', 77), ('Language', 78), ('Language', 84), ('Language', 80)]]

# NOTE: 'myList' is a list of sublists. Each sublist is a list of tuples.
zipList = list(zip(*myList))

print(zipList)
# [(('Science', 88), ('Language', 77)), (('Science', 89), ('Language', 78)), (('Science', 62), ('Language', 84)), (('Science', 95), ('Language', 80))]

myMap = map(dict, zipList)

result = list(myMap)

print(result)
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

#/////////////////////////////////////////////////////////////////////////////////////////////
# NOTE:

l = dict((('Science', 88), ('Language', 77)))

print(l) 
# {'Science': 88, 'Language': 77}

p = dict(('Science', 88))

print(p)
# ValueError: dictionary update sequence element #0 has length 7; 2 is required

v = dict((('Science', 88),))

print(v)
# {'Science': 88}

x = dict('Science', 88)

print(x)
# TypeError: dict expected at most 1 argument, got 2

y = dict(Science = 88)

print(y)
# {'Science': 88}

z = dict(Science = 88, language = 77)

print(z)
# {'Science': 88, 'language': 77}

#//////////////////////////////////////////////////

x = dict('Science', 88)

print(x)
# TypeError: dict expected at most 1 argument, got 2

z = dict(Science = 88, language = 77)

print(z)
# {'Science': 88, 'language': 77}

a = dict([("Raju", 40), ("Avanti", 6), ("Pinku", 32)])

print(a)
# {'Raju': 40, 'Avanti': 6, 'Pinku': 32}

w = dict((("Raju", 40), ("Avanti", 6), ("Pinku", 32)))

print(w)
# {'Raju': 40, 'Avanti': 6, 'Pinku': 32}

b = dict([["Raju", 40], ["Avanti", 6], ["Pinku", 32]])

print(b)
# {'Raju': 40, 'Avanti': 6, 'Pinku': 32}

m = dict([("Raju", 40),])

print(m)
# {'Raju': 40}

n = dict([["Raju", 40],])

print(n)
# {'Raju': 40}

s = dict(["Raju", 40])

print(s)
# ValueError: dictionary update sequence element #0 has length 4; 2 is required

t = dict(("Raju", 40))

print(t)
# ValueError: dictionary update sequence element #0 has length 4; 2 is required

c = dict("raju", 40)

print(c)
# TypeError: dict expected at most 1 argument, got 2


d = dict(["Raju", 40, "Avanti", 6, "Pinku", 32])

print(d)
# ValueError: dictionary update sequence element #0 has length 4; 2 is required

f = dict(("Raju", 40, "Avanti", 6, "Pinku", 32))

print(f)
# ValueError: dictionary update sequence element #0 has length 4; 2 is required

e = dict({"Raju", 40, "Avanti", 6, "Pinku", 32})

print(e)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence

