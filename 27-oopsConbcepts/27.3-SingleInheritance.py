class Calculator:
    def __init__(self, msg):
        self.res = 0
        print(msg)
    def add(self, numb):
        self.res = self.res+numb
    def subtract(self, numb):
        self.res= self.res-numb

class NewCalculator(Calculator):
    
    def __init__(self, msg):
        # invoking constructor method of parent(Calculator) class
        Calculator.__init__(self, msg)
        
    def mult(self, numb):
        self.res= self.res*numb

objNewCal = NewCalculator("ext msg")

print(objNewCal.res)

objNewCal.add(5)
print(objNewCal.res)

objNewCal.subtract(10)
print(objNewCal.res)

objNewCal.mult(5)
print(objNewCal.res)


# objCal = Calculator()

# print(objCal.res)

# objCal.add(5)

# print(objCal.res)

# objCal.subtract(10)

# print(objCal.res)

