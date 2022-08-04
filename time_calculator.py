def add_time(start, duration, day=None):  
    new_star,new_duration,meridiem=[],[],[]
    star_meridiem=start.split()

    for period in star_meridiem:
        if period=="PM" or period=="AM": meridiem.append(period)

    for numbers in start:
        if numbers==" " or numbers=="P" or numbers=="M" or numbers=="A": continue
        if numbers==":": numbers=" "
        new_star.append(numbers)

    start="".join(new_star)
    start_times=start.split()
    start_hours,start_minutes=start_times[0],start_times[-1]

    for numbers in duration:
        if numbers==":": numbers=" "
        new_duration.append(numbers)

    duration="".join(new_duration)
    duration_times=duration.split()
    duration_hours,duration_minutes=duration_times[0],duration_times[-1]

    #----------------operations-----------------
    hours=(int(duration_hours)+int(start_hours))
    minutes=int(duration_minutes)+int(start_minutes)
    duration_hours_total=(int(duration_hours)+int(duration_minutes)/60)
    start_hours_total=(int(start_hours)+int(start_minutes)/60)
    total=duration_hours_total+start_hours_total
    residuo=(((total/24)-(total//24))*24)
    
    #------------some important parameters-----------
    hours2,minutes2,days,am_or_pm,format_12,format_24=0,0,0,[],12,24
    if minutes>=60: 
        hours+=1
        minutes2=(60-minutes)*-1   

    hours=hours%format_12
    hours2=(hours/format_24-hours//format_24)*format_24
    hours2=round(hours2)
    if hours2==0 or hours==0:
        hours=12
        hours2=12    

    first_time=str(hours if int(hours)<25 else hours2)
    second_time=str(f'{minutes:02}' if int(minutes)<60 else f'{minutes2:02}')
    
    # ----------------handling AM or PM-----------------
    if int(duration_hours_total)<=12:
        if total >= 12 and meridiem[-1]=="PM": am_or_pm=" AM"
        elif total >= 12 and meridiem[-1]=="AM": am_or_pm=" PM"
        elif total < 13: am_or_pm=f' {meridiem[-1]}'

    if int(duration_hours_total)>12 and int(duration_hours_total)<=24:
        if total >= 24 and meridiem[-1]=="PM": am_or_pm=" AM"
        elif total >= 24 and meridiem[-1]=="AM": am_or_pm=" PM"
        elif total < 24: am_or_pm=f' {meridiem[-1]}'

    if int(duration_hours_total)>=24:
        if residuo<=12 and meridiem[-1]=="PM": am_or_pm=" PM"
        if residuo>12 and residuo<=24 and meridiem[-1]=="PM": am_or_pm=" AM"
        if residuo<=12 and meridiem[-1]=="AM": am_or_pm=" AM"
        if residuo>12 and residuo<=24 and meridiem[-1]=="AM": am_or_pm=" PM"

    #---------------handling days-------------
    days=round(total/24)
    day_of_week={'Monday':1,'tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'saturDay':6,'Sunday':7}
    if day==None: day=""
    elif days<1: day=f', {day}'
    elif days>=1:
        number_day_of_week=(day_of_week[day])
        counter=0
        for i in range(number_day_of_week,(days+number_day_of_week+1)):
            i=i%7
            if i==0: i=7
        day=f', {(dict((v,k) for k,v in day_of_week.items()).get(i))}'

    #----------------days message-----------------   
    if (days>=0 and days<1): days=""
    elif days==1 and meridiem[-1]=="PM": days=" (next day)"
    elif (days==1 and meridiem[-1]=="AM") and duration_hours_total>=24: days=" (next day)"
    elif days==1 and meridiem[-1]=="AM": days=""
    elif days>=2: days=(f' ({days} days later)')
    days_mesage=str(days)

    #---------------final output-------------
    final_time=[first_time,":",second_time,am_or_pm,day,days_mesage]
    new_time="".join(map(str,final_time))
    return new_time

#print(add_time("3:00 PM", "3:10"))
#print(add_time("11:30 AM", "2:32", "Monday"))
#print(add_time("11:43 AM", "00:20"))
#print(add_time("10:10 PM", "3:30"), "Sunday")
#print(add_time("11:43 PM", "24:20", "tuesday"))
#print(add_time("6:30 PM", "205:12", "Monday"))
#print(add_time("6:30 PM", "25:12"), "Friday")
print(add_time("5:01 AM", "0:00"))
#"5:42 PM, Monday"
#print(add_time("2:59 AM", "24:00", "saturDay"))