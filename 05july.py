'''
IF statement:
'''

#Q1. take a number and check wheather it is positive or negative

a = 11
if a>0:
    print("Positive")
else:
    print("Negative")


#Q2. Even and Odd

if a%2==0:
    print("Even")
else:
    print("Odd")


#Q3. consider a listnof 5 elements & display each elmt using loops

lst = [1,2,3,4,5]
print("Printing List")
for i in lst:
    print(i)

#Q.4 consider tuple of 5 elements & display each element
tup = (1,2,3,4,5)
print("Printing Tuple")
for i in tup:
    print(i)

#Q.5 consider dictionary and display it in pair
myDict = {1:"one",2:"two",3:"three"}
print("Printing Dictionary")
for i, j in myDict.items() :
    print(i , j)
    

#Q.6 consider s string and display each char. of the string
str = "Hello World"
print("Printing each char of string")
for i in str :
    print(i)


#Q.7 implement bubble sort
print("Implementing Bubble Sort :")
array = [2,4,3,7,6,1]
n = len(array)
for i in range(n) :
    for j in range(0,n-i-1):
        if array[j] > array[j+1] :
            array[j], array[j+1]=array[j+1], array[j]
print(array)


#Q.8 consider 2 dictionaries & merge them in one line
firstDict = {1:"one",2:"two",3:"three"}
secondDict = {4:"four", 5:"five"}

secondDict.update(firstDict)
print(secondDict)

#Q.9 consider 2 lists with 6 different integer elements and display intersection of both lists.

fList = [1,2,3,4,5]
sList = [2,3,4,7,9]
sd=fList+sList
print("Printing intersection:")
print(sd)


#Q.10 write a function to display  power of a number without using loop.

def power(x,y) :
    return x**y
print("Printing power:")
print(power(2,2))

#Q.11 WAP to argue with yourself. program must take statements that are typed in a list & change the pronounced and negate them
#you must be changed to I, are must be changed to I'm Not.

positive = ["you","are","a","stupid"]
negative = ["I","am","a","not stupid"]
print("Enter String :")
user = input()
list=user.split()
list1 = []
new = ''
for i in list:
    if i in positive :
        idx=positive.index(i)
        new += negative[idx]
        new += ' '
print(new)

