lower, upper = input("Enter the lower and upper range :(split by space)").split(' ')
lower = int(lower); upper = int(upper)
prime= []; non_prime=[]
for i in range (lower, upper + 1):
    if i < 2 :
        non_prime.append(i)
        continue
    is_prime= True #prime 
    
    for j in range(2,(i//2)+1):
        if i % j == 0 :
            non_prime.append(i)
            is_prime = False
            break
                
    if is_prime :
        prime.append(i)

print(f"From {lower} to {upper}..\nThe prime nos are :{prime}\nThe non_prime nos are :{non_prime}")
