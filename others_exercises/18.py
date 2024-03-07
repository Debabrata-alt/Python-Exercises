# Arithmatic calucation (Improve it with lambda function)

num1, num2 = int(input("Enter a: ")), int(input("Enter b: "))

user_choice = input("Sum for 1\nSubstraction for 2\nMultiplication for 3\nDivision for 4\n")

if user_choice == "1":
  print(f"Sum = {num1 + num2}")
elif user_choice == "2":
  subtraction = num1 - num2 if num1 > num2 else num2 - num1
  print(f"Subtraction = {subtraction}")
elif user_choice == "3":
  print(f"Multiplication = {num1 - num2}")
elif user_choice == "4":
  division = num1 / num2 if num1 > num2 else num2 / num1
  print(f"Division = {division}")