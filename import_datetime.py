import datetime

a=datetime.date.today()
print(a)
print("day",a.day)
print("year",a.year)
print("month",a.month)
#days are count from 0(monday) to 6(sunday)
print("day of the week",a.weekday())
#days are count from 1(monday) to 7(sunday)
print("day of the week",a.isoweekday())
print()

b=datetime.date(2020,12,20)
print(b)
print()

bday=datetime.date(1989,6,2)
last_bday=datetime.date(2022,6,2)
still_bday=bday-a
days_of_bday=last_bday-a
print(still_bday)
print(still_bday.days)
print(int(still_bday.days/365)*-1,"years and",(days_of_bday.days*-1),"days")
print()

now=datetime.datetime.now()
print(now)
print()

#personalized date
#%y=22 %Y=2022
current_date=datetime.datetime.strftime(now, '%d-%m-%Y  %H:%M:%S')
print(current_date)
print()

#%b=Jun %B=June
current_date2=datetime.datetime.strftime(now, '%B-%A-%d-%Y  %H:%M:%S')
print(current_date2)
print()

date_text='Jun-29-2022 07:18:55'
current_date3=datetime.datetime.strptime(date_text, '%b-%d-%Y  %H:%M:%S')
print(current_date3)
print()

old_date=datetime.datetime(2021,12,31)
difference=now-old_date
print(difference.days)
print(difference.total_seconds())
print()

day=datetime.datetime.strftime(now, '%d')
day=int(datetime.datetime.strftime(now, '%d'))
print(day)
print()

hour=datetime.datetime.strftime(now, '%H:%M:%S')
print(hour)
print()

delta_day=datetime.timedelta(days=5)
star_date=datetime.date.today()
print(star_date)
future_date= star_date+delta_day
print(future_date)

#fecha formato iso
datedate=datetime.datetime.now().isoformat()
print(datedate)

