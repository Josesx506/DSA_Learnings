def nextDay(year, month, day, daysInMonth):
    """Modified version: works for variation in month days"""
    if day < daysInMonth:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def isLeapYear(year_val):
    """Check if a year is a leap year or not"""
    if year_val % 400 == 0:
        return True
    if year_val % 100 == 0:
        return False
    if year_val % 4 == 0:
        return True
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    
    # List the days in a month for the different types of year
    monthDayCountsRegular = [31,28,31,30,31,30,31,31,30,31,30,31]
    monthDayCountsLeap = [31,29,31,30,31,30,31,31,30,31,30,31]
       
    # Throw an AssertionError if the input is not valid
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        if isLeapYear(year1):
            month_days = monthDayCountsLeap[month1-1]
            year1, month1, day1 = nextDay(year1, month1, day1, month_days)
            days += 1
        else:
            month_days = monthDayCountsRegular[month1-1]
            year1, month1, day1 = nextDay(year1, month1, day1, month_days)
            days += 1 
    return days

# Testing code -- do not change
def codeTest(year1, month1, day1, year2, month2, day2, answer):
    try:
        result = daysBetweenDates(year1, month1, day1, year2, month2, day2)
        if result == answer and answer != "AssertionError":
            return "correct"
        else: 
            return "incorrect"
    
    except AssertionError:
        if answer == "AssertionError":
            return "correct AssertionError"
        else:
            return "incorrect AssertionError"


# Tests
test_1 = codeTest(2012,1,1,2012,2,28,58)
test_2 = codeTest(2012,1,1,2012,3,1,60)
test_3 = codeTest(2011,6,30,2012,6,30,366)
test_4 = codeTest(2013,1,1,1999,12,31, "AssertionError")
test_5 = codeTest(2011,1,1,2012,8,8,585)
test_6 = codeTest(1991,3,1,1991,1,3,"AssertionError")
test_7 = codeTest(2012,2,1,2012,3,1,29)
test_8 = codeTest(1900,1,1,1999,12,31,36523)

def test_validity(year1, month1, day1, year2, month2, day2):
    from datetime import datetime
    date1 = datetime(year1, month1, day1)
    date2 = datetime(year2, month2, day2)
    python_days = (date2 - date1).days

    implementation_days = daysBetweenDates(year1, month1, day1, year2, month2, day2)

    assert implementation_days == python_days, "The implementation failed"

    print(f"The number of days between both dates is {python_days} days")

    return ''

print(test_validity(1999,2,20, 2024,3,30))