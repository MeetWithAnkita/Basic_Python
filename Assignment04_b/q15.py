# a) Check if a letter appears in a string
string = input("Enter a string: ")
letter = input("Enter a letter: ")

found = False
for char in string:
    if char == letter:
        found = True
        break
print("Letter found." if found else "Letter not found.")

# b) Count occurrences of a letter
count = 0
for char in string:
    if char == letter:
        count += 1
print(f"The letter '{letter}' occurs {count} times.")

# c) Find the index of the first occurrence
index = -1
for i, char in enumerate(string):
    if char == letter:
        index = i
        break
if index != -1:
    print(f"The letter '{letter}' first occurs at index {index}.")
else:
    print(f"The letter '{letter}' is not in the string.")