# .Define the function which returns the counts of saturdays part of a year 
# (year is an input [Ex: 2022])
import datetime

def count_saturdays(year):
    saturdays = 0
    # Loop over all the days in the year
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                # Create a datetime object for the current day
                date = datetime.date(year, month, day)
                # Check if the current day is a Saturday
                if date.weekday() == 5:
                    saturdays += 1
            except ValueError:
                # If the day is out of range for the current month, ignore it
                pass
    return saturdays
print(count_saturdays(int(input("enter any year: "))))

import calendar

def count_saturdays(year):
    count=0
    for month in range(1,13):
        days=calendar.monthrange(year,month)[1]
        # print(days)
        for day in range(1,days+1):
            weekday=calendar.weekday(year,month,day)
            if weekday==5:
                count+=1
    return count

print(count_saturdays(int(input("enter any year: "))))