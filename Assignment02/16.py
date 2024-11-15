# 16. It is required to print the name of the starting day of any given year
import datetime

def get_starting_day_of_year(year):
    start_date = datetime.date(year, 1, 1)
    day_name = start_date.strftime("%A") 
    return day_name

year = int(input("Enter the year: "))
starting_day = get_starting_day_of_year(year)
print(f"The starting day of the year {year} is: {starting_day}")
