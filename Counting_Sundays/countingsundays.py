startYear = 1901
startMonth = 1
startDay = 1
endYear = 2000
endMonth = 12
endDay = 31
daycount = 0

monthLenArr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def checkLeap(year):
    if (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        return True
    elif (year % 100 == 0) and (year % 400 == 0):
        return False
    elif (year % 4 == 0):
        return True

#    if (year % 100 != 0) and (year % 4 == 0):
#        return True
#    elif (year % 100 == 0) and (year % 400 == 0):
#        return True
#    return False


for currentYear in range(startYear, endYear+1):
    print(currentYear)
    if currentYear == endYear:
        month = endMonth
    else:
        month = 12
    for currentMonth in range(startMonth, month+1):
        if currentMonth + 1 == 2 and checkLeap(currentYear):
            print("leap")
            day = 29
        else:
            day = monthLenArr[currentMonth-1]
        for currentDay in range(1, day+1):
            daycount += 1
            if (currentYear == endYear) and (currentMonth == endMonth) and (currentDay == endDay):
                break

print(currentMonth)
print(currentDay)

print(daycount)
print(daycount//7)
print(daycount % 7)
