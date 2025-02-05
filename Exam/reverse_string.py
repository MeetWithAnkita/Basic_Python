str = input("Enter a sentance :")

# using slicing 
rev_str = str[::-1]
print("Reserse String (using slicing) :",rev_str)

# built-in-function 
rev_str2 = ''.join(reversed(str))
print("Reserse String (using build-in-function) :",rev_str2)

# using iteration
temp=" "
for i in str :
    temp= i + temp 
print("Reserse String (using iteration) :",temp)