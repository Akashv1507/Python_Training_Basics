import pandas as pd

#1. list of dictionary
#2. list of tuples
#3. from databases
#4. From excel or csv

listOfDict = [{"Name":'Akash', 'LastName': 'Verma', 'age':24 }, 
                {"Name":'Alisha', 'LastName': 'Verma', 'age':22 }, 
                {"Name":'Mayank', 'LastName': 'Verma', 'age':31 },
                {"Name":'Aman', 'LastName': 'Singh', 'age':29 }]

listOfTuples = [('Akash', 'Verma', 24), 
                ('Alisha', 'Verma', 22), 
                ('Mayank', 'Verma', 31),
                ('Aman', 'Singh', 29)]

# creating pandas dataframe from list of dictionary
nameDf = pd.DataFrame(listOfDict)

# creating pandas dataframe from list of Tuples
tupleNameDf = pd.DataFrame(listOfTuples, columns=['FirstName', 'LastName', 'Age'])

# creating pandas dataframe from excel/csv, relative path
# excelDf = pd.read_excel('dummyExcel.xlsx')

# using raw/absolute path
excelDf = pd.read_excel('D:/vs_code/python/Python_Training/Pandas/dummyExcel.xlsx')

#top 5 rows
print(excelDf.head(5))
# last 2 rows
print(excelDf.tail(2))