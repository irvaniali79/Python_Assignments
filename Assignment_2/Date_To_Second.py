import datetime
import time

time1=input("enter date in H:M:S format: 1")
x = time.strptime(time1,'%H:%M:%S')
total_seconds=datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
print("total_seconds: ",total_seconds)