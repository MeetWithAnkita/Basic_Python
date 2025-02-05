str = input("Enter a sentence :")
str1 = 'aeiouAEIOU'
count = 0 
for i in str :
    if i in str1 :
        count += 1 
print(f"Total of vowels in '{str}' is {count}")        