# 2. To determine the simple interest on a given amount of money at a
# given rate of interest for a given period of time.

# Simple interest = (P * R * T)/100 
# P means principle 
# R means rate of interest in percentage
# T means time (year)

principle = eval(input("Enter the priciple amount :"))
rate = eval(input("Enter the rate of interest in percentage(%) :"))
time = eval(input("Enter the period of time (year) :"))
SI = (principle*rate*time)/100
total_amount= SI + principle

print(f"Simple Interest on {principle} at {rate}% of interest for {time}year is: {SI}")
print(f"Total amount is: {total_amount}")