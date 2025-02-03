def is_niven_number(num):
    digit_sum = sum(int(digit) for digit in str(num))  # Sum of digits
    return num % digit_sum == 0 if digit_sum > 0 else False

def niven_numbers_within(limit):
    return [num for num in range(1, limit + 1) if is_niven_number(num)]

niven_numbers = niven_numbers_within(1000)
print("Niven Numbers within 1000:")
print(niven_numbers)
