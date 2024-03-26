# Write a Python program to remove newline characters from a file.

with open("demo6.txt", mode="w") as f:
  f.write("Add this content.\n")
  f.write("I am Raju.\n")
  f.write("I am 40 years old.\n")
  f.write("I am learning computer programming.\n")
  f.write("Programming is fun!.\n")

with open("demo6.txt", mode="r") as f:
  content = f.readlines()

print(content)
# ['Add this content.\n', 'I am Raju.\n', 'I am 40 years old.\n', 'I am learning computer programming.\n', 'Programming is fun!.\n']

for line in content:
  # Remove the trailing newline character from each line 
  print(line.rstrip("\n"))

# ////////////////////////////////////////////////////////////////////

# Alternatively, 

for line in content:
  # Print the entire line except the last character
  print(line[:-1])
