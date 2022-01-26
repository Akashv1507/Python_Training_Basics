# function/method syntax
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# def functionName(paramter 1/arguement 1, parameter 2/arguement2,  parameter 3/arguement3........ ):
#     #python code
#     return something

# ------------------------------------------------------------
# defintion of function, here c is a optional
# def sum ( a, b, c=1):
#     print("akash")
#     sum = a+b
#     return sum
    
# function call
# sum1 = sum(2,3)
# sum2 = sum(1000,200000)
# sum3 = sum(2.5, 305)
# print(sum1, sum2, sum3)
# -----------------------------------------------------------------------

# def DerivedPrint(msg, end='\n'):
#     return 'hi there ' + msg

# msg1 = DerivedPrint('this is akash')
# msg2 = DerivedPrint('we are learning python')
# print(msg1, msg2)

# ---------------------------------------------------------------------------

# funtion that does not take any argument and does not return anything
# def doNothingOnlyPrint():
#     print("I am doing nothing, does not take any argument and does not return anything")
    
# x = doNothingOnlyPrint()
# print(x)

# ---------------------------------------------------------------------------
# funtion that take one argument and does not return anything
# def oneArgumentOnlyPrint(msg):
#     print("I am doing nothing, does not take any argument and does not return anything" + msg)
    
# x = oneArgumentOnlyPrint('I am The End')
# print(x)
# -----------------------------------------------------------------------------

# def sum ( num1, num2, num3=0):
#     print("akash")
#     div = num1/num2
#     return div
    
# function call
# print(sum(6,2))
# print(sum(num2=6, num1=2))

# -----------------------------------------------------------------------------

# print element of list using function
# def printListElement(eleList):
#     for ele in eleList:
#         print(ele)

# returnVal = printListElement('akash')
# print(returnVal)

# returnVal = printListElement(['akash', 'alisha', 'mayank'])
# print(returnVal)

# ------------------------------------------------------------------------------
# names= ["Emil", "Tobias", "Linus"]-> inside in python this is happening, dont know exact no. of arguments, positional arguements
# def my_function(*names):
#   print("The youngest child is " + names[4])

# my_function("Emil", "Tobias", "Linus", 'akash', 'alisha', 'mayank' )

#----------------------------------------------------------------------------------
nameList = ['akash', 'alisha', 'mayank']
reversedNameList = []

def reverseString(nameStr):
    return nameStr[::-1]

for name in nameList:
    revName = reverseString(name)
    reversedNameList.append(revName)
    # print(reversedNameList)
print(reversedNameList)

# of we dont use loop then we have to call function with each element of list
# revName = reverseString(nameList[0])
# reversedNameList.append(revName)

# revName = reverseString(nameList[1])
# reversedNameList.append(revName)

# revName = reverseString(nameList[2])
# reversedNameList.append(revName)

# print(reversedNameList)