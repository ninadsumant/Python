'''tup = (4,5,2,7,1,9,3)
print (tup)
print (sorted(tup))
print(tup)

str = "Hello World"

#length of string
print (len(str))

#replace l with m in the string
print (str.replace('l','m'))

#count the string
print(str.count('l'))

#find in string
print(str.find('l'))

#split the string
print(str.split(' '))

print(str.join(' '))
#capitelize the first letter of the string
print(str[0].upper().join(str))
'''

'''
integerr = 5
floatt = 2.5

result = integerr + floatt
print(result)

'''
#List
lst=[1,2,3,4,5]
print(lst)
lst1 = [1,2,'hello',2.3]
print(lst1)

#operations on list

#Q.1 consider the list of programming languages & list of spoken languages, append new prog. lang. to 1st list
#insert new spoken language at position 1 in the second list. apply remove function & delete 1 prog. lang.
#display spoken languages in reverse order. sort prog. languages. apply extend() function.

pLang = ['c','c++','java']
sLang = ['marathi','english','hindi']
print(pLang)

pLang.append('python')
print(pLang)

sLang.insert(0,'sanskrit')
print(sLang)

pLang.remove('java')
print(pLang)

sLang.reverse()
print(sLang)

print(sorted(pLang))

sLang.extend(pLang)
print(sLang)

del(sLang[1])
print(sLang)


'''
consider a string Hello World.
1. modify world with there. also reverse 1st word & display the entire list
'''

s = "Hello World"
st = s.replace("World", "There")
print(st)
splitStr = st.split(' ')
print(splitStr)

revStr = splitStr.reverse()
print(revStr)


'''
consider a list and remove duplicates from it.
'''


'''
create a list of even numbers between 1-100
'''



'''
create a list, and
1.print first 3 numbers
2. display numbetrs ommiting 1st and last number
3. display in reverse order
'''
c = [1,4,6,7,9,0]
print(c[:3])
print(c[1:5])
print(c[::-1])


#Dictionary
'''
it is set of unordered key-val pair. the keys must be unique.
dictionary is created using '{ }'.

'''
dict1 = {1:"one", 2:"two"}
print(dict1) 

'''
Q.1 create a dictionary of 5 elements and apply following functions-
1. Append
2. Delete
3. Modify
'''
myDict = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
myDict.popitem()
print(myDict)

#append
myDict[6]="six"
print(myDict)

#update
myDict[1]="Ek"
print(myDict)

#delete
del(myDict[1])
print(myDict)

'''
Q.2 create a dictionary which has keys of datatypes integer & string
'''