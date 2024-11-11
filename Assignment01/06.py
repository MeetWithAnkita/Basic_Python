# 6. To determine the value of an exponential expression of the form a^b
# on the basis of a given base and the power to be raised.

base = eval(input("Enter the base value :"))
power = eval(input("Enter the power :"))
result = pow(base,power)
print(f"{base}^{power} = {result:.4f}")