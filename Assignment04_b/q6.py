# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Remove periods and commas, then convert to lowercase
result = user_input.replace('.', '').replace(',', '').lower()

# Print the resulting string
print("Resulting string:", result)