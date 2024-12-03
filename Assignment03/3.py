# 3. To generate a table of any given number n.

no = int(input("Enter the number :"))
for i in range(0,11):
    mul = no * i
    print(f"{no}*{i} = {mul}")