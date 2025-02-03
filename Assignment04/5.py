import math

def series_a(x, n):
    """Compute the sum of series (a): x^2/2 - x^4/4 + x^6/6 ± ... up to n terms."""
    total = 0
    for k in range(1, n + 1):
        term = (x ** (2 * k)) / (2 * k)  # Compute x^(2k)/(2k)
        if k % 2 == 0:
            total -= term  # Alternate sign
        else:
            total += term
    return total

def series_b(x, n):
    """Compute the sum of series (b): x^2/2! - x^4/4! + x^6/6! ± ... up to n terms."""
    total = 0
    for k in range(1, n + 1):
        term = (x ** (2 * k)) / math.factorial(2 * k)  # Compute x^(2k)/(2k)!
        if k % 2 == 0:
            total -= term  # Alternate sign
        else:
            total += term
    return total

def series_c(x, n):
    """Compute the sum of series (c): 1 + x/2 - x^2/(2*4) + x^3/(2*4*6) ± ... up to n terms."""
    total = 1  # Start with 1
    for k in range(1, n + 1):
        term = (x ** k) / math.factorial(2 * k)  # Compute x^k/(2k)!
        if k % 2 == 0:
            total -= term  # Alternate sign
        else:
            total += term
    return total

# Input values for x and n
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))

# Calculate sums for each series
sum_a = series_a(x, n)
sum_b = series_b(x, n)
sum_c = series_c(x, n)

# Print results
print(f"Sum of series (a): {sum_a}")
print(f"Sum of series (b): {sum_b}")
print(f"Sum of series (c): {sum_c}")
