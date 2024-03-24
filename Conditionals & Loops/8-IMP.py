# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).

lines = []

# Continue to prompt the user for input indefinitely until a blank line is entered
while True:
  l = input("Enter a line: ")
  # Check if the entered line is not empty (non-empty string)
  if l:
    lines.append(l.upper())
  else:
    # If the entered line is empty, break out of the loop
    break

for l in lines:
  print(l) 
