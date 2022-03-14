from matplotlib.style import available
import pandas as pd


excelDf = pd.read_excel('D:/vs_code/python/Python_Training/Pandas/dummyExcel.xlsx')

#getting all columns and index
allCols = excelDf.columns
allIndex = excelDf.index

# print(allCols.tolist())
# print(allIndex)

#getting single columns
# print(excelDf['Fee_type'])
#getting single value
# print(excelDf['Available_capacity'][4])

storageList=[]

for ind in excelDf.index:
    storageList.append(excelDf['Available_capacity'][ind])

print(excelDf['Available_capacity'].max())

excelDf['sumCol'] = excelDf['Available_capacity_dose1'] + excelDf['Available_capacity_dose2']

# savinf dataframe to excel
excelDf.to_excel("modified.xlsx")
print(excelDf)
