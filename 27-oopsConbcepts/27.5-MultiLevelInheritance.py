class Base(object):
     
    # Constructor
    def __init__(self, name):
        self.name = name
        print("level 1")
 
    # To get name
    def getName(self):
        return self.name
 
 
# Inherited or Sub class (Note Person in bracket)
class Child(Base):
     
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
        print("level 2")
 
    # To get name
    def getAge(self):
        return self.age
 
# Inherited or Sub class (Note Person in bracket)
class GrandChild(Child):
     
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
        print("level 3/child")
 
    # To get address
    def getAddress(self):
        return self.address       
 
# Driver code
g = GrandChild("Geek1", 23, "Noida") 
print(g.getName(), g.getAge(), g.getAddress())