'''#Q.1 create Time class with hr, minutes , sec
#create a method add time, which takes 2 time objects and add them.
# E.g : 1hr & 15 mins + 2hr & 30 mins
#create a method display which prints the time, create a method display minute which displays total minuter in given time

class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    def displayTime(self):
        print(self.hr,":",self.min,":",self.sec)

    def addTime(self):
        Addhr = time.hr + time2.hr
        Addmin = time.min + time2.min
        Addsec = time.sec + time2.sec
        print("Addition of time is:")
        print(Addhr,":",Addmin,":",Addsec)

    def totalMinutes(self):
        totalMins = self.hr * 60 + self.min
        print("Total minuts in given time are : ",totalMins)
time = Time(1,15,1)
time2 = Time(2,30,2)
time.displayTime()
time.addTime()
time.totalMinutes()



'''

#balancing brackets
'''myStr = "()()"
def check(myStr):
    openingBrackets = ["(","{","["]
    closingBrackets = [")","}","]"]
    stack = []
    for i in myStr:
        if i in openingBrackets:
            if openingBrackets.index(i) :
                stack.append(i)
            elif i in closingBrackets :
                pos = closingBrackets.index(i)
                if ((len(stack) > 0) and (openingBrackets[pos] == stack[len(stack)-1])):
                    stack.pop()
                else :
                    return 'unbalanced'

    if len(stack) == 0:
        return 'balanced'

print(check(myStr))'''

'''class Student:
    stream = 'Science'

    def __init__(self,rno):
        self.rno = rno
        print("Object Created")
    
    def __del__ (self):

        print ("Object deleted")

    def display(self):
        print("Stream is :",self.stream)
        print("Roll number is :",self.rno)
        

    def creatingObject(self):
        print("Creating object of student class")
        obj1 = Student(11)
        print("Function has ended")
        return obj1

obj = Student(10)

print(obj.creatingObject())
'''

#Ingeritance :

'''
syntax:
class A:
    body of base class

class derived(baseclass):
    body of derived

'''

#create class bird

'''class Bird:

    def __init__(self):
        #self.bird = bird
        print("base class constructor")

    def whoIam(self):
        print("Bird")

    def canISwim(self):
        print("I can swim faster")

    
class Penguine(Bird):

    def __init__(self):
        Bird.__init__(self)
        print("Display some statement")
        

    def whoIam(self):
        Bird.whoIam(self)
        print("Penguine")

    def canIRun(self):
        print("I can run faster")

    
penguine = Penguine()
penguine.whoIam()
penguine.canIRun()
penguine.canISwim()
'''


'''
create a class named as polygon, in the constructor of polygon initilize the number of sides.
crrate a  function to input side. Display the size.
creat child class Trianlge in the ctor, pass the number of size if required. create a function to compute and display area of trianle.


'''
'''
class Polygon :

    def __init__(self):
        print("Enter the number of sides")
        self.sides = int(input())
        print(self.sides,"sides are given")

    
class Triangle(Polygon):

    def __init__(self,sides):
        Polygon.__init__(self)

    def area(self):
        tArea = 0.5 * self.b * self.h 
        return tArea

    def setsides(self,b,h):
        self.b = b
        self.h = h
        

tri = Triangle(3)
tri.setsides(12,3)
print(tri.area())
'''
'''
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

print(MyClass.staticmethod())
print(MyClass.classmethod())
'''

assa

class Polygon :

    def __init__(self, sides):
        self.sides = sides


    
class Triangle(Polygon):

    def __init__(self,sides):
        Polygon.__init__(self, sides)

    def area(self):
        tArea = 0.5 * self.b * self.h 
        return tArea

    def setsides(self,b,h):
        self.b = b
        self.h = h
        
triangle = Polygon(3)
#tri = Triangle(3)
triangle.setsides(12,3)
print(triangle.area())
