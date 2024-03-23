# Write a Python program to convert a given list of tuples to a list of strings using the map function.

tuplex1 = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
tuplex2 = [('Sheridan', 'Gentry'), ('Laila', 'Mckee'), ('Ahsan', 'Rivas'), ('Conna', 'Gonzalez')]

def myFunc(tuplex):
  result = map(" ".join, tuplex)
  return list(result)

print(myFunc(tuplex1))
# ['red pink', 'white black', 'orange green']

print(myFunc(tuplex2))
# ['Sheridan Gentry', 'Laila Mckee', 'Ahsan Rivas', 'Conna Gonzalez']


#////////////////////////////////////////////////////////////////////////////////////////////

tuplex1 = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
tuplex2 = [('Sheridan', 'Gentry'), ('Laila', 'Mckee'), ('Ahsan', 'Rivas'), ('Conna', 'Gonzalez')]

def myFunc(tuplex):
  return list(map(lambda el: el[0] + " " + el[1], tuplex))

print(myFunc(tuplex1))
# ['red pink', 'white black', 'orange green']

print(myFunc(tuplex2))
# ['Sheridan Gentry', 'Laila Mckee', 'Ahsan Rivas', 'Conna Gonzalez']