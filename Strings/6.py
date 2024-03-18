# Write a program that asks the user for a string and prints out the location of each 'a' in
# the string.

# Sample input: Debabrata Mandal
# letter to search: "a"
# Sample Output: Total 5 occurances, at index no 3, 6, 8, 11, 14 respectively.

string = "Debabrata Mandal"
letter_to_search = "a"
my_list = []
count = 0

for n in range(len(string)):
  if string[n] == letter_to_search:
    my_list.append(n)
    count +=1

indices = ", ".join(str(el) for el in my_list)

print(f"Total {count} occurances, at index no {indices} respectively.")
# Total 5 occurances, at index no 3, 6, 8, 11, 14 respectively.