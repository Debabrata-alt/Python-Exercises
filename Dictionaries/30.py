# Write a Python program to count the number of items in a dictionary value that is a list.

dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

l = sum(len(dict[key]) for key in dict)

print(l) # 5

#////////////////////////////////////////////////////////////////////////////////////////

dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

l = sum(map(len, dict.values()))

print(l) # 5