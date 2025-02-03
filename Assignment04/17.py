import math

def series_a(n):
    return sum(k * (k + 1) * (k + 2) // 6 for k in range(1, n + 1))

def series_b(n):
    return sum(math.factorial(k) for k in range(1, n + 1))

def series_c(n):
    result = 0
    for k in range(1, n + 1):
        numerator = k * (k + 1) // 2
        denominator = math.factorial(k)
        result += numerator / denominator
    return result

n = int(input("Enter the number of terms (n): "))

print("Sum of series (a):", series_a(n))
print("Sum of series (b):", series_b(n))
print("Sum of series (c):", series_c(n))
