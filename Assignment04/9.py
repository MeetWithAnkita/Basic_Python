def get_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def is_abundant(n):
    return sum(get_divisors(n)) > n

def abundant_numbers_within(limit):
    return [num for num in range(1, limit + 1) if is_abundant(num)]

abundant_numbers = abundant_numbers_within(500)
print("Abundant Numbers within 500:")
print(abundant_numbers)
