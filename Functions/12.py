# Write a Python program to access a function inside a function.

def test(a):
  def add(b):
    # Declare 'a' from the outer scope as nonlocal to modify its value
    nonlocal a
    a += 1
    return a + b
  return add


func = test(4)

print(func(7)) # 12
