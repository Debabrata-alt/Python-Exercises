# Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using the lambda function.
# Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
# Sum of the negative numbers: -32
# Sum of the positive numbers: 48

myList = [2, 4, -6, -9, 11, -12, 14, -5, 17]

pos_sum = sum(filter(lambda el: el > 0, myList))

neg_sum = sum(filter(lambda el: el < 0, myList))

print(pos_sum) # 48
print(neg_sum) # -32

#///////////////////////////////////////////////////////////////////////////////////////

myList = [2, 4, -6, -9, 11, -12, 14, -5, 17]

pos_sum = sum(el for el in myList if el > 0)

neg_sum = sum(el for el in myList if el < 0)

print(pos_sum) # 48
print(neg_sum) # -32