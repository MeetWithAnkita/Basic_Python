# 15. To determine the net salary of an employee when it is known that
# the employee is eligible to dearness allowance (DA) of 97% of the
# basic pay, House Rent Allowance (HRA) of 57% of the basic pay
# and medical allowance of Rs.150 . It is further known that 12% of
# the basic pay is deducted from the gross salary for the Employees’
# Provident fund (EPF) and Rs. 200 is deducted from the gross pay
# as the professional tax.

# B = basic salary 
# DA = B * 0.97
# HRA = B * 0.57
# Medical allowance = 150
# gross pay = B + DA + HRA + Medical allowance

# EPF = B * 0.12
# professional tax = 120 
# The Net salary = gross pay - (EPF + professional tax)

basic_salary = eval(input("Enter the basic salary is :"))
DA = basic_salary * 0.97
HRA = basic_salary * 0.57
Medical_allowance= 150
EPF= basic_salary * 0.12
professional_tax = 200

Gross_salary = basic_salary + DA + HRA + Medical_allowance
The_net_salary = Gross_salary - (EPF + professional_tax)

print("The Net salary is :",The_net_salary)
