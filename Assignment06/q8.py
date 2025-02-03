def is_prime(number):
    """
    Check if a number is a prime number.

    Parameters:
    - number (int): The number to check for primality.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if number <= 3:
        return True  # 2 and 3 are prime numbers
    if number % 2 == 0 or number % 3 == 0:
        return False  # Eliminate multiples of 2 and 3

    # Check divisors from 5 to √number
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number to check if it is prime: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
