import datetime as dt
import pandas as pd

name = "mayank" # string(str)
age= 31         # integer(int)
isMale= True    # boolean(bool)
currTime= "2022-01-18 20:43:00"
currTimestamp = dt.datetime.strptime(currTime, "%Y-%m-%d %H:%M:%S")

print(type(name))
print(type(age))
print(type(isMale))
print(type(currTime))
print(currTimestamp)
print(type(currTimestamp))

newFormatTime= "2022/01/18 20/43/00"
currTimestampNew = dt.datetime.strptime(newFormatTime, "%Y/%m/%d %H/%M/%S")
print(currTimestampNew)

newFormatTime2= "18-01-2022 20/43/00"
currTimestampNew2 = dt.datetime.strptime(newFormatTime2, "%d-%m-%Y %H/%M/%S")
print(currTimestampNew2)


print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[-1])
print(len(name))





