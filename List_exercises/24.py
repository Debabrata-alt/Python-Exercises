# Write a Python program to iterate over two lists simultaneously.


num = [1, 2, 3]
color = ['red', 'white', 'black']

# Use a 'for' loop and the 'zip' function to iterate over pairs of elements from 'num' and 'color' in parallel.
# In each iteration, the variables 'a' and 'b' will hold the values from 'num' and 'color', respectively.
# Print the values of 'a' and 'b' in each iteration
for (a, b) in zip(num, color):
  print(a, b)

  # 1 red
  # 2 white
  # 3 black  

#///////////////////////////////////////////////////////////////

# zip() function

num = [1, 2, 3]
color = ['red', 'white', 'black']
names = ["raju", "avanti", "pinku"]

my_list = list(zip(num, color, names))

print(my_list) # [(1, 'red', 'raju'), (2, 'white', 'avanti'), (3, 'black', 'pinku')]


# zip(iter1, iter2, iter3, iter4, iter5, iter6, iter7, .......)