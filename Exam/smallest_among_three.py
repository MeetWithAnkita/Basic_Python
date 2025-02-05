num1, num2, num3 = input("Enter three number :(separated by (,)): ").split(',')
num1 = eval(num1); num2 = eval(num2); num3 = eval(num3)
if (num1 < num2 ):
    if (num1 < num3):
        print("Smallest is :",num1)
    else :
        print("Smallest is :",num3)
elif (num2 < num1 ) :
    if (num2 < num3 ):
        print("Smallest is :",num2)
    else:
        print("Smallest is :",num3)                
else :
    print("Smallest :",num3)        
