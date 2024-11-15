# 11. To compute the festival bonus of the employees on the basis of the
# basic pay and the designation as per the following rules:
# Basic Pay             Designation             Percentage of basic pay payable
# <40,000                Manager        12% of the basic pay subject to minimum of Rs. 2500
# >=40,000               Manager        16% of the basic pay subject to maximum of Rs. 7500
# <20,000                Officer      14% of the basic pay subject to a minimum of Rs.2500 and a maximum of Rs.5000.
# For all others cases   Whatever                  8.9% of basic pay

designation = input("What is your designation (Manager / Officer / any other maintion) :").upper()
basic_pay = eval(input("Enter the basic pay :"))

if designation == "MANAGER" :
    if basic_pay < 40000 :
        money = basic_pay * (12/100)
        if money < 2500 :
            bonus = 2500
        else :
            bonus = money     

    elif basic_pay >= 40000 :
        money = basic_pay * (16/100)        
        if money > 7500 :
            bonus = 7500
        else :
            bonus = money
   
elif designation == "OFFICER" :
    if basic_pay < 20000 :
        money = basic_pay * (14/100)
        if money < 2500 :
            bonus = 2500
        elif money > 5000 :
            bonus = 5000    
        else :
            bonus = money

else :
    bonus = basic_pay * (8.9/100)

print("Banous :",bonus)
                
