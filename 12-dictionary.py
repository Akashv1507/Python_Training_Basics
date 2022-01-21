from xml.dom.minidom import Element


emptyDict = {}

# key value pair {key1:val1, key2:val2.....}

dictWithOneKey = {'name': 'akash'}
dictWithMultKeys= {'name':'akash', 'age':24}
dictWithNumbKey = {1:'akash', 2: 24, 'ismale':True} # { 2: 24, 1:'akash',  'ismale':True}

# [1,2,3] != [2,1,3] for list

# accesing Element, indexing is not there
print(dictWithNumbKey[1])
print(dictWithNumbKey.get(1))
print(dictWithNumbKey['ismale'])
print(dictWithNumbKey.get('ismale'))

# adding element in dictionary
dictWithOneKey['age'] = 24
#modifying existing dictionary
dictWithNumbKey['ismale'] = False
print(dictWithOneKey)
print(dictWithNumbKey)

# deleting dictionary
del dictWithNumbKey
del dictWithMultKeys['age']

#nested dictionary
nestedDict = {'key1': 'val1',
 'key2':{'nestKey1':'nestVal1', 'nestKey2':['akash', 24]}
            }
print(nestedDict['key2']['nestKey1'])
print(nestedDict['key2']['nestKey2'][0][2])