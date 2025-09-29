#Classes are user defined blueprint or prototype
#sum, multiplication, addition, constant
#Methods, class variables, instance variables, constructor, etc.
#Self keyword is mandatory for calling variable names into method
#Instance and class variables have whole different purpose
#Constructor name should be __init__
#New keyword is not required when you create object

class Calculator:
    num = 100    #Class variables
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num


obj = Calculator(2, 3)    #Syntax to create objects in python
obj.getData()
print(obj.Summation())

obj = Calculator(4, 5)    #Syntax to create objects in python
obj.getData()
print(obj.num)