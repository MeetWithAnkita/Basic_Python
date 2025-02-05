str = input("Enter a sentence :").upper()
letter = input("Enter a letter which you want to count :").upper()
count = 0 
for i in str :
    if i == letter :
        count +=1 
print(f"{letter} has in the '{str}' {count} times")        