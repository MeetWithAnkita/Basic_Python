num = int(input("Enter the number to perform the factorial :"))
fact = 1
for i in range(1, num+1) :
    fact = fact * i
print(f"factorial of {num} is {fact}")
