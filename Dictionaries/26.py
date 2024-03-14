# Write a Python program to remove spaces from dictionary keys.

student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

newDict = {key.replace(" ", ""): value for key, value in student_list.items()}

print(newDict) # {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}