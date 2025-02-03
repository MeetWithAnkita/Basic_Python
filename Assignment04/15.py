def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_twisted_prime(num):
    if not is_prime(num):
        return False
    reversed_num = int(str(num)[::-1])  
    return is_prime(reversed_num)

def twisted_primes_within(limit):
    """Find all twisted primes within a given limit."""
    return [num for num in range(2, limit) if is_twisted_prime(num)]

twisted_primes = twisted_primes_within(1000)
print("Twisted Prime Numbers within 1000:")
print(twisted_primes)
