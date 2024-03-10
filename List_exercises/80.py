# Write a Python program to remove the first specified number of elements from a given list satisfying a condition.
# Remove the first 4 number of even numbers from the following list:
# [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
# Output:
# [3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]
# Original list:
# [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
# Remove first 4 even numbers from the said list:
# [3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]

list1 = [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
list2 =  [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]

def func(inp_list, num):
  count = 0
  for el in inp_list:
    if el % 2 == 0:
      count += 1
      inp_list.remove(el)
    if count == num:
      break
  return inp_list


print(func(list1, 4)) 
# [3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]

print(func(list2, 4))
# [3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]