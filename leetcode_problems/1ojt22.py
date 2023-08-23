import calendar

# def satCounter(year ,month):
    
#     days=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     sat=[]
#     d=days[month]
#     if month==2 and calendar.isleap(year):
#         d=29
#     for day in range(1,d+1):
#         sat.append(calendar.weekday(year,month,day))
#     print(sat)
#     return f"number of saturdays are {sat.count(6)}"

# year=int(input("Enter the year"))
# month=int(input("Enter month 'in numbers':"))
# print(satCounter(year,month))

def list_of_saturday(month,year):
    num_days = calendar.monthrange(year, month)[1] #get weekday of first day of the month and 
                                    # number of days in month, for the specified year and month.
    print(num_days)
    saturday = []
    for day in range(1,num_days+1):
        weekday = calendar.weekday(year, month, day)
        # returns index of the day (0-monday, 1-tuesday......6-sunday)
        if weekday == 5:
            saturday.append(day)
    return saturday

list = list_of_saturday(1,2023)
# print(list)
