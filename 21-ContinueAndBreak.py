# break condition will terminate the loop instaneously
# continue will break current iteration instantaneously and move to next iteration

for var in range(1,10):
    print(var)
    if var==3:
        break
    print('statement1')
    print('statement2')

print(f'the value of var after for loop termination is {var}')

for var in range(1,10):
    print(var)
    print('statement1')
    print('statement2')
    if var==3:
        continue
    print('statement3')
    print('statement4')
