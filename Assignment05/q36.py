# Time zone offsets in hours relative to Eastern
time_zones = {"Eastern": 0, "Central": -1, "Mountain": -2, "Pacific": -3}

# Input the time and zones
time = input("Enter time (e.g., 3:48pm): ").strip().lower()
from_zone = input("Enter starting time zone: ").capitalize()
to_zone = input("Enter ending time zone: ").capitalize()

if from_zone in time_zones and to_zone in time_zones:
    offset = time_zones[to_zone] - time_zones[from_zone]

    # Extract hours and minutes
    is_pm = "pm" in time
    hour, minute = map(int, time[:-2].split(":"))
    if is_pm and hour != 12:
        hour += 12
    if not is_pm and hour == 12:
        hour -= 12

    # Convert time
    total_minutes = (hour * 60 + minute + offset * 60) % (24 * 60)
    new_hour, new_minute = divmod(total_minutes, 60)

    # Format the result
    period = "am" if new_hour < 12 else "pm"
    new_hour = new_hour % 12 or 12
    print(f"Time in {to_zone}:", f"{new_hour}:{new_minute:02d}{period}")
else:
    print("Invalid time zones.")