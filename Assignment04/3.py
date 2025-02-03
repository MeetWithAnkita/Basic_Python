def find_consecutive_numbers(limit):
    result = []
    
    for n in range(limit - 4): 
        sum_squares_first_three = n**2 + (n+1)**2 + (n+2)**2
        sum_squares_last_two = (n+3)**2 + (n+4)**2
        if sum_squares_first_three == sum_squares_last_two:
            result.append((n, n+1, n+2, n+3, n+4))
    
    return result

limit = 1000
consecutive_numbers = find_consecutive_numbers(limit)
if consecutive_numbers:
    print(f"Series of five consecutive numbers where sum of squares of the first three equals the sum of squares of the last two:")
    for series in consecutive_numbers:
        print(series)
else:
    print(f"No series found within {limit}.")
