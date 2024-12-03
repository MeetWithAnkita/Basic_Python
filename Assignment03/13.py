# 13. A program is required which will accept a date in either long hand
# or short hand (e.g. either 19/7/2019 or 19th July, 2019 ) with a view
# to determine if the given date is valid. e.g. 14/13/2019 is clearly
# not valid.
from datetime import datetime

def validate_date(date_input):
    # Define possible date formats
    date_formats = [
        "%d/%m/%Y",  # Shorthand: 19/7/2019
        "%d %B, %Y",  # Longhand: 19 July, 2019
        "%d%B, %Y",  # Longhand without space: 19thJuly, 2019
        "%d%B,%Y"  # Longhand without space: 19thJuly,2019
    ]
    
    # Remove suffixes like "st", "nd", "rd", "th" from day
    suffixes = ['st', 'nd', 'rd', 'th']
    for suffix in suffixes:
        if suffix in date_input:
            date_input = date_input.replace(suffix, '')

    # Attempt to parse the date with each format
    for date_format in date_formats:
        try:
            datetime.strptime(date_input, date_format)
            return True  # Valid date
        except ValueError:
            continue

    return False  # Invalid date

# Input from user
date_input = input("Enter a date (e.g., 19/7/2019 or 19th July, 2019): ")

# Validate the date
if validate_date(date_input):
    print(f"The date '{date_input}' is valid.")
else:
    print(f"The date '{date_input}' is invalid.")