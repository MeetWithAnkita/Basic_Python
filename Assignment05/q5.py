# Prompt user input for strings
strings = input("Enter a list of strings separated by spaces: ").split()
# Remove the first character
modified_strings = [s[1:] for s in strings]
print("Modified list:", modified_strings)