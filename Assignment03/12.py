# 12. A program is required which accepts two numbers then prints out
# a random number somewhere between those two numbers without
# using the built in random function.
import time

def custom_random(min_value, max_value):
    # Ensure min_value is less than max_value
    if min_value > max_value:
        min_value, max_value = max_value, min_value

    # Get the current time in microseconds
    seed = int(time.time() * 1000000) % (max_value - min_value + 1)

    # Generate a random number in the range [min_value, max_value]
    return min_value + seed

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Generate and print a random number
random_number = custom_random(num1, num2)
print(f"Random number between {num1} and {num2}: {random_number}")