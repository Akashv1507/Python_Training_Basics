class Calculator:
    # this is a class variable
    pi = 3.14
   
    def __init__(self, extMsg, extNumb1, extNumb2, prvtNumb):
        #self-> current instance/object
        #self.msg-> instance/variable
        self.msg = extMsg
        self.numb1= extNumb1
        self.numb2 = extNumb2

    def addition(self):
        return self.numb1+self.numb2
    
    def subtraction(self, extBias):
        return self.numb1-self.numb2 + extBias
    
    def printMsg(self):
        print(self.msg)

obj1 = Calculator("this is a constructor", 10, 5, 3)
obj2 = Calculator("this is a second object/instance", 20,7, 3)

# accessing class variable
print(Calculator.pi)

# accessing method PrintMasg with obj1
obj1.printMsg()
# accessing instance variable of obj1
print(obj1.numb1)
# accessing method PrintMasg with obj2
obj2.printMsg()

# accessing method Addition with obj1
print(obj1.addition())
# accessing method subtraction with obj2
print(obj2.subtraction(6))
print(obj1.subtraction(6))




