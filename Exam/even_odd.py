lower, upper = input("Enter the lower and upper range (split by comma(,)):").split(',')
lower = int(lower); upper = int(upper)
even=[] ; odd=[]

for i in range (lower , upper+1 ):
    if i % 2 == 0 :
        even.append(i)
    else :
        odd.append(i)   

print("The list of even number :",even)
print("The list of odd number :",odd)
        