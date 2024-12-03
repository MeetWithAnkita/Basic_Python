# 10. To find out the list of months with a Friday the 13th for any given
# year.
from datetime import date

def friday_the_13ths(year):
    """Find months with a Friday the 13th for a given year."""
    months_with_friday_13th = []
    for month in range(1, 13):  # Iterate through months 1 to 12
        if date(year, month, 13).weekday() == 4:  # Check if the 13th is a Friday (4 means Friday)
            months_with_friday_13th.append(month)
    return months_with_friday_13th

# Example usage:
year = int(input("Enter the year: "))
months = friday_the_13ths(year)

if months:
    print(f"Months with a Friday the 13th in {year}:")
    for month in months:
        print(f"{month} - {date(year, month, 1).strftime('%B')}")
else:
    print(f"No Friday the 13ths in {year}.")
