# Write a Python program to create an intersection of sets.

setx = set(["green", "blue"])

sety = set(["blue", "yellow"])

# Find the intersection of 'setx' and 'sety' (keep only the duplicates)
setz = setx & sety

print(setz) # {'blue'}