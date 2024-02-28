#  Write a Python program to strip a set of characters from a string.

def strip_chars(string, chars):
  return "".join(s for s in string if s not in chars)


print(strip_chars("The quick brown fox jumps over the lazy dog", "aeiou"))
# Th qck brwn fx jmps vr th lzy dg