# 1. To obtain the sum of the first n natural numbers for some given n
# without using any formula.

n = int(input("Enter the range of natural numer :"))
sum = 0 
for i in range (0,n+1):
    sum+=i
print(f"Sum of first {n} natural number :{sum}")    