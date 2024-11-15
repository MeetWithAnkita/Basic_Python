# 7. To print the number of days in each month of a given year
import calendar

def print_days_in_months(year):
    
    for month in range(1, 13):
        _, num_days = calendar.monthrange(year, month)
        month_name = calendar.month_name[month]
        print(f"{month_name}: {num_days} days")

# Example usage
year = int(input("Enter the year: "))
print_days_in_months(year)
