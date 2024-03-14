# Write a Python program to print a dictionary line by line.

students = {'Aex': {'class': 'V', 'roll_id': 2}, 'Puja': {'class': 'V', 'roll_id': 3}}

for key in students:
  print(key)
  for k, v in students[key].items():
    print(f"{k}: {v}")
    
    # Aex
    # class: V
    # roll_id: 2
    # Puja
    # class: V
    # roll_id: 3

#////////////////////////////////////////////////////////////////////////////////////

students = {'Aex': {'class': 'V', 'roll_id': 2}, 'Puja': {'class': 'V', 'roll_id': 3}}

for key in students:
  print(key)
  for k in students[key]:
    print(k, ":", students[key][k])
    
    # Aex
    # class : V
    # roll_id : 2
    # Puja
    # class : V
    # roll_id : 3

#////////////////////////////////////////////////////////////////////////////////////////

students = {'Aex': {'class': 'V', 'roll_id': 2}, 'Puja': {'class': 'V', 'roll_id': 3}}

for key in students:
  print(key)
  for k,v in students[key].items():
    print(k, ":", v)
    
    # Aex
    # class : V
    # roll_id : 2
    # Puja
    # class : V
    # roll_id : 3