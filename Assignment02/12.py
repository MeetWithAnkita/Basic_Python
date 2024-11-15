# 12. For the first 75 calls, the charge is fixed and it is equal to Rs. 75;
# for the next 75 calls, the charge is calculated @Rs 0.75 per call; for
# the next 90 calls, the charge is Rs.0.65 per call and for the rest,
# if any, the rate is Rs.0.55 per call. It is required to determine the
# monthly bill of a subscriber.

# 1st 75 calls ==>> 75rs
# next 75 calls => [75 < no of calls <=  150 calls]  ==>> 0.75rs per call
# next 90 calls => [150 < no of calls <= 240 calls ]  ==>> 0.65rs per call
# rest of calls => [240 < no of calls <<                   ]  ==>> 0.55rs per call


no_of_calls = int(input("Enter the no of calls :"))
if no_of_calls <= 75 :
    charge = 75
elif no_of_calls <= 150:    
    charge = 75 + (no_of_calls - 75) * 0.75     
elif no_of_calls <=240 :
    charge = 75 + 75 * 0.75 + (no_of_calls - 150) * 0.65
else :
    charge = 75 + 75 * 0.75 +  90 * 0.65 + (no_of_calls-240) * 0.55     

print(f"The monthly bill : {charge}")    