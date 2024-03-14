# Write a Python program to count the values associated with a key in a dictionary.
# Expected Output:
# 6
# 2

student = [
  {'id': 1, 'success': True, 'name': 'Lary'},
  {'id': 2, 'success': False, 'name': 'Rabi'},
  {'id': 3, 'success': True, 'name': 'Alex'}
]

id_sum = sum(el["id"] for el in student)

success_sum = sum(el["success"] for el in student)

print(id_sum) # 6
print(success_sum) # 2