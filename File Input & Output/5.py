# Write a Python program to read last n lines of a file.

with open("demo.txt", mode="r") as f:
  # read the last 3 lines of the file
  content = f.readlines()[-3:]

for line in content:
  print(line)