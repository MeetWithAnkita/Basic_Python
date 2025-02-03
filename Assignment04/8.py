import re
from datetime import datetime

def is_valid_date_shorthand(date_str):
    try:
        day, month, year = map(int, date_str.split('/'))
        datetime(year, month, day)  # Validate using datetime
        return True
    except ValueError:
        return False

def is_valid_date_longhand(date_str):
    try:
        # Remove 'st', 'nd', 'rd', 'th' from the day part
        match = re.match(r"(\d+)(st|nd|rd|th)? (\w+), (\d{4})", date_str)
        if not match:
            return False
        day, _, month, year = match.groups()
        day = int(day)
        year = int(year)
        # Map the month name to its number
        month = datetime.strptime(month, "%B").month
        datetime(year, month, day)  # Validate using datetime
        return True
    except (ValueError, AttributeError):
        return False

def validate_date(date_str):
    if '/' in date_str:  # Shorthand format
        return is_valid_date_shorthand(date_str)
    elif re.search(r"\d+(st|nd|rd|th)? \w+, \d{4}", date_str):  # Longhand format
        return is_valid_date_longhand(date_str)
    return False

# Test cases
dates = [
    "19/7/2019",    # Valid shorthand
    "14/13/2019",   # Invalid shorthand
    "19th July, 2019",  # Valid longhand
    "32nd July, 2019",  # Invalid longhand
    "14th Month, 2019", # Invalid longhand
]

for date in dates:
    result = "Valid" if validate_date(date) else "Invalid"
    print(f"{date} => {result}")
