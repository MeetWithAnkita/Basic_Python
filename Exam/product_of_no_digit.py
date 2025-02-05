num = int(input("Enter a number :"))
no = num
product = 1 
while num != 0 :
    rem = num % 10
    product *= rem 
    num = num //10

print(f"Product of {no}'s digit is {product}")