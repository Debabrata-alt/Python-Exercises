# Write a Python program to find the numbers in a given string and store them in a list. Afterward, display the numbers that are longer than the length of the list in sorted form. Use the lambda function to solve the problem.
# Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
# Numbers in sorted form:
# 20 23 56

myStr = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"

myList = myStr.split(" ")

print(myList)
# ['sdf', '23', 'safs8', '5', 'sdfsd8', 'sdfs', '56', '21sfs', '20', '5']

num_list = list(filter(lambda el: el.isdigit(), myList))

print(num_list) 
# ['23', '5', '56', '20', '5']

mixed_list = (list(el for el in myList if not el.isdigit()))

print(mixed_list)
# ['sdf', 'safs8', 'sdfsd8', 'sdfs', '21sfs']

extracted_num_list = list(e for el in mixed_list for e in el if e.isdigit())

print(extracted_num_list) 
# ['8', '8', '2', '1']

total_num_list = sorted(num_list + extracted_num_list)

print(total_num_list)
# ['1', '2', '20', '23', '5', '5', '56', '8', '8']

requied_nums = [el for el in total_num_list if int(el) > len(total_num_list)]

print(requied_nums)
# ['20', '23', '56']