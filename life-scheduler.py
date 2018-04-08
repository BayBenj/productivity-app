#
from datetime import timedelta
import datetime
import time

def weekday_(i):
    if i == 0:
        return "Sunday"
    elif i == 1:
        return "Monday"
    elif i == 2:
        return "Tuesday"
    elif i == 3:
        return "Wednesday"
    elif i == 4:
        return "Thursday"
    elif i == 5:
        return "Friday"
    elif i == 6:
        return "Saturday"

def month_(i):
    if i == 0:
        return "January"
    elif i == 1:
        return "February"
    elif i == 2:
        return "March"
    elif i == 3:
        return "April"
    elif i == 4:
        return "May"
    elif i == 5:
        return "June"
    elif i == 6:
        return "July"
    elif i == 7:
        return "August"
    elif i == 8:
        return "September"
    elif i == 9:
        return "October"
    elif i == 10:
        return "November"
    elif i == 11:
        return "December"

def getTextFromNowTo(end):
    now = datetime.datetime.now()#.timestamp()
    getTextForPeriod(now, end)

def getTextForPeriod(start, end):
    sundays = 1
    prev_month = 0
    while start < end:
        start = start + timedelta(days=1)
        year = start.year
        month = start.month
        if prev_month != month:
            sundays = 1
        weekday = start.weekday()
        day = start.day

        if weekday == 0:
            print("\n\n\n\n" + str(month_(month)) + " week " + str(sundays))
            print(str(year))
            print("This Week\n\n")
            sundays += 1
        print(str(weekday_(weekday)) + " " + str(day) + "\n\n")
        if weekday == 6:
            print("End of week\n\n")
            print("Week notes\n\n")
        if prev_month != month:
            sundays = 1

        new_week = False
        prev_year = year
        prev_month = month
        prev_day = day

# end_date = datetime.datetime.strptime('31.05.2018 09:38:42,76', '%d.%m.%Y %H:%M:%S,%f').timestamp()
end_date = datetime.datetime.strptime("2018-05-31", "%Y-%m-%d")
getTextFromNowTo(end_date)
