# Write a Python program to filter the height and width of students, which are stored in a dictionary using lambda.
# Original Dictionary:
# {'Cierra Vega': (6.2, 68), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66), 'Rajubaba': (6.3, 72), 'Pinku': (6.0, 70), 'Avanti': (5.9, 71)}
# Height> 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 68), 'Rajubaba': (6.3, 72)}

myDict = {'Cierra Vega': (6.2, 68), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66), 'Rajubaba': (6.3, 72), 'Pinku': (6.0, 70), 'Avanti': (5.9, 71)}

newDict = dict(filter(lambda el: (el[1][0], el[1][1]) > (6, 70), myDict.items()))

print(newDict)
# {'Cierra Vega': (6.2, 68), 'Rajubaba': (6.3, 72)}

#///////////////////////////////////////////////////////////////

newDict = dict(filter(lambda el: (el[1][0], el[1][1]) >= (6, 70), myDict.items()))

print(newDict)
# {'Cierra Vega': (6.2, 68), 'Rajubaba': (6.3, 72), 'Pinku': (6.0, 70)}
