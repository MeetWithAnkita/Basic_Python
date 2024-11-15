# 2. To determine greater between two numbers.
num1 , num2 = input("Enter the two number (separated by comma(,)) :").split(',')
num1 = eval(num1)
num2 = eval(num2)

if (num1 > num2) :
    {
        print(f"{num1} is the biggest number.")
    }
else :
    {
        print(f"{num2} is the biggest number.")
    }    