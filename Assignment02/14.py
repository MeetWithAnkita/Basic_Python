# 14. In a certain area, the parking charge for cars is calculated according
# to the following rules: For the first 8.5 hours or part thereof, the
# rate is fixed and it is equal to Rs. 55; for the next every 2 hours
# or part thereof up to a maximum of 23 hours, the rate Rs. 13.75;
# beyond the 23 hours limit, the charge Rs. 5.50 for every minute.
# Develop a Python script to calculate the parking charge for the
# users of the area.

#  first 8.5h(510 min) ==> fixed rate = 55
#  next every 2 h ,max 23 h ==> rate per hour = 13.75
#  then ==> rate per minite = 5,50

parking_hour = eval(input("Enter the parking hour(in hour) :"))
parking_time = parking_hour * 60


if (parking_hour <= 8.5) :
    rate = 55 
elif ( 23 > parking_hour > 8.5) :
    rate = 55 + ((parking_hour - 8.5) * (13.75/2))        
else :
    rate = 55 + ((23 - 8.5) * (13.75/2)) + ((parking_hour - 23) * 60 * 5.50)

print("Parking charge =",rate)