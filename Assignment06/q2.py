def digital_root(n):
    """
    Calculate the digital root of a given number.

    Parameters:
    - n (int): The number to calculate the digital root for.

    Returns:
    - int: The digital root of the number.
    """
    while n >= 10:  # Continue until the number has only one digit
        n = sum(int(digit) for digit in str(n))  # Sum the digits of n
    return n

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number to find its digital root: "))
    print(f"The digital root of {number} is: {digital_root(number)}")
