class ArithmeticOperations:

    def __init__(self, msg):
        self.res = 0
        print(msg)
    def sum(self, numb):
        self.res = self.res+numb
    def sum(self, numb1, numb2=10):
        self.res = self.res+numb1+numb2
    def sum(self, numb1, numb2=20, numb3=40):
        self.res = self.res+numb1+numb2+numb3
    def diff(self, numb):
        self.res= self.res-numb
    def mult(self, numb):
        self.res= self.res*numb

obj = ArithmeticOperations(6)
obj.sum(10)
obj.sum(10, 5)
print(obj.res)