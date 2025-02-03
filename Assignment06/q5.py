def factors(number):
    """
    Returns a list of factors of a given number.

    Parameters:
    - number (int): The number to find factors for.

    Returns:
    - list: A list of factors of the given number.
    """
    factor_list = []
    
    for i in range(1, abs(number) + 1):  # Loop from 1 to the absolute value of the number
        if number % i == 0:  # If the number is divisible by i, it is a factor
            factor_list.append(i)
    
    return factor_list

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number to find its factors: "))
    print(f"The factors of {number} are: {factors(number)}")
