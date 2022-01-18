import datetime as dt

newFormatTime= "18-01-2022 20/43/00"
currTimestampNew = dt.datetime.strptime(newFormatTime, "%d-%m-%Y %H/%M/%S")

# timeedelta add/subtract from timestamp
nextDay = currTimestampNew + dt.timedelta(days=1, minutes=30, seconds=40)

print(currTimestampNew.date())
print(currTimestampNew.time())
print(currTimestampNew.day)
print(currTimestampNew.month)

# print current time
print(dt.datetime.now())


