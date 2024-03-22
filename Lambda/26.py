# Write a Python program to sort each sublist of strings in a given list of lists using lambda.
# Original list:
# [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
# After sorting each sublist of the said list of lists:
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

myList = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]

sort_list = list(map(lambda el: sorted(el), myList))

print(sort_list)
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]