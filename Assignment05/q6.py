# Prompt user input
string = input("Enter a string: ")
# ASCII values for each character
ascii_values = {char: ord(char) for char in string}
print("ASCII values:", ascii_values)