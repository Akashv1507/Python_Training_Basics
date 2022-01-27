# empty dictionary
emptyDict = {}
emptyDict = dict()

# creating dictionary using dict keyword
numdict = dict(I='one', II='two', III='three')
# print(numdict)

# modifying and adding dictionary key val pair, if no key present -> it will add new key
# numdict['I']= 'new one'
# numdict['IV'] = 'fourth added'
# print(numdict)

#update
# x = {'one': 0, 'two': 2}
# y = {'one': 1, 'three': 3}
# x.update(y)
# print(x)
# return no. of key value pair
# print(len(x))

#find all keys, find all values, get items in tuple/list->[('I', 'one'),('II', 'two'),('III', 'three')]
# print(list(numdict.keys()))
# print(numdict.values())
# print(numdict.items())

# numdict.values() is not of type list
# print(type(numdict.values()))
# print(type([1,2,3]))
for ele in numdict.values():
    print(f'ele value is {ele}')

    # used in python 3.7 and above
    # print('ele value is {} and once again element{}'.format(ele, ele))


# check any keys present in dictionary
# if 'III' in numdict.keys():
#     print(f"key exist")

# print all key and corresponding values
for ele in numdict.items():
    print('the key is {} and its value is {}'.format(ele[0], ele[1]))
