from datetime import datetime , date

now = datetime.now()
day=now.day
month=now.month
year=now.year
hour=now.hour
minute=now.minute
timestamp=datetime.timestamp(now)
print(timestamp,day,month,year,hour,minute)
now=now.strftime("%m %d %Y ,%H,%M,%S")
print(now)
str1="5 December ,2019"
t0=datetime.strptime(str1,"%d %B ,%Y")
newyear=datetime(2027,1,1)
diff=newyear-datetime.now()
print(t0)
print(diff)
str2="1 January ,1970"
t1=datetime.strptime(str2,"%d %B ,%Y")
t2=datetime.now()-t1
print(t2)
#we can use this module to calculate age display dynamicaly current time make calculation for some coolmath tricks
