# Write a Python program to extract common index elements from more than one given list.
# Original lists:
# [1, 1, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 7]
# [0, 1, 2, 3, 4, 5, 7]
# Common index elements of the said lists:
# [1, 7]


list1 = [1, 1, 3, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 5, 7]
list3 = [0, 1, 2, 3, 4, 5, 7]

my_list1 = list(enumerate(list1))
my_list2 = list(enumerate(list2))
my_list3 = list(enumerate(list3))

print(my_list1) # [(0, 1), (1, 1), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
print(my_list2) # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 7)]
print(my_list3) # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 7)]


final_list = [el[1] for el in my_list1 if el in my_list2 and el in my_list3 and my_list1.index(el) == my_list2.index(el) == my_list3.index(el)]

print(final_list) # [1, 7]

