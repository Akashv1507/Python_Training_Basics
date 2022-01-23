
numbList = [1,0,2,0,24,65,0,0]
number = int(input ("Please enter number whose table you want to print : "))
countZero = 0
sum = 0

# loop variable
ind = 0
 
# print sum of elements in list
while(ind<len(numbList)):           #len(numbList)=8
    sum = sum + numbList[ind]
    ind = ind+1

# at this point variable ind hold value 8 , hence reinitialization
ind =0 
# count number of zeros
while(ind<len(numbList)):
    if numbList[ind] == 0:
        countZero= countZero + 1
    ind = ind+1


print(f'No of time 0 in list is {countZero}')
print(f'sum of  list is {sum}')

# print table of number given by users

loopVar = 1

# print table of number given by user
while(loopVar<=10):
    print(loopVar*number)
    loopVar = loopVar+1





