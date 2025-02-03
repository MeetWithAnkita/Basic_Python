# Prompt for integer input
num = int(input("Enter an integer: "))
# Find factors
factors = [i for i in range(1, num + 1) if num % i == 0]
print("Factors of", num, "are:", factors)