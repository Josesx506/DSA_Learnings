def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#     """Returns the number of days between year1/month1/day1
#        and year2/month2/day2. Assumes inputs are valid dates
#        in Gregorian calendar, and the first date is not after
#        the second. 
#        My implementation. The helper function is supposed to return a boolean if
#        days can exist between 2 days"""
        
#     # YOUR CODE HERE!
#     if (year2, month2, day2) > (year1, month1, day1):
#         day_count = 0
#         new_day_value = (year1, month1, day1)
#         while new_day_value < (year2, month2, day2):
#             new_day_value = nextDay(new_day_value[0],new_day_value[1],new_day_value[2])
#             day_count += 1
#         return day_count
#     else:
#         return None


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """
    Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False.
    Default Udacity Solution that doesn't check for erroneous dates
    """
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


# def dateIsBefore(year1, month1, day1, year2, month2, day2):
#     """
#     Returns True if year1-month1-day1 is before year2-month2-day2. 
#     Otherwise, returns False.
#     Modified Udacity solution by me to throw assertion errors
#     """
    
#     assert year1 <= year2, "The first date should be before the second date"
#     if year1 < year2:
#         return True
    
#     if year1 == year2:
        
#         assert month1 <= month2, "The first date should be before the second date"
#         if month1 < month2:
#             return True
        
#         if month1 == month2:

#             assert day1 <= day2, "The first date should be before the second date"
#             return day1 < day2
#     return False


# Testing code -- do not change
def codeTest(year1, month1, day1, year2, month2, day2, answer):
    try:
        result = daysBetweenDates(year1, month1, day1, year2, month2, day2)
        if result == answer and answer != "AssertionError":
            return "correct"
        else: 
            return "incorrect", answer
    
    except AssertionError:
        if answer == "AssertionError":
            return "correct AssertionError"
        else:
            return "incorrect AssertionError"


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    
    # A cleaner way to include the AssertionError is to raise the error if the reversed input is not valid
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)

    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days 


# Tests
test_1 = daysBetweenDates(2012,9,30,2012,10,30)
test_2 = daysBetweenDates(2012,1,1,2013,1,1)
test_3 = daysBetweenDates(2012,9,1,2012,9,4)


# Tests for invalid date comparison
test_1 = codeTest(2012,9,30,2012,10,30, 30)
test_2 = codeTest(2012,1,1,2013,1,1,360)
test_3 = codeTest(2012,9,1,2012,9,4,3)
test_4 = codeTest(2013,1,1,1999,12,31, "AssertionError")
