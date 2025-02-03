# Prompt the user to enter two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the strings are of the same length
if len(string1) != len(string2):
    print("The strings are not of equal length.")
else:
    # Concatenate alternate characters
    result = ''.join(a + b for a, b in zip(string1, string2))
    print("Resulting string:", result)