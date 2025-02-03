# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Modify the string
if len(user_input) >= 3:
    new_str = user_input[:2] + '*' + user_input[3:] + '!!'
else:
    new_str = user_input + '!!'

# Print the modified string
print("Modified string:", new_str)