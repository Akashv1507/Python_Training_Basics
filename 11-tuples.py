

# tuples are immutable/not changeable 

tupleWith1Val= ('akash',)

multiValTuple = 'akash', 1, 'verma'
multiTuple = ('akash', 1, 'verma')

nestedTuple = ('akash', 24, ('verma', 23))
print(tupleWith1Val,multiValTuple, multiTuple)

print(multiTuple[0], nestedTuple[2][0][1])

print(nestedTuple[1:][1:][0][0][2])

# convert list to tuple
list1 = ['akash', 1, 'verma']
list1[1]= 'changedVal'
tupl1 = tuple(list1)

# tupl1[1] = 1 not possible to change tuple created
print(tupl1)

#converting tuple to list
listCon = list(tupl1)
print(listCon)

