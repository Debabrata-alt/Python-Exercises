# Write a Python program to replace dictionary values with their average.

student_details = [
  {'id': 1, 'subject': 'math', 'V': 70, 'VI': 82},
  {'id': 2, 'subject': 'math', 'V': 73, 'VI': 74},
  {'id': 3, 'subject': 'math', 'V': 75, 'VI': 86}
]

newList = []

for el in student_details:
  n1 = el.pop("V")
  n2 = el.pop("VI")
  el["V + VI"] = (n1 + n2)/2
  newList.append(el)


print(newList)
# [{'id': 1, 'subject': 'math', 'V + VI': 76.0}, {'id': 2, 'subject': 'math', 'V + VI': 73.5}, {'id': 3, 'subject': 'math', 'V + VI': 80.5}]