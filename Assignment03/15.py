import math
from itertools import permutations, count

# Helper functions
def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def product_of_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Functions for specific number types
def floyds_triangle(n):
    result = []
    num = 1
    for i in range(1, n + 1):
        result.append(list(range(num, num + i)))
        num += i
    return result

def hyperfactorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i ** i
    return result

def is_kaprekar(n):
    square = str(n**2)
    d = len(str(n))
    left = square[:-d] or "0"
    right = square[-d:]
    return n == int(left) + int(right)

def is_vampire_number(n):
    digits = sorted(str(n))
    for i in range(10**(len(digits) // 2 - 1), 10**(len(digits) // 2)):
        j = n // i
        if n % i == 0 and sorted(str(i) + str(j)) == digits:
            return True
    return False

def is_sublime_number(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    divisors_sum = sum(divisors)
    return is_perfect(len(divisors)) and is_perfect(divisors_sum)

def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_smith_number(n):
    if is_prime(n):
        return False
    prime_factors = []
    num = n
    for i in range(2, int(math.sqrt(n)) + 1):
        while num % i == 0:
            prime_factors.append(i)
            num //= i
    if num > 1:
        prime_factors.append(num)
    return sum_of_digits(n) == sum(sum_of_digits(f) for f in prime_factors)

def lucky_numbers(limit):
    numbers = list(range(1, limit + 1))
    idx = 1
    while idx < len(numbers):
        step = numbers[idx]
        numbers = [num for i, num in enumerate(numbers) if (i + 1) % step != 0 or i == 0]
        idx += 1
    return numbers

def is_pandigital(n):
    digits = str(n)
    return sorted(digits) == [str(i) for i in range(len(digits))]

# Main program
def main():
    while True:
        print("\nNumber Properties Checker")
        print("1. Floyd's Triangle")
        print("2. Hyperfactorial Number")
        print("3. Kaprekar Number")
        print("4. Vampire Number")
        print("5. Sublime Number")
        print("6. Smith Number")
        print("7. Lucky Numbers")
        print("8. Pandigital Number")
        print("9. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            n = int(input("Enter the number of rows for Floyd's Triangle: "))
            triangle = floyds_triangle(n)
            print("Floyd's Triangle:")
            for row in triangle:
                print(" ".join(map(str, row)))
        elif choice == 2:
            n = int(input("Enter the number to calculate Hyperfactorial: "))
            print(f"Hyperfactorial of {n}: {hyperfactorial(n)}")
        elif choice == 3:
            n = int(input("Enter the number: "))
            print(f"{n} is a Kaprekar Number: {is_kaprekar(n)}")
        elif choice == 4:
            n = int(input("Enter the number: "))
            print(f"{n} is a Vampire Number: {is_vampire_number(n)}")
        elif choice == 5:
            n = int(input("Enter the number: "))
            print(f"{n} is a Sublime Number: {is_sublime_number(n)}")
        elif choice == 6:
            n = int(input("Enter the number: "))
            print(f"{n} is a Smith Number: {is_smith_number(n)}")
        elif choice == 7:
            limit = int(input("Enter the limit for lucky numbers: "))
            print(f"Lucky Numbers up to {limit}: {lucky_numbers(limit)}")
        elif choice == 8:
            n = int(input("Enter the number: "))
            print(f"{n} is a Pandigital Number: {is_pandigital(n)}")
        elif choice == 9:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
