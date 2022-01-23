# typecasting string into integer
number = int(input ("Please enter number whose table you want to print : "))
sum =0

for i in range(1,11):
    print(number*i)

print('---------------------------------')

for i in (1,2,3,4,5,6,7,8,9,10):
    print(number*i)

print('---------------------------------')

# executing our code logic without using loop variable.
for i in range (10,20):
    print(sum+number)
    sum = sum + number