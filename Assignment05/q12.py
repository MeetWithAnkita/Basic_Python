import random

# Generate 100 random 0s and 1s
random_list = [random.randint(0, 1) for _ in range(100)]
max_zeros = max("".join(map(str, random_list)).split("1"), key=len).count("0")

print("Random binary list:", random_list)
print("Longest run of zeros:", max_zeros)