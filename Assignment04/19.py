def is_magic_number(num):
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(n))

    while num >= 10:  
        num = sum_of_digits(num)

    return num == 1

def find_magic_numbers(limit):
    magic_numbers = []
    for num in range(1, limit + 1):
        if is_magic_number(num):
            magic_numbers.append(num)
    return magic_numbers

if __name__ == "__main__":
    limit = 1000
    magic_numbers = find_magic_numbers(limit)
    print(f"Magic Numbers within {limit}: {magic_numbers}")
