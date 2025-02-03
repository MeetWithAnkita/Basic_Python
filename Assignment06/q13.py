# (a) Recursive function for a^b
def power(a, b):
    if b == 0:  # Base case
        return 1
    return a * power(a, b - 1)

# (b) Recursive function to calculate the square root of a real number
def sqrt_real(n, guess=1.0, tolerance=1e-10):
    if abs(guess**2 - n) < tolerance:  # Base case
        return guess
    new_guess = (guess + n / guess) / 2
    return sqrt_real(n, new_guess)

# (c) Recursive function to calculate the square root of a complex number
def sqrt_complex(c, guess=1+0j, tolerance=1e-10):
    if abs(guess**2 - c) < tolerance:  # Base case
        return guess
    new_guess = (guess + c / guess) / 2
    return sqrt_complex(c, new_guess)

# (d) Recursive function for the sum of digits of a number
def sum_of_digits(n):
    if n == 0:  # Base case
        return 0
    return abs(n % 10) + sum_of_digits(abs(n) // 10)

# (e) Recursive function for the number of digits in a number
def num_digits(n):
    if n == 0:  # Base case
        return 0
    return 1 + num_digits(abs(n) // 10)

# (f) Recursive function for the sum of each digit raised to the power of the number of digits
def sum_of_powers(n, digits=None):
    if digits is None:  # Calculate the number of digits only once
        digits = num_digits(n)
    if n == 0:  # Base case
        return 0
    return (abs(n % 10) ** digits) + sum_of_powers(abs(n) // 10, digits)

# (g) Recursive function to calculate the series: x + x^2/2 + x^3/3 + ... up to n terms
def series_sum(x, n):
    if n == 1:  # Base case
        return x
    return (x**n / n) + series_sum(x, n - 1)

# Example usage
if __name__ == "__main__":
    # (a)
    print("a^b (2^3):", power(2, 3))  # Output: 8

    # (b)
    print("Square root of 16 (real):", sqrt_real(16))  # Output: 4.0

    # (c)
    print("Square root of 4+4j (complex):", sqrt_complex(4+4j))  # Output: (2.197...+0.910...)

    # (d)
    print("Sum of digits of 12345:", sum_of_digits(12345))  # Output: 15

    # (e)
    print("Number of digits in 12345:", num_digits(12345))  # Output: 5

    # (f)
    print("Sum of each digit raised to the power of the number of digits (123):", sum_of_powers(123))  # Output: 36

    # (g)
    print("Sum of series (x=2, n=3):", series_sum(2, 3))  # Output: 6.333...
