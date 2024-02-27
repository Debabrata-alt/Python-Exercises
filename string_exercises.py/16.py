# Write a Python program to sort a string lexicographically.
# lexicographically = in dictionary order

def lexicographic_sort(string):
  # sort in ascending order
  sorted_list = sorted(string, key=str.upper)
  sorted_string = "".join(str for str in sorted_list)
  return sorted_string

sorted_string = lexicographic_sort("amAr 12Soshi 34Non JaPan")
print(sorted_string) # 1234aAaahiJmNnnooPrSs

sorted_string = lexicographic_sort("qUick1 uMbRaLlA2 45yOUr")
print(sorted_string) # 1245aAbcikLlMOqRrUuUy


