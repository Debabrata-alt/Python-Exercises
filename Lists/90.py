# Write a Python program to concatenate element-wise three given lists.
# Original lists:
# ['0', '1', '2', '3', '4']
# ['red', 'green', 'black', 'blue', 'white']
# ['100', '200', '300', '400', '500']
# Concatenate element-wise three said lists:
# ['0red100', '1green200', '2black300', '3blue400', '4white500']

list1 = ['0', '1', '2', '3', '4']
list2 = ['red', 'green', 'black', 'blue', 'white']
list3 = ['100', '200', '300', '400', '500']

x = list(el[0] + el[1] + el[2] for el in zip(list1, list2, list3))

print(x)
# ['0red100', '1green200', '2black300', '3blue400', '4white500']