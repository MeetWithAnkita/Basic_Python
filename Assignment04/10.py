from itertools import chain, combinations

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

def is_semi_perfect(n, divisors):
    for subset in chain.from_iterable(combinations(divisors, r) for r in range(len(divisors) + 1)):
        if sum(subset) == n:
            return True
    return False

def find_weird_numbers(limit):
    weird_numbers = []
    for num in range(1, limit + 1):
        divisors = get_divisors(num)
        if is_abundant(num) and not is_semi_perfect(num, divisors):
            weird_numbers.append(num)
    return weird_numbers

weird_numbers = find_weird_numbers(1000)
print("Weird Numbers within 1000:")
print(weird_numbers)
