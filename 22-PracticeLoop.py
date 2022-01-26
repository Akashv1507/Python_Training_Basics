#Q1 reverse a string, akash->hsaka
#Q2 reverse each element of a list, ['akash', 'alisha', 'mayank']


name= 'akash,verma,24 akash'
nameList = ['akash', 'alisha', 'mayank']

# use of split method, by default split on space chanracter, always retrun a list
# returnList =name.split(',')
# print(returnList)
# use of join method, to join all element of a list into a single string based on join character
# retrunString = "@".join(returnList)
# print(retrunString)

# Q1 method 1
# revName = name[::-1]
# print(revName)

# q1 method 2
# revStr = ""
# for i in range(len(name)-1, -1, -1):
#     revStr+= name[i]
# print(revStr)

# q2 method1
# revListNames= []
# for name in nameList:
#     revStr = ""
#     for i in range(len(name)-1, -1, -1):
#         revStr+= name[i]
#     revListNames.append(revStr)
# print(revListNames)

#list comprehension
# numList = [1,2,3,4,5]       #->[1,4,9,16,25]
# squaredNumList= []
# for num in numList:
#     # squaredNumList.append(num*num)
#     squaredNumList.append(num**2)
# print(squaredNumList)

# numList = [1,2,3,4,5]
# squaredNumList = [num*num for num in numList]
# print(squaredNumList)

# reversing list of string using list comprehension
# revNameList = [name[::-1] for name in nameList]
# print(revNameList)

    

    

