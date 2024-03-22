# Write a Python program that sums the length of a list of names after removing those that start with lowercase letters. Use the lambda function.
# Result:
# 16

sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']

len_final = len("".join(filter(lambda el: not el[0].islower(), sample_names)))

print(len_final) # 16