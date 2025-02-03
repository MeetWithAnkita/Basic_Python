import datetime

def months_with_saturday_13th(year):
    months_with_saturday = []
    for month in range(1, 13): 
        date = datetime.date(year, month, 13)
        if date.weekday() == 5:
            months_with_saturday.append(date.strftime('%B'))  
    return months_with_saturday
year = int(input("Enter the year: "))
months = months_with_saturday_13th(year)
if months:
    print(f"\nMonths with a Saturday the 13th in {year}:")
    for month in months:
        print(month)
else:
    print(f"\nThere are no months with a Saturday the 13th in {year}.")
