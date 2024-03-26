# Write a Python program to write a list to a file.

import json

colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

with open("demo1.txt", mode="w") as myFile:
  myFile.write(json.dumps(colors))

#/////////////////////////////////////////////////////////////////////

colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# append at the end of the file
with open("demo1.txt", mode="a") as myFile:
  myFile.write("\n")
  # write() method accepts only strings as parameters
  myFile.write(str(colors))

#/////////////////////////////////////////////////////////////////////

colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

with open("demo1.txt", mode="a") as myFile:
  for color in colors:
    myFile.write("\n")
    myFile.write(color)