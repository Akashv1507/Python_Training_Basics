

emptyList = []
listWith1Ele = [1]
listWithMultipleEle = [1, 'Akash', 24, 'M']
# list of list or nested list or multidimensionList
list2d = [[1, 'Akash', 24, 'M'],
          [2, 'Alisha', 22, 'F'], 
          [3, 'Mayank', 31, 'M'] ]

# finding list length
print(len(emptyList), len(listWith1Ele), len(listWithMultipleEle), len(list2d))

# indexing in list(to access any element in list)
print(listWithMultipleEle[3], listWithMultipleEle[1][3], list2d[1][1], list2d[1][1][-1] )

# variuos methods applied on list
#1. to append element in list

emptyList.append('akash')
emptyList.append(2)
emptyList.append(False)

# 2. insert Element at any index
emptyList.insert(2, 'insertedEle' )

# 3. Addition of multiple elements to the List at the end (using Extend Method)
emptyList.extend([8, 'Geeks', 'Always'])
# print(emptyList)

# 4. pop(retrieve) element from list, pop will return retrived element, no argument given will pop last element
poppedEle = emptyList.pop()
print(poppedEle)

# 5. remove will remove element of argument, no returning and argument is must
emptyList.remove(2)

# --------------slicing list/string-----------------------
# start index will be included, and last/end index will not be included
print(emptyList[:3])
print(emptyList[1:3])
print(emptyList[2:])
print(emptyList[:])

# slicing in string
print(emptyList)
print(emptyList[0][:-1])
print(emptyList[1][-8:-2])

#list.sort(reverse=True|False, key=myFunc)
unsortedList = [5,3,10,11,2354,11,234]
# sortedList = unsortedList.sort() # this will not return new sorted list, change will take inplace

sortedNewListReturned = sorted(unsortedList)# this will return new branded sorted list, no inplace operation

