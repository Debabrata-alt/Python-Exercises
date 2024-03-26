# Write a Python program to append text to a file and display the text.

def myFunc():
  with open("demo.txt", mode="a") as f:
    f.write("New line is appended at the end.\n")
    f.write("This is the current last line.\n")

myFunc()

with open("demo.txt", mode="r") as f:
  # read the last 2 lines of the file
  content = f.readlines()[-2:]

for line in content:
  print(line)