# to prevent python code terminating abruptly/sudden, we use error or exception handling

numbList = [1,2,3]

# for numb in numbList:
#     print(numbList[numb-1])

print("before for loop")
try:
    for i in range(0, len(numbList)):
        print(f"{i} is {5*numbList[i]}")
    print('will this line of code execute?')
except Exception as err:
    print('-----------error-----------')
    print(f"the code terminated abruptly via error {err}")
finally:
    print('-----------finally block-----------')
    print("this code block executes everytime")


print('after for loop body')
print('python file execution terminates')
print('----------ENd of pytho file-------')

