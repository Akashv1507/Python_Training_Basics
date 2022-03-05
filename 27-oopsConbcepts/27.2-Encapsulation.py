from matplotlib.pyplot import cla


class Database:

    def __init__(self, extDbUserName, extDbPass, extDbName) :
        self._dbUserName= extDbUserName # protected access modifier
        self.__dbPass = extDbPass       # private access modifier(private to class)
        self.dbName = extDbName         # public access modifier

    def getDbPass(self):
        self.dbPass = self.__dbPass
        return self.dbPass 
    def changePass(self, bias):
        self.__dbPass = self.__dbPass+ f"{bias}"

db1 = Database("mayank", "12345", "python_projects")

# this is a not  encapsulation/public attribute is changed
db1.dbName = "hey i have changed your name.. you have not implemented encapsulation properly"
print(db1.dbName)

# this is not a encapsulation
db1._dbUserName = "hey this is protected but it can be changed in python"
print(db1._dbUserName)

# you tried changing pass, but didnt changed due to privatr in nature
db1.__dbPass = "hey I have changed your pass"

# this is an encapsulation private member/attribute accessed thorough method
print(db1.getDbPass())
# this is an encapsulation private member/attribute changed thorough method
db1.changePass("_changed")
print(db1.getDbPass())



