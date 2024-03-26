# Write a Python program to count the number of lines in a text file.

with open("demo.txt", mode="r") as f:
  # 'content' is a List of lines (strings).
  content = f.readlines()
  no_of_lines = len(content)

print(no_of_lines) # 11

#///////////////////////////////////////////////////////////////////

def myFunc():
  with open("demo.txt", mode="r") as f:
    content = f.readlines()
    for i, e in enumerate(content):
      pass
  return i + 1

print(myFunc()) # 11
