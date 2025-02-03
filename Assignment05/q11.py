# Create a patterned list [1, 1, 0, 1, 0, 0, 1, ..., 1]
patterned_list = []
for i in range(11):  # The last two ones separated by 10 zeroes
    patterned_list.extend([1] + [0] * i)
print("Patterned list:", patterned_list)