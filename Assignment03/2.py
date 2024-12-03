# 2. To obtain all the whole numbers which are divisible by some given
# p but not by some other given q.

WN = int(input("Enter the range of whole number :"))
p = int(input("Enter the no which can devide the whole no :"))
q = int(input("Enter the no which can't devide the whole no :")) 

print(f"{WN} which are devisible by {p} but not {q} is :")
for i in range(0, WN+1):
    if ( (i%p == 0) and (i%q != 0) ) :
        print(f"{i}")