def day_in_month(month,year):
    month = month%12
    day = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (year%4==0 and year%400==0 and month==2) or (year%4==0 and year%100!=0 and month==2):
        return 29
    else:
        return day[month-1]

print(f"The year and month you have entered has {day_in_month(year=int(input("Enter year: ")),month=int(input("Enter months: ")))} ")