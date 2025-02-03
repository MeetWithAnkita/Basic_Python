# a) Integers 0 through 59
list1 = list(range(60))
print("a) Integers 0 through 59:", list1)

# b) Squares of 1 through 49
list2 = [x**2 for x in range(1, 50)]
print("b) Squares of 1 through 49:", list2)

# c) Pattern ['a', 'bb', 'ccc', ..., 'z'*26]
list3 = [chr(97 + i) * (i + 1) for i in range(26)]
print(list3)
