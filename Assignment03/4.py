# 4. To obtain all the groups of three successive numbers within 1000
# that have the property that the square of the middle one is greater
# by unity than the product of the other two numbers. For example,
# 18^2 =17*19+1

print("The list is :\n")
no = 1000
for a in range(0,no-2):
    b= a+1
    c= a+2
    if b**2 == (a * c + 1) :
        print(f"({a},{b},{c})")