# 8. To calculate commission of a salesman when the calculation of commission is based on the rules given below :
# (a) Nil, when the sales <10000 in region A
# (b) 6.5% of the sales if the sales <15000 in region B and <16000 in region A
# (c) 8.5% plus Rs.1500, if the sales >=15000 but <25000 in region B and >=16000 but <35000,in region A.
# (d) 11% of the sales plus Rs.4500 for all regions for all other cases.

sales = eval(input("Enter the sales of salesman :"))
region = input("Enter the region (A or B):").upper()
commission = 0
if (region == "A"):
    if sales < 10000:
        commission = 0
    elif 10000 <= sales < 16000 :    
        commission += sales * (6.5 / 100)
    elif ( (sales >= 1600) and (sales<35000)):
        commission += 1500 + (sales * (8.5 /100))
    else :
        commission += ( sales * (11/100) ) + 4500 
else:
    if sales < 15000 :
        commission += sales * (6.5/100)
    elif 15000<= sales <25000 :
        commission += 1500 + (sales * (8.5 /100))     
    else :
        commission += ( sales * (11/100) ) + 4500   

print("The commission is :",commission)               
            