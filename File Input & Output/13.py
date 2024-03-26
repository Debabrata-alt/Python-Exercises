# Write a Python program to combine each line from first file with the corresponding line in second file.

# 1. Creating a new file named 'demo3.txt'

names = ["Raju", "Pinku", "Avanti", "Manik", "Manika", "Debu"]

with open("demo3.txt", mode="w") as f:
  for name in names:
    f.write(name + "\n")

# 2. Creating a new file named 'demo4.txt'

flowers = ['Rose', 'Zinnia', 'Tulip', 'Jesmine', 'Dahlia', 'Sunflower']

with open("demo4.txt", mode="w") as f:
  for flower in flowers:
    f.write(flower + "\n")

# 3. Now combining the contents of 'demo3.txt' and 'demo4.txt' in a new file named 'demo5.txt'

with open("demo3.txt", mode="r") as f1, open("demo4.txt", mode="r") as f2:
  with open("demo5.txt", mode="w") as f:
    for line1, line2 in zip(f1, f2):
      f.write(line1)
      f.write(line2)