num1 , num2 = input("Enter two number (separated by (,)):").split(',')
num1 = eval(num1); num2 = eval(num2)
print(f"Before swap :\nnum1 is {num1} and num2 is {num2}")
num1, num2 = num2, num1 
print(f"After swap :\nnum1 is {num1} and num2 is {num2}")


# anothe type 
num1 , num2 = input("Enter two number (separated by (,)):").split(',')
num1 = eval(num1); num2 = eval(num2)
print(f"Before swap :\nnum1 is {num1} and num2 is {num2}")
num1 = num1 + num2 
num2 = num1 - num2
num1 = num1 - num2
print(f"After swap :\nnum1 is {num1} and num2 is {num2}")
