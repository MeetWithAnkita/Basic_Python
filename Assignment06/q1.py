def rectangle(m, n):
    """
    Prints an m x n rectangle of asterisks.

    Parameters:
    - m (int): The number of rows in the rectangle.
    - n (int): The number of columns in the rectangle.
    """
    for i in range(m):
        print('*' * n)  # Print a row of n asterisks

# Example usage
if __name__ == "__main__":
    m = int(input("Enter the number of rows (m): "))
    n = int(input("Enter the number of columns (n): "))
    rectangle(m, n)
