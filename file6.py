#OOP CONCEPT

class classOne:
    def funcOne(self):
        print("hello world")
    def functionTwo(self):
        print("hello world 2") 



obj1= classOne()
obj1.funcOne()
obj1.functionTwo()

obj2= classOne()
obj2.funcOne()
obj2.functionTwo()


class person():

    def __init__(self,name,age,address): #dunder method as it has double underscore
        self.name=name
        self.age=age
        self.address=address
    def printInfo(self):
        print(self.name,self.age,self.address)

hello= person(name="sailesh", age=23, address="kathmandu")
hello.printInfo()

#encapsulation -> grouping of related attributes and methods
#inheritance
class addresss(person):
    def add(self):
        print("i live in nepal")






    
    