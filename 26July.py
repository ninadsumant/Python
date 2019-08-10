#PICKLE in python
'''
Pickle is used for serializing(marshaling or flateining) & deserializign python object structures i.e it is a process of converting of
object in memory to a bite stream that can be stored on disk or sent over a network. De-serializing means conerting a char string into Object
The datatypes can be pickeled are Integers, Floats, Complex numbers, Strings, Tuples, List, Set

'''
#Q.1 consider a list with 5 values, consider a file pickle the list in the file. (pickle.dump()) is used.

import pickle
'''
my_list = [1,2,3,4,5]
filename = 'nums'
outfile = open(filename,'wb')
pickle.dump(my_list,outfile)
outfile.close()
'''
filename = 'nums'
infile = open(filename,'rb')
new_list = pickle.load(infile)
infile.close()
print(new_list)



#Q.2 consider a data dictionary and pickle it as well as unpickle and display the data
my_dict = {1:"One",2:"Two"}
filename = 'dicti'
outfile = open(filename,'wb')
pickle.dump(my_dict,outfile)
outfile.close()


filename = 'dicti'
infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()
print(new_dict)

import bz2

sfile = bz2.BZ2File('smallerfile', 'w')
pickle.dump(my_dict, sfile)