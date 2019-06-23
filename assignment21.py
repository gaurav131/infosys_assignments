def generate_next_date(day,month,year):
    months = [1,3,5,7,8,10,12]
    next_month = month
    next_year = year
    if month in months:
        if month == 12 and day == 31:
            next_day = 1
            next_month = 1
            next_year = year+1
        elif day == 31:
            next_day = 1
            next_month = month + 1
        else:
            next_day = day+1
    elif month==2 and day >= 28:
        leap_year = True if (year%400==0 or year%100!=0) and year%4==0 else False
        if leap_year and day == 28:
            next_day = 29
            next_month = 2
        else:
            next_day = 1
            next_month = 3
    else:
        if day == 30:
            next_day = 1
            next_month = month+1
        else:
            next_day = day+1

    print(next_day,"-",next_month,"-",next_year)


generate_next_date(30,6,2015)