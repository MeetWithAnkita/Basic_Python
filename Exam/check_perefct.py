# A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).

# num = int(input("Enter a number :"))
# no = num
# sum = 0 
# print("All devisiors are :")
# for i in range (1,num):
#     if num % i == 0 :
#         sum = sum + i   
#         print(i)

# if sum == no :
#     print(f"{no} is perfect ")
# else :
#     print(f"{no} is not the perfect number .")    


lower, upper = input("Enter the lower and upper range :(split by space)").split(' ')
lower = int(lower); upper = int(upper)
perfect= []; non_perfect=[]
for j in range (lower, upper+1) : 
    num = j 
    sum = 0 

    for i in range (1,num):
        if num % i == 0 :
            sum = sum + i   
    if sum == j :
        perfect.append(j)
    else :
        non_perfect.append(j)

print("The perfect numbers are : ",perfect,"\n and non perfect numbers are : ",non_perfect)

