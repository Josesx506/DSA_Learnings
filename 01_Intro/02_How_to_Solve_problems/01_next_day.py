# Define a simple nextDay procedure, that assumes every month has 30 days.

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if day < 30:
        day = day + 1
    elif day == 30 and month < 12:
        day = 1
        month = month + 1
    elif day == 30 and month == 12:
        day = 1
        month = 1
        year = year + 1
     
    return (year, month, day)


# def nextDay(year, month, day):
#     """ Warning: this version assumes every month has 30 days [Udacity Solution]"""
#     if day < 30:
#         return year, month, day + 1
#     else:
#         if month < 12:
#             return year, month + 1, 1
#         else:
#             return year + 1, 1, 1


# Tests
new_day = nextDay(2022, 5, 11)
new_month = nextDay(2022, 6, 30)
new_year = nextDay(2022, 12, 30)
