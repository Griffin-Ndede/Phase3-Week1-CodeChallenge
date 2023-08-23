#  to convert pm to 24hr add 12 to the hour if it is between 1 and 11
# to convert am to 24hr change 12 to 0 and leave it as it is if hour is between 1 and 11

def hour_converter(hour, minute, period):
    if period == "am" and hour == 12:
        hour = 0
    elif period == "pm" and hour != 12:
        hour += 12

    # format the hour and minutes to strings
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)

    return hour_str + minute_str

print(hour_converter(1,35,"am"))