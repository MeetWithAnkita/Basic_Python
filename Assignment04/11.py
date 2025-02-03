def is_automorphic(number):
    square = number ** 2
    return str(square).endswith(str(number))

def automorphic_numbers_within(limit):
    return [num for num in range(limit + 1) if is_automorphic(num)]

automorphic_numbers = automorphic_numbers_within(1000)
print("Automorphic Numbers within 1000:")
print(automorphic_numbers)
