# Write a Python program to find the elements of a given list of strings that contain a specific substring using lambda.
# Original list:
# ['red', 'black', 'white', 'green', 'orange']
# Substring to search:
# ack
# Elements of the said list that contain specific substring:
# ['black']
# Substring to search:
# abc
# Elements of the said list that contain specific substring:
# []

myList = ['red', 'black', 'white', 'green', 'orange']

def func(myList, sub_str):
  return list(filter(lambda el: sub_str in el, myList))


print(func(myList, "ack"))
# ['black']

print(func(myList, "abc"))
# []

