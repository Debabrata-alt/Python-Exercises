# Write a Python program to move a specified element in a given list.
# Original list:
# ['red', 'green', 'white', 'black', 'orange']
# Move white at the end of the said list:
# ['red', 'green', 'black', 'orange', 'white']
# Original list:
# ['red', 'green', 'white', 'black', 'orange']
# Move red at the end of the said list:
# ['green', 'white', 'black', 'orange', 'red']
# Original list:
# ['red', 'green', 'white', 'black', 'orange']
# Move black at the end of the said list:
# ['red', 'green', 'white', 'orange', 'black']


def func(word):
  inp_list = ['red', 'green', 'white', 'black', 'orange']
  # Remove the word from the List
  inp_list.remove(word)
  # Append the word at the end of the List
  inp_list.append(word)
  return inp_list


print(func("white"))
# ['red', 'green', 'black', 'orange', 'white']

print(func("red"))
# ['green', 'white', 'black', 'orange', 'red']

print(func("black"))
# ['red', 'green', 'white', 'orange', 'black']