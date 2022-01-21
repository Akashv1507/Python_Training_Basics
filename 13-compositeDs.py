#nested dictionary
nestedDict = {'key1': 'val1',
 'key2':{'nestKey1':'nestVal1', 'nestKey2':['akash', 24]}
            }
print(nestedDict['key2']['nestKey1'])
print(nestedDict['key2']['nestKey2'][0][2])

# normal use cases in database data fetching , suppose Employee(name, age, deptName)=>3 rows

generalInPython =[('akash', 24, 'cs'),
                ('mayank', 31, 'mech'),
                ('alisha', 23, 'arts')] # list of tuples/normal database return

listofList = [['akash', 24, 'cs'],
                ['mayank', 31, 'mech'],
                ['alisha', 23, 'arts']]

listOfDictionary = [{'name':'akash', 'age':24, 'deptName':'cs'}, 
                    {'name':'mayank', 'age':31, 'deptName':'mech'}, 
                    {'name':'alisha', 'age':22, 'deptName':'arts'}] # api call/frontend-backend data exchange

print(generalInPython[2][2])
print(listofList[1][2][1])
print(listOfDictionary[1]['deptName'][1])

