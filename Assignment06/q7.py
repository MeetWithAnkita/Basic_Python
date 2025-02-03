def is_leap_year(year):
    """
    Check if a year is a leap year.

    Parameters:
    - year (int): The year to check.

    Returns:
    - bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Example usage
if __name__ == "__main__":
    year = int(input("Enter a year to check if it is a leap year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
