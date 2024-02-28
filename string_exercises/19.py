# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def s_uppercase(s):
  s_list = [s for s in s[:5] if s.isupper()]
  if len(s_list) >= 2:
    return s.upper()
  else:
    return s.lower()


print(s_uppercase("RajAbabu")) # RAJABABU
print(s_uppercase("rajaBaBu")) # rajababu

print(s_uppercase("rAJababu")) # RAJABABU
print(s_uppercase("rajaBABu")) # rajababu
