# Prompt the user to enter a large integer
number = input("Enter a large integer: ")

# Insert commas
formatted_number = "{:,}".format(int(number))
print("Formatted number:", formatted_number)