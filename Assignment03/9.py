# 9. Twin prime numbers are primes that differ by 2(e.g. 3 and 5, 101
# and 103). To find out all twin primes within 10000.
def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_twin_primes(limit):
    """Find all twin primes up to a given limit."""
    twin_primes = []
    for num in range(2, limit - 1):
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

# Example usage:
limit = 10000
twin_primes = find_twin_primes(limit)

print(f"Twin primes up to {limit}:")
for pair in twin_primes:
    print(pair)
