while True:
    num1,num2 = input("Enter two number to perform operation (separate by (,)):").split(',')
    num1 = eval(num1); num2 = eval(num2)
    print("Menu..........\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for devision\n5 for modulo\n 6 for power")
    choice = int(input("Enter number between 1 to 6: "))
    if choice == 1 :
        print(f"{num1} + {num2} = {num1+num2}")
    elif choice == 2 :
        print(f"{num1} - {num2} = {num1-num2}")
    elif choice == 3 :
        print(f"{num1} * {num2} = {(num1*num2)}")
    elif choice == 4 :
        print(f"{num1} / {num2} = {num1//num2}")    
    elif choice == 5 :
        print(f"{num1} % {num2} = {num1%num2}")    
    elif choice == 6 :
        print(f"{num1} ** {num2} = {num1**num2}")
    else :
        print("Wrong choice....")
    yes = input("Are you want to perform repatedly : (if yes press y)")
    if yes == 'y' :
        continue 
    else :
        break 

