# Write a Python program to remove a specified dictionary from a given list.
# Original list of dictionary:
# [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

myList = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

l = [el for el in myList if "#FF0000" not in el.values()]

print(l) # [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

#////////////////////////////////////////////////////////////////////////////////////////

myList = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

l = [{k: v} for el in myList for k, v in el.items() if v != "#FF0000"]

print(l)
# [{'color': 'Red'}, {'id': '#800000'}, {'color': 'Maroon'}, {'id': '#FFFF00'}, {'color': 'Yellow'}, {'id': '#808000'}, {'color': 'Olive'}]

#/////////////////////////////////////////////////////////////////////////////////////////////

myList = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

l = [{k: v for el in myList for k, v in el.items() if v != "#FF0000"}]

print(l)
# [{'color': 'Olive', 'id': '#808000'}]