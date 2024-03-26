# Write a Python program to read a file line by line and store it into a list.

myList = []

with open("demo.txt", mode="r") as f:
  # Read the first line
  line = f.readline()
  myList.append(line)
  while line:
    print(line)
    # Read the next lines one after another
    line = f.readline()
    myList.append(line)

# print 'Done!' when all lines in the file will be read.
print("Done!")

print(myList)