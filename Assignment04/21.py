import math
def is_sunny_number(num):
    successor = num + 1
    sqrt_successor = math.sqrt(successor)
    return sqrt_successor.is_integer()

def find_sunny_numbers(limit):
    sunny_numbers = []
    for i in range(1, limit + 1):
        if is_sunny_number(i):
            sunny_numbers.append(i)
    return sunny_numbers
limit = 2000
sunny_numbers = find_sunny_numbers(limit)
print(f"Sunny numbers within {limit}:")
print(sunny_numbers)
