# Project: Working with Dates

**NOTE:** The project functions can be executed in  [CodeSkulptor3/Working_with_ _Dates](https://py3.codeskulptor.org/#user307_WaUaYkowRR_10.py)

```{python}
"""
The goal is write three helper functions and one final funtion that takes three 
integers as input: the year, month, and day of a persons birthday. The function 
should return that person's age in days as of today. 
The function should return 0 if the input date is invalid, the function should 
also return 0 if the input date is in the future.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if (month + 1) > 12:
        my_days = datetime.date((year + 1), 1, 1) - datetime.date(year, month, 1)
    else:
        my_days = datetime.date(year, (month + 1), 1) - datetime.date(year, month, 1)
    
    return my_days.days

#print(days_in_month(12, 12))

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if not isinstance(year or month or day, int):
        print('at less one of the arguments is invalid')
        return False
    
    if not datetime.MINYEAR <= year <= datetime.MAXYEAR:
        print('year argument is invalid')
        return False
    
    if not 1 <= month <= 12:
        print('month argument is invalid')
        return False
    
    if not 1 <= day <= days_in_month(year, month):
        print('day argument is invalid')
        return False
    
    return True
     
#print(is_valid_date(9998, 12, 31))             

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    date_one = is_valid_date(year = year1, month = month1, day = day1)
    date_two = is_valid_date(year = year2, month = month2, day = day2)
    
    if date_one and date_two:
        if datetime.date(year2, month2, day2) < datetime.date(year1, month1, day1):
            return 0
        else:
            my_days = datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)
            return my_days.days
    return 0

#print(days_between(2000, 1, 1, 2000, 12, 31))

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    current_date = datetime.datetime.today()
    current_date = current_date.date()
    current_year = current_date.year
    current_month = current_date.month
    current_day = current_date.day
    
    
    if (not is_valid_date(year, month, day)) or (datetime.date(year, month, day) > current_date):
        return 0
    else:
        return days_between(year, month, day, current_year, current_month, current_day)

print(age_in_days(year = 2016, month = 12, day = 31))
```

    2061
