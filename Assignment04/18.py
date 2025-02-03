def is_harshad_number(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0

def is_multiple_harshad_number(num):
    while num > 9:  
        if not is_harshad_number(num):
            return False
        num = sum(int(digit) for digit in str(num))  
    return is_harshad_number(num)  

try:
    number = int(input("Enter a number to check if it is a Multiple Harshad Number: "))

    if number <= 0:
        print("Please enter a positive integer.")
    else:
        if is_multiple_harshad_number(number):
            print(f"{number} is a Multiple Harshad Number.")
        else:
            print(f"{number} is not a Multiple Harshad Number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
