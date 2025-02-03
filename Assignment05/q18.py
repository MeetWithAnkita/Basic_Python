L = ["apple", "banana", "kiwi", "pear", "cherry"]
# a) Remove first characters
new_list_a = [s[1:] for s in L]

# b) Lengths of strings
new_list_b = [len(s) for s in L]

# c) Strings at least 3 characters long
new_list_c = [s for s in L if len(s) >= 3]

print("a) Without first characters:", new_list_a)
print("b) Lengths:", new_list_b)
print("c) Strings with 3+ characters:", new_list_c)