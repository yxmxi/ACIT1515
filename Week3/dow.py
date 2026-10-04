#Part 1:
month_codes = {
    1: 1, #January
    2: 4, #February
    3: 4, #March
    4: 0, #April
    5: 2, #May
    6: 5, #June
    7: 0, #July
    8: 3, #August
    9: 6, #September
    10: 1, #October
    11: 4, #November
    12: 6 #December
}

weekdays = {
    0: "Saturday",
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday"
}


def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

def getDayOfWeek(day, month, year):
    last_two_digits = year % 100
    num_twelves = int(last_two_digits / 12)
    remainder = last_two_digits % 12
    num_fours = int(remainder / 4)

    offset_month = month_codes[month]

    century = int(year / 100)
    if century == 16:
        offset_month = offset_month + 6
    elif century  == 17:
        offset_month = offset_month + 4
    elif century == 18:
        offset_month = offset_month + 2
    elif century == 20:
        offset_month = offset_month + 6
    elif century == 21:
        offset_month = offset_month + 4
    

    total = num_twelves + remainder + num_fours + day + offset_month
    return weekdays[total % 7]


#Part 2:
days_in_month = {
    1: 31, #January
    2: 28, #February
    3: 31, #March
    4: 30, #April
    5: 31, #May
    6: 30, #June
    7: 31, #July
    8: 31, #August
    9: 30, #September
    10: 31, #October
    11: 30, #November
    12: 31 #December
}
def makeCalendar():
    year = 2026
    for month in range(1, 13):
        total_days = days_in_month[month]
        if month == 2 and isLeapYear(year):
            total_days + 1
        
        for day in range(1, total_days + 1):
            weekday = getDayOfWeek(day, month, year)
            print(f"{month}-{day}-{year} is a {weekday}")

