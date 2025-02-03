def sum_of_squares(n):
    """Calculate the sum of the squares of the first n natural numbers without using a formula."""
    sum_squares = 0
    for i in range(1, n + 1):
        sum_squares += i ** 2
    return sum_squares

# Input number n
n = int(input("Enter a number n to find the sum of the squares of the first n natural numbers: "))

# Calculate and print the sum of squares
result = sum_of_squares(n)
print(f"The sum of the squares of the first {n} natural numbers is: {result}")
