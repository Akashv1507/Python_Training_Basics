# # q1 , fucntion(list)->max min avg

# def getMaxMinAvg(numbList):
#     maxEle = numbList[0]
#     minEle = numbList[0]
#     sum = 0
#     for ele in numbList:
#         if ele>maxEle:
#             maxEle=ele
#         elif ele<minEle:
#             minEle=ele
#         sum = sum +ele
    
#     return {'maxEle': maxEle, 'minEle': minEle, 'avg': sum/len(numbList)}
#     # return maxEle, minEle, sum/len(numbList)
#     # return [maxEle, minEle, sum/len(numbList)]

# noList = [10,24,231,5436,11,3,78234,11112321]

# # noList= [] # exception/error handling-> will learn when connecting to database.

# respObj = getMaxMinAvg(noList)
# # accessing dictionary
# # print(respObj['maxEle'])

# print(respObj)


#  q2 , fucntion(list)->lis of factorials
def getFact(numb):
    fact = numb
    for i in range(1,fact):
        fact *= i
    return fact

def getListFactorials(numbList):
    
    factorialList = []
    # for ele in numbList:
    #     fact =ele
    #     for i in range(1,ele):
    #         fact = fact*i
    #     factorialList.append(fact)

    # using factorial function
    for ele in numbList:
        fact =getFact(ele)
        factorialList.append(fact)  
    return factorialList

noList = [1,2,3,4,5]
respList = getListFactorials(noList)
print(respList)
