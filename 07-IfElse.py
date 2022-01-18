
'''if operator/expression that retruns boolean:
        code1
    elif operator/expression that retruns boolean:
        code 2
    elif....

    else:
        code 3
'''
# code 1
marks = 30

if marks>=33:
    print("student is passed")
else:
    print("student is failed")
    print('other logic')
    print(1+2-5*4)
print("normal code execute/ end of python file")

# code 2, using user input and nested if else print largest no and smallest no
numb1= 20
numb2 = 30 
numb3 = 40

if numb1>numb2:
    if numb1>numb3:
        print(f'number {numb1} is greatest') # template literals
    else:
        print(f'number {numb3} is greatest')
else:
    if numb2>numb3:
        print(f'number {numb2} is greatest')
    else:
        print(f'number {numb3} is greatest')


name = "akdnasfjsdfjdsjfdas 9+9"
print(name)
name = f"akdnasfjsdfjdsjfdas {9+9}"
print(name)

