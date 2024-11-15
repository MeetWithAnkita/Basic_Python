# 13. In a certain country, the difference between two consecutive gas
# meter readings gives the amount of gas consumed in cubic feet. It
# is then multiplied by a factor 1.475 to convert it into the number
# of therms used by the consumer, where therm is the unit of billing.
# The meter readings are collected at the end of each month. The
# following rate chart is then used by the gas company to calculate
# the bill amount of each consumer:
# No. of therms used                       Rate per therm
#      <=125                                   Rs.7.75
#   >125 but <=250                   Rs. 9.75 plus a surcharge of 1.25% over the calculated charge;
#       >250                         Rs. 13.00 plus a surcharge 0f 2.5% over the calculated charge.
# A meter rent of Rs.25 is also added to the gas charges of each
# consumer to determine the gas bill. If the gas meters display 8-digit
# readings, then develop a script in Python is required to determine
# the monthly gas bill of the consumers.

previous_gas_reading = eval(input("Enter the previous gas reading in 8 digit :"))
currenr_gas_reading = eval(input("Enter the current gas reading :"))
gas_consumed_in_cubic_feet = currenr_gas_reading - previous_gas_reading
print("gas_consumed_in_cubic_feet = ",gas_consumed_in_cubic_feet)
no_of_therms = 1.475 * gas_consumed_in_cubic_feet
print("no_of_therms :",no_of_therms)


meter_rent  =25

if no_of_therms <= 125 :
    bill = no_of_therms*7.75
elif 125 < no_of_therms <= 250 :
    bill = (no_of_therms * 9.75) 
    bill += (bill * (1.25/100))
else:
    bill = (no_of_therms *13.00)
    bill += (bill * (2.5/100))
    
print("The monthlt gas bill of a consumer is :",(bill + meter_rent ))    
