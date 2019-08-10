#decorators in python

'''
We can use decorators to extend the functionality of function
without modifying it.
'''

'''
def decor(func):
    def inner(name):
        if name =='shrikar':
            print("Hello Shrikar! bad morning!")
        else:
            func(name)
    return inner


#@decor
def wish(name):
    print("Hello",name,"Good Morning")

decorFunction = decor(wish)
decorFunction("shrikar")
wish("Ninad")
wish("shrikar")
'''

'''
def smart_division(func):
    def inner(a,b):
        if b == 0:
            print("Ayyy bhauuu!! 0 se nahi hoga!!")
        else:
            return func(a,b) 
    return inner 

@smart_division
def division(a,b):
    return a/b

print(division(10,0))
'''
