# Write a Python program to read first n lines of a file.

def myFunc(n):
  with open("demo.txt", mode="r") as f:
    content = f.readlines()[:n + 1]
  return content

content = myFunc(3)

for line in content:
  print(line)

