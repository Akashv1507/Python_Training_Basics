
from pickle import TRUE

# loop variable initialization
loopVar = 1

# loop termination condition
while loopVar<=10:
    print('inside of loop body')
    print(f'value of loopVar is {loopVar}')
    print('loop body executed for currrent iteration')
    print('------------------------------------')
    #loop variable modification(commpulsory step)
    loopVar = loopVar *3

print("normal loop execution")

# infinite loop, becuase loop termination condition is always true
# while True:
#     print("infinite loop")

# loop body wont execute , becuase loop termination condition is always true
while False:
    print("infinite loop")

