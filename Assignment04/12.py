def special_two_digit_numbers(limit):
    special_numbers = []
    for num in range(10, min(100, limit)):  
        tens = num // 10  
        units = num % 10  
        digit_sum = tens + units
        digit_product = tens * units
        if digit_sum + digit_product == num:
            special_numbers.append(num)
    return special_numbers

special_numbers = special_two_digit_numbers(500)
print("Special two-digit numbers within 500:")
print(special_numbers)
