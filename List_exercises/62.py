# Write a Python program to check if two lists have the same elements in them in same order or not.
# Original lists:
# ['red', 'green', 'black', 'orange']
# ['red', 'pink', 'green', 'white', 'black']
# ['white', 'orange', 'pink', 'black']
# Test common elements between color1 and color2 are in same order?
# True
# Test common elements between color1 and color3 are in same order?
# False
# Test common elements between color2 and color3 are in same order?
# False

color1 = ['red', 'green', 'black', 'orange']
color2 = ['red', 'pink', 'green', 'white', 'black']
color3 = ['white', 'orange', 'pink', 'black']

def check_common_elements(list1, list2):

  common_elements = set(list1) & set(list2)
  
  my_list1 = [el for el in list1 if el in common_elements]
  my_list2 = [el for el in list2 if el in common_elements]
  
  return my_list1 == my_list2


print(check_common_elements(color1, color2)) # True
print(check_common_elements(color1, color3)) # False
print(check_common_elements(color2, color3)) # False