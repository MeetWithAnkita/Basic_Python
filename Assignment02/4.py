# 4. To validate a given date
from datetime import datetime

def validate_date(date_string, date_format="%y-%m-%d"):
    try:
        valid_date = datetime.strptime(date_string, date_format)
        return True  
    except ValueError:
        return False  


date_string = input("Give the date is (Format :year-month-day) :")
if validate_date(date_string):
    print(f"{date_string} is a valid date.")
else:
    print(f"{date_string} is not a valid date.")
