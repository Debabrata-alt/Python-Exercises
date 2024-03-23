# Write a Python program to create set difference.

# 1. Using difference() method

set1 = {'green', 'blue'}
set2 = {'yellow', 'blue'}

diff_set1_set2 = set1.difference(set2)

print(diff_set1_set2) # {'green'}

diff_set2_set1 = set2.difference(set1)

print(diff_set2_set1) # {'yellow'}

#/////////////////////////////////////////////

set1 = {1, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}

diff_set1_set2 = set1.difference(set2)

print(diff_set1_set2) # {2, 3, 4}

diff_set2_set1 = set2.difference(set1)

print(diff_set2_set1) # {8, 9, 6, 7}

#///////////////////////////////////////////////////////////////////////////////////////////

# Using '-' operator

set1 = {"green", "blue"}
set2 = {"blue", "yellow"}

diff_set1_set2 = set1 - set2

print(diff_set1_set2) # {'green'}

diff_set2_set1 = set2 - set1

print(diff_set2_set1) # {'yellow'}

#///////////////////////////////////////////////////

set1 = {1, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}

diff_set1_set2 = set1 - set2

print(diff_set1_set2) # {2, 3, 4}

diff_set2_set1 = set2 - set1

print(diff_set2_set1) # {8, 9, 6, 7}

#///////////////////////////////////////////////////////////////////////////////////////////

# Multiple sets in the difference() method:

set1 = {1, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}
set3 = {3, 4, 5, 3, 9, 10}
set4 = {5, 7, 9, 10, 12, 14}

# Elements that exist only in set1
diff_set1_others = set1.difference(set2, set3, set4)

print(diff_set1_others) # {2}

# Elements that exist only in set4
diff_set4_others = set4.difference(set1, set2, set3)

print(diff_set4_others) # {12, 14}
