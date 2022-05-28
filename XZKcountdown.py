import datetime,time,os

today = datetime.date.today()
print(today)
xzk = datetime.date(2022,6,25)
print(xzk)
delta = xzk - today
print(delta)
os.system("pause")