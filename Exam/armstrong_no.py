num = int(input("Enter a number :"))
no = num 
order = len(str(num))
sum = 0 
while num != 0 :
    rem = num % 10 
    sum = sum + pow(rem,order)
    num = num//10

if sum == no :
    print("It is an armstrong no .")
else :
    print("It's not an armstrong no.")    

