# 13. To determine the acceleration due to gravity on the basis of the
# effective length of a simple pendulum.
# g= (4 * π^2 * L ) / T^2
# g = acceleration due to gravity (in m/s^2)
# L = effective length of the pendulum (in meters)
# T = period of oscillation (in seconds)
pi = (22/7)
lenth_of_pendulam = eval(input("Enter the length of pendulam(in meters) :"))
period_of_oscillation = eval(input("Enter the period of oscillation(in second) :"))
gravity = (4 * (pow(pi,2)) * lenth_of_pendulam) / (pow(period_of_oscillation,2))

print(f"The resulted acceration to gravity is :{gravity:.5f} m/s^2")