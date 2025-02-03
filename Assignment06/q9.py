def is_armstrong(number):
    """
    Check if a number is an Armstrong number.

    Parameters:
    - number (int): The number to be checked.

    Returns:
    - bool: True if the number is an Armstrong number, False otherwise.
    """
    # Convert the number to a string to calculate digits
    digits = list(map(int, str(number)))
    power = len(digits)  # Number of digits
    total = sum(digit ** power for digit in digits)  # Sum of digits raised to the power
    return total == number

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number to check if it is an Armstrong number: "))
    if is_armstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
