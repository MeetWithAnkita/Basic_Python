# 8. To obtain the sum of the following series for some given values of x
# and n:
#                                     1
#                                 1       1
#                             1       2       1        
#                         1       3       3       1
#                     1       4       6       4       1
#                 1       5       10      10      5       1            
#                Figure 1: First Six rows of Pascal’s Triangle
# (a) x - x^3/3 + x^5/5 − x^7/7 ± · · · . . . . .....................up to n terms.
# (b) x^2/2 − x^4/4 + x^6/6 ± · · ·. . . . . . .......................up to n terms
# (c) x^1/1! − x^3/3! + x^5/5! ± · · ·. . . . . . .....................up to n terms
# (d) x^2/2! − x^4/4! + x^6/6! ± · · ·. . . . . . .....................up to n terms
# (e) x − [(x^3)/2] + [(3∗x^5)/(2∗4)] − [(3∗5∗x^7)/(2∗4∗6)] ± · · · . . up to n terms

from math import factorial

def series_a(x, n):
    """Compute x - x^3/3 + x^5/5 − ... up to n terms."""
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
        result += term
    return result

def series_b(x, n):
    """Compute x^2/2 − x^4/4 + x^6/6 − ... up to n terms."""
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 2)) / (2 * i + 2)
        result += term
    return result

def series_c(x, n):
    """Compute x/1! − x^3/3! + x^5/5! − ... up to n terms."""
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result

def series_d(x, n):
    """Compute x^2/2! − x^4/4! + x^6/6! − ... up to n terms."""
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 2)) / factorial(2 * i + 2)
        result += term
    return result

def series_e(x, n):
    """Compute x − (x^3)/2 + (3*x^5)/(2*4) − (3*5*x^7)/(2*4*6) ± ... up to n terms."""
    result = 0
    numerator = 1  # Initial numerator value for 3 * 5 * 7...
    denominator = 1  # Initial denominator value for 2 * 4 * 6...
    for i in range(n):
        if i > 0:
            numerator *= 2 * i - 1
            denominator *= 2 * i
        term = ((-1) ** i) * (numerator / denominator) * (x ** (2 * i + 1))
        result += term
    return result

# Example usage:
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms n: "))

print(f"(a) Series result: {series_a(x, n)}")
print(f"(b) Series result: {series_b(x, n)}")
print(f"(c) Series result: {series_c(x, n)}")
print(f"(d) Series result: {series_d(x, n)}")
print(f"(e) Series result: {series_e(x, n)}")
