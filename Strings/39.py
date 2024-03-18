# Write a Python program to count and display vowels in text.

vowels = "aeiuoAEIOU"

def func(text):
  return [t for t in text if t in vowels]

list = func("w3resource.com")

print(f"Total no of vowels: {len(list)}")  # Total no of vowels: 5
print(f"Vowels list: {list}")  # Vowels list: ['e', 'o', 'u', 'e', 'o']
