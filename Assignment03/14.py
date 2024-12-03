import math
from itertools import chain, combinations

# Helper functions
def sum_of_digits(number):
    return sum(int(d) for d in str(number))

def product_of_digits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Functions for specific number types
def is_harshad(number):
    return number % sum_of_digits(number) == 0

def is_abundant(number):
    divisors_sum = sum(i for i in range(1, number // 2 + 1) if number % i == 0)
    return divisors_sum > number

def is_weird(number):
    divisors = [i for i in range(1, number // 2 + 1) if number % i == 0]
    divisors_sum = sum(divisors)
    if divisors_sum <= number:
        return False
    for subset in chain.from_iterable(combinations(divisors, r) for r in range(len(divisors) + 1)):
        if sum(subset) == number:
            return False
    return True

def is_amicable(a, b):
    return (sum_of_divisors(a) == b and sum_of_divisors(b) == a and a != b)

def sum_of_divisors(number):
    return sum(i for i in range(1, number // 2 + 1) if number % i == 0)

def is_automorphic(number):
    return str(number ** 2).endswith(str(number))

def fermat_number(n):
    return 2 ** (2 ** n) + 1

def is_happy(number):
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(d) ** 2 for d in str(number))
    return number == 1

def is_special_two_digit(number):
    if 10 <= number <= 99:
        digits = [int(d) for d in str(number)]
        return sum(digits) + (digits[0] * digits[1]) == number
    return False

def perfect_square_adjustment(number):
    root = math.isqrt(number)
    if root ** 2 == number:
        return 0
    return (root + 1) ** 2 - number

def is_neon(number):
    return sum_of_digits(number ** 2) == number

def is_coprime(a, b):
    return math.gcd(a, b) == 1

def product_of_successors(number):
    product = 1
    for digit in str(number):
        if int(digit) % 2 == 0:
            product *= (int(digit) + 1)
    return product

def is_pronic(number):
    for i in range(1, int(number ** 0.5) + 1):
        if i * (i + 1) == number:
            return True
    return False

def is_twisted_prime(number):
    return is_prime(number) and is_prime(int(str(number)[::-1]))

def is_duck(number):
    return '0' in str(number)[1:]

def is_spy(number):
    return sum_of_digits(number) == product_of_digits(number)

def is_sunny(number):
    return math.isqrt(number + 1) ** 2 == number + 1

def tribonacci_sequence(n):
    sequence = [1, 1, 2]
    while len(sequence) < n:
        sequence.append(sum(sequence[-3:]))
    return sequence

def series_sum(n):
    return sum(sum(range(1, i + 1)) for i in range(1, n + 1))

# Main program
def main():
    while True:
        print("\nNumber Property Checker")
        print("1. Harshad Number")
        print("2. Abundant Number")
        print("3. Weird Number")
        print("4. Amicable Numbers")
        print("5. Automorphic Number")
        print("6. Fermat Number")
        print("7. Happy Number")
        print("8. Special Two-Digit Number")
        print("9. Perfect Square Adjustment")
        print("10. Neon Number")
        print("11. Co-prime Numbers")
        print("12. Product of Successors of Even Digits")
        print("13. Pronic Number")
        print("14. Twisted Prime")
        print("15. Duck Number")
        print("16. Spy Number")
        print("17. Sunny Number")
        print("18. Tribonacci Sequence")
        print("19. Series Sum")
        print("20. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            number = int(input("Enter the number: "))
            print(f"{number} is a Harshad Number: {is_harshad(number)}")
        elif choice == 2:
            number = int(input("Enter the number: "))
            print(f"{number} is an Abundant Number: {is_abundant(number)}")
        elif choice == 3:
            number = int(input("Enter the number: "))
            print(f"{number} is a Weird Number: {is_weird(number)}")
        elif choice == 4:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"({a}, {b}) are Amicable Numbers: {is_amicable(a, b)}")
        elif choice == 5:
            number = int(input("Enter the number: "))
            print(f"{number} is an Automorphic Number: {is_automorphic(number)}")
        elif choice == 6:
            n = int(input("Enter n for Fermat Number (n >= 0): "))
            print(f"Fermat Number F{n} is: {fermat_number(n)}")
        elif choice == 7:
            number = int(input("Enter the number: "))
            print(f"{number} is a Happy Number: {is_happy(number)}")
        elif choice == 8:
            number = int(input("Enter the two-digit number: "))
            print(f"{number} is a Special Two-Digit Number: {is_special_two_digit(number)}")
        elif choice == 9:
            number = int(input("Enter the number: "))
            adjustment = perfect_square_adjustment(number)
            if adjustment == 0:
                print(f"{number} is a Perfect Square.")
            else:
                print(f"Least number to add: {adjustment}")
        elif choice == 10:
            number = int(input("Enter the number: "))
            print(f"{number} is a Neon Number: {is_neon(number)}")
        elif choice == 11:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"({a}, {b}) are Co-prime Numbers: {is_coprime(a, b)}")
        elif choice == 12:
            number = int(input("Enter the number: "))
            print(f"Product of successors of even digits: {product_of_successors(number)}")
        elif choice == 13:
            number = int(input("Enter the number: "))
            print(f"{number} is a Pronic Number: {is_pronic(number)}")
        elif choice == 14:
            number = int(input("Enter the number: "))
            print(f"{number} is a Twisted Prime: {is_twisted_prime(number)}")
        elif choice == 15:
            number = int(input("Enter the number: "))
            print(f"{number} is a Duck Number: {is_duck(number)}")
        elif choice == 16:
            number = int(input("Enter the number: "))
            print(f"{number} is a Spy Number: {is_spy(number)}")
        elif choice == 17:
            number = int(input("Enter the number: "))
            print(f"{number} is a Sunny Number: {is_sunny(number)}")
        elif choice == 18:
            n = int(input("Enter the number of terms: "))
            print(f"Tribonacci Sequence: {tribonacci_sequence(n)}")
        elif choice == 19:
            n = int(input("Enter the number of terms: "))
            print(f"Series Sum: {series_sum(n)}")
        elif choice == 20:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
