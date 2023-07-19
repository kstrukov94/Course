from datetime import datetime as dt

now = dt.now()
print(now)
print(now.day, now.month, now.year, now.hour)
print(now.utcnow())

sa_date = dt(2016, 7, 29, )
print(sa_date)