'''
Types of parameters in python:

1. Posistional
2. Variable name based or keyword based 
3. Default Parameters
4. Variable length
'''

#codefor variable arguments
def add(*a):
    sum=0
    for i in a:
        sum +=i
    return sum

#print(add(10,20,30))


#
#the functuions which take as an argument another func. are
# filter
#
#   

def even(n):
    if n%2==0:
        return True
    else: 
        return False

nums = [1,2,3,4,5,6,7,8,9,10]

'''c = list(filter(even,nums))
print(c)'''

print(filter(even,nums))


#Map function:
#write a function square() to return a square and apply map() on a list of numbers

'''def square(x):
    return x*x
li = [1,2,3,4,5]

m = list(map(square,li))
print(m)'''

#reduce
#the reduce function is present in functools module, it accepts an iterator

'''
c = [1,2,3,4,5]
l = list(map(lambda x : x * x,c))
print(l)

import functools as ft
strings = ['Ninad', 'Shrikant', 'Sumant']
ml = ' '.join(strings)
print(ml)

ll = ft.reduce(lambda x,y: x +' '+ y,strings)
print(ll)
'''

#nested functions and decorators
def func1(func):
    def inn(a,b):
        if b==0:
            print("Cant divide")
        else:
            return func(a,b)    
    return inn

@func1    
def div(a,b):
    print(a/b)

div(10,10)
