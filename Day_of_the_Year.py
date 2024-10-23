date = "1900-05-02"



def foo(date : str) -> int:
    DaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year, month, day = date.split("-")

    if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
        DaysInMonth[1] = 29


    TotalDays = 0
    for i in range(int(month)-1):
        TotalDays += DaysInMonth[i]
    
    TotalDays += int(day)



    return TotalDays


print(foo(date))