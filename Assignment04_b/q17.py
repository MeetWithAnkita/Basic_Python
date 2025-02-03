from itertools import permutations

# Prompt the user to enter a word
word = input("Enter a word: ")

# Generate permutations
all_permutations = [''.join(p) for p in permutations(word)]
print("All permutations:", all_permutations)