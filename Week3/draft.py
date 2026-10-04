def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

#def getDayOfWeek(day, month, year):
# while True: 
#     year = int(input("Enter year: "))
#     if isLeapYear(year):
#         print(f"{year} is a larp year.")
#     else:
#         print(f"{year} is not a leap year.")
    