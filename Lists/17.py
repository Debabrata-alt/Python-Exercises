# Write a Python program to get the frequency of elements in a list.

myList = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

myDict = {el: myList.count(el) for el in myList}

print(myDict)
# {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

#/////////////////////////////////////////////////////////////////////////////////////////////

# Import the 'collections' module, which provides specialized container data types
import collections

# Define a list 'my_list' containing multiple numbers, including duplicates
my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

# Use the 'collections.Counter' function to count the frequency of each element in 'my_list' and store it in 'ctr'.
ctr = collections.Counter(my_list)

print(ctr) 
# Counter({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})

