#Pyhton Decorators

'''#W.A.P which uses decorators for divide function, the divide function takes two parameters and returns "a/b"
def smart_division(func):
    def inner(a,b):
        if b == 0:
            print("can't divide by 0")
        else:
            return func(a,b) 
    return inner 

@smart_division
def division(a,b):
    return a/b

print(division(10,33))
print(division(10,0))'''

#W.A.P to to write a function to convert any string into upper case, using decorators.

def smart_text(func):
    def inner(name):
        name_upper = name.upper() 
        return name_upper

    return inner

@smart_text
def text(name):
    print(name)

print(text("ninad"))
print(text("NinAD"))