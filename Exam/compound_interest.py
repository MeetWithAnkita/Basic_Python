principal  = eval(input("Enter the principal amount :"))
r = eval(input("Annual interest rate :"))
n = eval(input("No of times interest is compounded per year :"))
t= eval(input("times in year :"))

r= r/100
amount = principal*(pow( (1+(r/n)),(n*t) ))
print(amount)
CI = amount-principal
print("The compound interest is :",CI)
