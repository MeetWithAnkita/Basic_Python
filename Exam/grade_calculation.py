no_of_sub= int(input("enter the no of subjects :"))
sum = 0 
for i in range (1,no_of_sub+1) :
    no = eval(input(f"No of Subject-{i} :"))
    sum += no 
avg_no = sum / no_of_sub
if 100>= avg_no >80 :
    print("Grade A")    
elif 80>= avg_no >60 :
    print("Grade B")    
elif  60>= avg_no >40 :
    print("Grade C")    
else :
    print("Grade D")    
    
