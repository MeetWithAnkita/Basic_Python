while True :
    print("If you try to convert Celcius to farenhite ...press C\n else  press F....")
    choice = input("Enter C or F :") 
    if choice == 'C' :
        celcius = eval(input("Enter the temperature in celcius :"))
        farenhite = ((celcius//5)*9)+32
        print(f"{celcius}C = {farenhite}F")
    else :
        farenhite = eval(input("Enter the temperature in celcius :"))
        celcius = ((farenhite-32)//9)*5
        print(f"{farenhite}F = {celcius}C")

    yes = input("For or more try press y")
    if yes == 'y':
        continue
    else :
        break 



