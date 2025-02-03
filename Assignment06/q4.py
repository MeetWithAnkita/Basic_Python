def number_of_factors(number):
    """
    Returns the number of factors of a given number.

    Parameters:
    - number (int): The number to find the number of factors for.

    Returns:
    - int: The number of factors of the given number.
    """
    factor_count = 0
    
    # Loop through all numbers from 1 to the absolute value of the number
    for i in range(1, abs(number) + 1):
        if number % i == 0:  # If i is a factor of the number
            factor_count += 1  # Increment the factor count

    return factor_count

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number to find how many factors it has: "))
    print(f"The number of factors of {number} is: {number_of_factors(number)}")
