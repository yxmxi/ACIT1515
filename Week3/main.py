import dow

dow.makeCalendar()

print("\n")

def getDayOfTheWeekForUserDate():
    print(" ~~~~ Day of the Week ~~~~")
    print("please only use numbers ／༼ ༏༏ີཻ༾ﾍ ༏༏ີཻ༾༾༽༽ program won't like it (e.g. 1-2-3456)")
    input_month = int(input("Enter a month: "))
    input_day = int(input("Enter a day: "))
    input_year = int(input("Enter a year: "))
    
    user_input_date = dow.getDayOfWeek(input_month, input_day, input_year)
    print(f"{input_month}-{input_day}-{input_year} is a {user_input_date}")


getDayOfTheWeekForUserDate()
