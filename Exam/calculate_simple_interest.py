p = eval(input("Enter the principle :"))
ROI = eval(input("Enter the rate of interest :"))
time = eval(input("Enter the time in year :"))
SI = (p * ROI * time) // 100
print(f"Simple Interest is :{SI}")