# Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an integer.

students_list = [('Alberto Franco', '15/05/2002', '35kg'), ('Gino Mcneill', '17/05/2002', '37kg'), ('Ryan Parkes', '16/02/1999', '39kg'), ('Eesha Hinton', '25/09/1998', '35kg')]

name_list = list(map(lambda el: el[0], students_list))
dob_list = list(map(lambda el: el[1], students_list))
weight_list = list(map(lambda el: int(el[2][:2]), students_list))

print(name_list)
# ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton']
print(dob_list)
# ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998']
print(weight_list)
# [35, 37, 39, 35]