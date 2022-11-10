# Event Remindar to convert from lunar dates to solar dates:
# Copyright (C) 2022 Eunice Lee <euncholee@gmail.com>

import datetime
from lunardate import LunarDate


def create_event():
    name = input("------- Name : ")
    yy = input("------- Year of Birth : ")
    mm = input("------- Month of Birth : ")
    dd = input("------- Day of Birth : ")

    print_event(name, yy, mm, dd)


def print_event(name, yy, mm, dd):
    print ('Lunar birthday of ' + name + ' : ' + yy + '/' + mm  + '/' + dd)
    print_birthday_inSolarCalendar(name, yy, mm, dd)

def print_birthday_inSolarCalendar(name, yy, mm, dd):
    today = datetime.date.today() 
    currentYear = today.year
    solarDate = LunarDate(currentYear, int(mm) , int(dd), 0).toSolarDate()

    if today >= solarDate:
        currentYear = currentYear + 1   

    for num in range(5):
        solarDate = LunarDate(currentYear + num, int(mm) , int(dd), 0).toSolarDate()
        print ('Birthday of ' + name + ' in ' + str(solarDate.year) + ' : ' + str(solarDate.month) + '/' + str(solarDate.day))

def main():
    create_event()
    
if __name__=='__main__':
    main()
