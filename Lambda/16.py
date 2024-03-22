# Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of each student using lists and lambda. Input the number of students, the names and grades of each student.
# Input number of students: 5
# Name: S ROY
# Grade: 1
# Name: B BOSE
# Grade: 3
# Name: N KAR
# Grade: 2
# Name: C DUTTA
# Grade: 1
# Name: G GHOSH
# Grade: 1
# Names and Grades of all students:
# [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
# Second lowest grade: 2.0
# Names:
# N KAR

students = []

n = int(input("Input number of students: "))

for _ in range(n):
  s_name = input("Name: ")  
  score = float(input("Grade: ")) 
  students.append([s_name, score]) 

print(students)
# [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]

sort_list = sorted(students, key=lambda el: el[1])

previous_val = sort_list[0][1]

for el in sort_list:
  if el[1] != previous_val:
    requred_el = el
    break
  previous_val = el[1]

# student who got 2nd lowest grade and his grade
print(f"Student: {requred_el[0]}, Grade: {requred_el[1]}")
# Student: N KAR, Grade: 2.0