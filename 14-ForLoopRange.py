# loop variable, loop variable initialization, loop body, loop terminate
# loopvar belogs to [0.......7]
'''
for loopvar in range(startind, endInd, stepSize)
    algo:
    loopvar = startInd -> initialization 
    if loopvar<endInd:
        then execute loopbod
    else:
        go out of loop'''

for loopVar in range(0, 3):
    print('inside of loop body')
    print(f'value of loopVar is {loopVar}')
    print('loop body executed for currrent iteration')
    print('------------------------------------')

for loopVar in range(0, 10, 3):
    print('inside of loop body')
    print(f'value of loopVar is {loopVar}')
    print('loop body executed for currrent iteration')
    print('------------------------------------')



print("out of the loop normal execution")
