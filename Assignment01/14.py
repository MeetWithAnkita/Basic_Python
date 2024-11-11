# 14. To determine the volume a certain mass of gas at a given temperature and pressure when the volume is 
# known at the normal pressure and at the absolute temperature

# (p1 * v1) / t1  = (p2 * v2) / t2
# v2= (p1 * v1 * t2) / (t1 * p2)

p1,p2 = input("Enter the initial and final pressure of gas(atm)separated by space) :").split()
v1= input("Enter the initial volume of gas(liter): ")
t1,t2= input("Enter the initial and final temperature of gas(Kelvin)(separated by space) :").split()
p1 = eval(p1)
p2 = eval(p2)
v1 = eval(v1)
t1 = eval(t1)
t2 = eval(t2)

v2 = (p1 * v1 * t2)/(t1 * p2)
print(f"The final volume of {t2}Kelvin temperature is :{v2:.2f} L")