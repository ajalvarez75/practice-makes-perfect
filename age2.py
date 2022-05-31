import datetime
currentDate = datetime.datetime.now()

deadline= input ('Please enter your date of birth (dd/mm/yyyy): ')
deadlineDate= datetime.datetime.strptime(deadline,'%d/%m/%Y')

daysLeft = deadlineDate - currentDate
print(daysLeft)

years = ((daysLeft.total_seconds())/(365.242243600))
years = abs(years)
yearsInt=int(years)

months=(years-yearsInt)*12
months = abs(months)
monthsInt=int(months)

days=(months-monthsInt)*(365.242/12)
days = abs(days)
daysInt=int(days)

print(daysInt)