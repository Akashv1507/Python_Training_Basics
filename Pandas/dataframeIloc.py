import pandas as pd 

# filtering in dataframe
excelDf = pd.read_excel('D:/vs_code/python/Python_Training/Pandas/dummyExcel.xlsx')
excelDf.set_index('Date', inplace=True)

# filteredExcelDf = excelDf[excelDf['Available_capacity']>10]

iLocExcelDf = excelDf.iloc[0:15,0:2]
iLocExcelDf = excelDf.iloc[0:15]
iLocExcelDf = excelDf.iloc[[0,3,7], [0,4]]
iLocExcelDf = excelDf.iloc[[0,3,7], ]
print(iLocExcelDf)

