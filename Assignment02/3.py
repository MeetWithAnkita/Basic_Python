# 3. To determine the absolute difference between a given number and
# 123 and if it is greater than 123 then print the triple of the given number.

num = eval(input("Enter the number :"))
diff = abs(num - 123)
if (diff > 123) :
    print(f"Difference is greater than 123.\nSo,3 * {num} = {num*3}")
else:
    print("Difference is equal or lesser than 123.")    