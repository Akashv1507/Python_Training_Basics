# logical operator will also retrun boolean value

'''a | b    And     OR     not And      Not Or
   0 | 0 -> 0       0       1           1
   0 | 1 -> 0       1       1           0
   1 | 0 -> 0       1       1           0
   1 | 1 -> 1       1       0           0

   Note- in coding
   0: False
   1:True
'''
# cond1 and cond 2 and cond 3
# precedenc 1. not 2.and   3. or
num1 = 2
num2 = 4
a= True
b= False
c= True

print(a and b and (num2>6))
print(a and c and (num1==num2))
print((a or b)  and (num2<=num1)) #-> print false, since bracket has larger precedence
print(a or b  and (num2<=num1))  # -> print true, since and has larger precedence than or operator
# print( a or b and False)
print(not a)




