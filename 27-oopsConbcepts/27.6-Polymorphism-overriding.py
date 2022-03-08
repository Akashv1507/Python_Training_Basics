class Calculator:
    def __init__(self, msg):
        self.res = 0
        print(msg)
    def method1(self, numb):
        self.res = self.res+numb
    def method2(self, numb):
        self.res= self.res-numb
    def method3(self, numb):
        self.res= self.res*numb

class NewCalculator(Calculator):
    
    def __init__(self, msg):
        # invoking constructor method of parent(Calculator) class
        Calculator.__init__(self, msg)
        pass
    
    def method4(self, numb):
        self.res= self.res/numb
    
    # method 3 and method 2 are overridden, hence it is polymorphism
    def method3(self, numb):
        self.res= self.res-numb
    
    def method2(self, numb):
        self.res= self.res*numb

    def getResult(self):
        return self.res


obj = NewCalculator("this is msg")

obj.method1(5)
obj.method3(4)
obj.method4(2)

print(obj.res)
print(obj.getResult())