'''
*
**
***
****
....
'''
numbOfLines = int(input("enter number of lines : ")) #5

for i in range(1, numbOfLines+1):
    print('*'*i, end='\n') # by defalut
    
print('-------------------------')
# for i in range(1, numbOfLines+1):
#     print('*'*i, end='@') 
    

# for i in range (numbOfLines): # 0,1,2,3
#     for j in range(0,i):
#         print(i+j, end='')
#     print('')

for outerLoopVar in range(0, numbOfLines): #0,1,2,3
    for innerLoopVar in range(0, outerLoopVar+1): #i=0  j =0
        print(outerLoopVar+1, end='')             #i=1  j =0,1
    print('')                                     #i=2  j =0,1,2
                                                  #i=3  j =0,1,2,3
print('-------------------------')
for outerLoopVar in range(1, numbOfLines+1):      #1, 2, 3, 4, 5
    for innerLoopVar in range(1, outerLoopVar+1): #i=0  j =0
        print(innerLoopVar, end='')               #i=1  j =0,1
    print('')                                     #i=2  j =0,1,2
                                                  #i=3  j =0,1,2,3
print("normal execution")

