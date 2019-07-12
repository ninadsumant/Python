#Q.1 WAP to create simple calculator

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

while True:
    print("1. Addition \n2. Subtraction \n3.Division \n4 Multiplication")
    print("Enter your choice :")
    choice = input()
    print("Enter the number 1")
    a = int(input())
    print("Enter the number 2")
    b = int(input())
    if choice == '1':
        print("Addition is: \n",add(a,b))

    elif choice == '2':
       print("Subtraction is: \n",sub(a,b))
    
    elif choice == '3':
        print("Division is: \n",division(a,b))

    elif choice == '4':
        print("Multiplication is: \n",multiply(a,b))

#Q.2 consider a list of a number and display smallest number, largest number and second largest number


#Q.3 consider a sentence and reverse each wordt of a sentence



'''
Q.4 WAP to display factors of a number
'''
'''
def factors(num):
    print("factors of given numbers are: ")
    for i in range(1,num+1):
        if num % i == 0:
            print(i)

print("Enter any number :")
num = int(input())
factors(num)

'''

'''
Q.5 Factorial using recursion
'''

'''
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)

print("Enter the number")
num = int(input())
print("Factorial is :",factorial(num))
'''

#Q.6 find GCD and LCM of a number


'''
Q.7 print the following pattern

*
***
*****
*******

'''

'''
for i in range (5):
    for j in range(i):
        print("* ",end=" ")
    print("\n")    
'''


#Q.8 consider a list and implement following sorting techniques
#Bubble sort, insertion sort, merge sort, quick sort


#Q.9 Consider a list and implement binary search algorithm
'''
def binarySearch(array, target):
    return binarySearchHelper(array,target,0,len(array) - 1)

def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle + 1
        else:
            left = middle + 1
    return -1

array = [1,2,3,4,5]
target = 3
print(binarySearch("Number is present at position :",array, target))
'''