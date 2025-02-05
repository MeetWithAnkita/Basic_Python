turm = int(input("Enter the turm number :"))
n0 = 0 ;  n1=1
print(n0,n1,end=',')
for i in range (3,turm+1):
    n3 = n0 + n1 
    print(n3,end=',')
    n0= n1
    n1 = n3
    