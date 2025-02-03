def is_divisible(dividend, divisor):
    """
    Check if one number is divisible by another.
    
    Parameters:
    - dividend (int): The number to be divided.
    - divisor (int): The number by which we divide.
    
    Returns:
    - bool: True if divisible, False otherwise.
    - str: An error message if divisor is zero.
    """
    if divisor == 0:
        return "Error: Division by zero is not allowed."
    return dividend % divisor == 0

# Example usage
if __name__ == "__main__":
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    result = is_divisible(dividend, divisor)
    if isinstance(result, str):  # Check for error message
        print(result)
    else:
        if result:
            print(f"{dividend} is divisible by {divisor}.")
        else:
            print(f"{dividend} is not divisible by {divisor}.")
