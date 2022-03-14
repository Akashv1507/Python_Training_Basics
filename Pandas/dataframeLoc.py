import pandas as pd

excelDf = pd.read_excel('D:/vs_code/python/Python_Training/Pandas/dummyExcel.xlsx')
excelDf.set_index('Date', inplace=True)

# loc works on index value, it completly depends on index value
iLocExcelDf = excelDf.loc['2022-03-01': '2022-03-05', 'District_name': 'Min_Age_Limit']
print(excelDf)
print(iLocExcelDf)

