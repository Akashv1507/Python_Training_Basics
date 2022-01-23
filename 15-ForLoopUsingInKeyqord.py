# in keyword needed iterable, List, tuples, string, 
# range(0,8)-> [0,1,2,3,4,5,6,7]

numbList = [1,0,2,0,24,65,0,0]
countZero = 0
sum = 0

# syntax of for loop using in
for loopVar in [1,2,3]:
    print(loopVar)
    print("-----------------------")
# iterating on tuples
for loopVar in (1,2,3):
    print(loopVar)
    print("-----------------------")
# iterating in string
for loopVar in 'akash':
    print(loopVar)
    print("-----------------------")

# count zero using loop
for loopVar in numbList:
    if loopVar == 0:
        countZero = countZero+1

# sum of all element in list  
for loopVar in numbList:
    sum = sum + loopVar

print(f'No of time 0 in list is {countZero}')
print(f'sum of  list is {sum}')


