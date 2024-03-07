# Write a Python program to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']

color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]

diff_color1_color2 = list(set(color1) - set(color2))

diff_color2_color1 = list(set(color2) - set(color1))

print(diff_color1_color2) # ['red', 'orange', 'white']
print(diff_color2_color1) # ['yellow', 'black']

#/////////////////////////////////////////////////////////////////////////////////////////
# 2nd method (using Counter method from collections package)

from collections import Counter

color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]

# Create Counter objects 'counter1' and 'counter2' for each list to count the occurrences of color names
counter1 = Counter(color1)
counter2 = Counter(color2)

print(counter1) # Counter({'red': 1, 'orange': 1, 'green': 1, 'blue': 1, 'white': 1})
print(counter2) # Counter({'black': 1, 'yellow': 1, 'green': 1, 'blue': 1})

# Print the elements that are in 'counter1' but not in 'counter2' (Color1-Color2)
print("Color1-Color2: ", list(counter1 - counter2))
# Color1-Color2:  ['red', 'orange', 'white']

# Print the elements that are in 'counter2' but not in 'counter1' (Color2-Color1)
print("Color2-Color1: ", list(counter2 - counter1))
# Color2-Color1:  ['black', 'yellow']
