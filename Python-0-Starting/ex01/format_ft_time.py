import time

timestamp = time.time() # is used to get the time in seconds since epoch (January 1, 1970, 00:00:00 (UTC))

# Print the Unix timestamp in scientific notation
print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")

formatted_date = time.strftime("%b %d %Y", time.gmtime(timestamp))
# time.gmtime() method is used to convert a time expressed in seconds since
#   the epoch to a time.struct_time object in UTC

# print(time.gmtime(timestamp)) - looks like dictionary

# strftime() function lets us convert a datetime object into a formatted string using special format codes.
#   These format codes represent different parts of the date and time-like year, month, weekday, hour, etc.
#       %Y gives the full year, %m gives the month, %d gives the day.
#       %H:%M:%S returns the hour, minute, and second in 24-hour time format.
#       %a and %A represent the short and full weekday names.
#       %I %p %S shows 12-hour time with seconds and AM/PM.
#       %j represents the day of the year (001 to 366).

# Print the formatted date
print(formatted_date)
