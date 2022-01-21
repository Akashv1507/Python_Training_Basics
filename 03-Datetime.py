import datetime as dt

newFormatTime= "18-01-2022 20/43/00"
currTimestampNew = dt.datetime.strptime(newFormatTime, "%d-%m-%Y %H/%M/%S")

# timeedelta add/subtract from timestamp
nextDay = newFormatTime + dt.timedelta(days=1, minutes=30, seconds=40)

print(newFormatTime.date())
print(newFormatTime.time())
print(newFormatTime.day)
print(newFormatTime.month)

# print current time
print(dt.datetime.now())



