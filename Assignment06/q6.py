def reverse_number(number):
    """
    Reverse the digits of a given number.

    Parameters:
    - number (int): The number to be reversed.

    Returns:
    - int: The reversed number.
    """
    reversed_num = 0
    sign = -1 if number < 0 else 1  # Preserve the sign of the number
    number = abs(number)  # Work with the absolute value

    while number > 0:
        digit = number % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Add it to the reversed number
        number //= 10  # Remove the last digit from the original number

    return sign * reversed_num  # Restore the original sign

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number to reverse: "))
    print(f"The reversed form of {number} is {reverse_number(number)}.")
