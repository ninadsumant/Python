'''
Modules:
It means a design technique to split your code into 2 parts. And these parts are called as modules. Here we try to see, there is no or minimal dependency on modules.
To create a module.
'''
#Q.1 WAP to create the module which has following functions
#display weather number is palindrom or not, display n fibonacci series

'''
def palindrome(data):
    newdata = reversed(data)
    if list(newdata) == list(data):
        print("Palindrome Number")
    else:
        print("Not Palindrome")

print("Enter the number")
data = input()
palindrome(data)


def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

print("Enter number for fibonacci series:")
num = int(input())
print("Fibonacci is :",fibonacci(num))
'''


'''
Built in modules:
they are weitten in C language & integrated using python interpreter.
'''

'''
import sys
import math
import datetime
print(sys.api_version)
print(sys.path)
print(math.factorial(10))
print(datetime.date.today())
'''
'''
Python module search path:
when we impoet the module, python searches for the module at certain places, if we cannot find the module in the built in modules it searches through the list
in sys.path
'''


'''
Self:
in python class methods must have an extra parameter in method definition. The value for this parameter is not given when we call the method.
python privides it. Even if a method doesent take any arguments, still we need to specify the argument as self. Is similar to this pointer in C++. and this reference 
in Java.

__init__ is similar to constructor in C++ or Java. It is executed as soon as object of class is instantiated. It is useful for initilization purpose.
E.g : create a class named as student initilize roll number by using init method. and display his roll number in method called display
'''

'''
class student:
    def show(self):
        print("Roll Number is :",self.rno)

    def __init__(self,rno):
        self.rno = rno
obj = student(4)
obj.show()
'''

#crete a class circle use a constructor to initilize calculate area of circle
'''
class Circle:
    def area(self):
        circleArea = 3.14*(self.radius*self.radius)
        print("Area is :", circleArea)

    def __init__(self, radius):
        self.radius = radius

circle = Circle(5)
circle.area()
'''
#create a class named as rectangle use l,w and calculate the area and display
'''
class Rectangle:
    def rectArea(self):
        rectangleArea = self.length * self.breadth
        print("Area of Rectangle is :", rectangleArea)

    def __init__ (self, length, breadth):
        self.length = length
        self.breadth = breadth

rect = Rectangle(2,4)
rect.rectArea()
'''

#create a class named as student consist of class variable stream which is initilized with value, use init method and initilize rno
#create 2 objects and display stream and rno

'''
class Student:
    stream = 'Science'

    def __init__(self,rno):
        self.rno = rno
    
    def display(self):
        print("Stream is :",self.stream)
        print("Roll number is :",self.rno)

obj = Student(10)
obj.display()
'''

#create an empty class.
#pass is the special statement in python that does nothing it works as a dummy statement

def aa():
    pass
    