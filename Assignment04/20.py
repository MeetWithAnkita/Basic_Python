import math
def hyperfactorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i ** i
    return result

def find_hyperfactorials(limit):
    hyperfactorials = []
    n = 1
    while True:
        h = hyperfactorial(n)
        if h > limit:
            break
        hyperfactorials.append(h)
        n += 1
    return hyperfactorials

limit = 1000
hyperfactorials = find_hyperfactorials(limit)
print(f"Hyperfactorial numbers within {limit}:")
print(hyperfactorials)
