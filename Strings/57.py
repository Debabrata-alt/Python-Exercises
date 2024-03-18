# Write a Python program to find the longest common sub-string from two given strings.

# Import SequenceMatcher from difflib
from difflib import SequenceMatcher

# Function to find longest common substring
def longest_Substring(s1, s2):

  # Create sequence matcher object
  seq_match = SequenceMatcher(None, s1, s2) 
  
  print(seq_match) # <difflib.SequenceMatcher object at 0x00000231212D60C0>
  
  # Find longest matching substring
  match = seq_match.find_longest_match(0, len(s1), 0, len(s2))
  
  print(match) # Match(a=0, b=5, size=4)
  
  print(match.a) # 0
  print(match.b) # 5
  print(match.size) # 4

  # If match found, return substring
  if (match.size!=0):  
    return (s1[match.a: match.a + match.size])
  
  # Else no match found
  else:
    return ('Longest common sub-string not present')


# Print longest common substring
print(longest_Substring("abcdefgh", "xswerabcdwd")) # abcd

# Print longest common substring
print(longest_Substring("efgabcdefhjcd", "xswerzmabcdefbcdwd")) # abcdef


#/////////////////////////////////////////////////////////////////////

# NOTE: 

# print(longest_Substring("efgabcdefhjcd", "xswerzmabcdefbcdwd")) # abcdef

# match = Match(a=3, b=7, size=6)

# match.a = 3
# match.b = 7
# match.size = 6