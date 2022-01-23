for i in [1,2,3,4]:
    for j in [10,20,30]:
        print(i*j, end=',')
    print(i+j, end=',')
print(i,j)

'''o/p
10,20,30,31, 20,40,60,32,30,60,90,33,40,80,120,34,4,30
'''
# 1,2,3,2,3,2,3,4,2,3,2,3,2,3,4

# for i in [1,2]:
#     for j in [10,20]:
#         print('inside inner loop')
#         for k in [100,200]:
#             print('inside very inner loop')
#     print('---------------')
#     print('inside outer loop')
# print("OUTSIDE both loop")

# 9,10,11,12,13,12,13,10,11,12,13,12,13,14,15,9,10...........
