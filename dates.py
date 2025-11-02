import datetime
#retrieves the current date and time using datetime.now() method 
x = datetime.datetime.now()
print(x) 
#the above contains 2024-04-08 23:01:15.608734 
#from above we can get year,month,day,week,hour,minute,second,microseconds
print("Year:", x.year)
print("Month:", x.month)
print("Day:", x.day)
print("Hour:", x.hour)
print("Minute:", x.minute)
print("Second:", x.second)
print("Microsecond:", x.microsecond)
#(0 for Monday, 1 for Tuesday, ..., 6 for Sunday).
print("Weekday:", x.weekday())
print(x.strftime("%A"))     #it prints weekday 
#The strftime() Method
#The datetime object has a method for formatting date objects into readable strings.
print(x.strftime("%p"))   #AM/PM

#Creating Date Objects
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)            #2020-05-17 00:00:00











""" 
from datetime import date,time,datetime
dt1=date.today()
print("today date: ",dt1)
t1=datetime.now()
print("now date and time: ",t1)
bd=date(2003,8,15)                 #(year,month,date)
bt=time(12,45,45)                  #(hour,minutes,sec)
print(bd) 
print(bt)       
gap=(dt1-bd).days
print("age in days: ",gap)
#for user input date
dateinput=input("enter date: ")     # enter data wrt format specifiers of below line
bd1=datetime.strptime(dateinput,"%d %m %Y ")
print(bd1)
gap=(dt1-bd1.date()).days
print("gap of days: ",gap)
 """



# from datetime import date,time,datetime
# dt=date(2023,12,15)
# a=dt.strftime("%d/%m/%Y")
# print(a)



""" 
import datetime
t=datetime.time(2,30,45,500) #hr,min,sec,microsec
print(t)
print("time is: ",t.hour,"hours",t.minute,"minutes",t.second,"seconds",t.microsecond,"microseconds")
d=datetime.date(2018,5,15) #year, month,day
print(d)
d1=d.year
d2=d.month
d3=d.day
print("the day month year is:",d3,d2,d1)

dt=datetime.datetime.now()                          #here datetime module has datetime object and it has now function 
print("now date and time is: ",dt)                                           #give current date and time
year=dt.strftime("%Y")                              # %y(to get year last two digit as 23),%B for monthname,%m(month as number),
print("current year: ",year)

nowd=datetime.date.today()
print("today date is",nowd)  #give today date

 """


 











""" 
#it always prints  year-month-date hour:min:sec

import datetime 
from datetime import date,time,datetime    #---->these are objects
print(date.today())                 #print date
print(datetime.now())               #print date and time 
print(date(2003,8,15))              #(year,month,date)
print(time(14,45,45))               #(hour,minutes,sec)
print(datetime(2016,10,28,15,30))   #both date and time
print(datetime.strptime("10/12/2003","%m/%d/%Y"))   #it prints wrt format specifiers

dateinput=input("enter date: ")  # enter data wrt format specifiers of below line
bd=datetime.strptime(dateinput,"%d/%m/%Y")
print(bd)

 """


 






 
""" #timedelta gives span of time 
from datetime import datetime, timedelta,date
w=timedelta(weeks=3)                        #give as days
print(w)
t=timedelta(weeks=5,days=3,hours=2,minutes=30)
print(t)
tm=timedelta(hours=2,minutes=30)
print(tm)
pd=date.today()-timedelta(weeks=4)
print(pd)
tf=datetime.now()-timedelta(hours=4,days=5)
print(tf)
 """




#to find span between two dates
""" 
pre=datetime(2023,8,12)
tod=datetime.now()
print("difference is: ",tod-pre) 
#to find span only days
d=(datetime.now()-pre).days
print("days: ",d)
#d=(datetime.now()-pre)
#print("just days: ",d.days,"seconds: ",d.seconds )
 """




 
#attributes that retruns part of date and time 
"""
dat=datetime(2003,8,17,00,36,35)
print("year is: ",dat.year)  #similarly-->dat.month,dat.day,dat.hour,dat.minute,dat.second,dat.microsecond
td=datetime.today()
print("last year is: ",td.year-1)
if td.year>dat.year:
    print("it is past")
if td>dat :
    print("the gap is: ",td-dat)

st=datetime.now()
end=st+timedelta(hours=2)
print("meeting time : ",end-st)
 """






#find the gap  of days between next birthday and today........>
""" 
from datetime import date
# Your birthdate (replace with your actual birthdate)
birth_date = date(2003, 8, 15)
# Get today's date
current_date = date.today()
# Calculate the next birthday
next_birthday = date(current_date.year, birth_date.month, birth_date.day)
# Check if the next birthday has already occurred this year
if next_birthday < current_date:
    next_birthday = date(current_date.year + 1, birth_date.month, birth_date.day)
# Calculate the difference in days
gap_in_days = (next_birthday - current_date).days
print("Gap in days until the next birthday:", gap_in_days)

 """
















""" 
from datetime import datetime,timedelta
def inputdate():
    dt=input("enter meeting date: ")
    dat=datetime.strptime(dt,"%d/%m/%Y")
    td=datetime.today()
    return dat

def main():
    print("the days of meeting time: ")
    while(1):
        dt=inputdate()
        td=datetime.today()
        try:
            gap=(dt-td).days
            print("the meeting in: ",gap," days")
        except Exception:
            print("the day is already paassed")
        opt=input("you want to change time(y/n): ")
        if(opt!='y'):
            break

if __name__=='__main__':
    main() """





""" 
from datetime import datetime, time
print("the timer program")
input("press enter to start")
st=datetime.now()
print("starttime is: ",st)
input("press enter to stop")
ed=datetime.now()
span=(ed-st).seconds
print("gap time in seconds: ",span)
 """






""" 
from datetime import datetime,timedelta
def arrival_date():
    dt=input("enter arrival date: ")
    date1=datetime.strptime(dt,"%d/%m/%Y")
    return date1
def leaving_date():
    dt=input("enter leaving date: ")
    date2=datetime.strptime(dt,"%d/%m/%Y")
    return date2          #return should be writtern

def main():
    print("the days of meeting time: ")
    while(1):
        dt1=arrival_date()
        dt2=leaving_date()
        try:
            gap=(dt2-dt1).days
            print("no of days staying: ",gap," days")
            print("per day cost is 10$")
            cost=10*int(gap)
            print("total cost while staying",cost)
        except Exception:
            print("arrival should should be lesser than leaving date")
        opt=input("you want to change time(y/n): ")
        if(opt!='y'):
            break

if __name__=='__main__':
    main()
 """


















""" 
from datetime import datetime
# Your birthdate (replace with your actual birthdate)
birth_date = datetime(1990, 5, 15)
# Get the current date and time
current_date = datetime.now()
# Calculate the difference between current date and birthdate
difference = current_date - birth_date
# Extract the number of days from the difference
days_difference = difference.days
print(f"Method 1: You are {days_difference} days old.")







from datetime import date
# Your birthdate (replace with your actual birthdate)
birth_date = date(1990, 5, 15)
# Get the current date
current_date = date.today()
# Calculate the difference between current date and birthdate
difference = current_date - birth_date
# Extract the number of days from the difference
days_difference = difference.days
print(f"Method 2: You are {days_difference} days old.")
 """




# #changing year from 2 digit to 4 digit
# from datetime import datetime,date
# bd=input("enter date: ")
# bdt=datetime.strptime(bd,"%d/%m/%y")
# a=bdt.strftime("%d/%m/%Y")
# print(a)












