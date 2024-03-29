# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

myList = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

x = sorted(myList, key=lambda el: el[1])

print(x)
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

