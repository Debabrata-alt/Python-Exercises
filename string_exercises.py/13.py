# Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def insert_sting_middle(str1, str2):
  # floor division (//)
  index_at_half = len(str1) // 2
  return str1[:index_at_half] + str2 + str1[index_at_half: ]

new_str = insert_sting_middle(str1="{{}}", str2="PHP")
print(new_str) # {{PHP}}

new_str = insert_sting_middle(str1="[[]]", str2="Python")
print(new_str) # [[Python]]

new_str = insert_sting_middle(str1="<<>>", str2="Python")
print(new_str) # <<Python>>