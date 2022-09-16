'''
Author: Py Tricks email subscription
Title: Function argument for unpacking
'''

def myfunc(x, y, z):
 print(x, y, z)


tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}


myfunc(*tuple_vec)
myfunc(**dict_vec)
----------------------------------------------------
args = [3, 6]


print(range(3, 6))
print(range(*args))




''' 
1, 0, 1
1, 0, 1
'''
'''
What is Function argument unpacking?:
 We use two operators * (for tuples) and ** (for dictionaries).


The code below is a demonstration of why we need packing and unpacking:
def fun(a, b, c, d):
 print(a, b, c, d)


my_list = [1, 2, 3, 4]


# This doesn't work
fun(my_list)


Now lets use unpacking:
def fun(a, b, c, d):
 print(a, b, c, d)


my_list = [1, 2, 3, 4]


# Unpacking list into four arguments
fun(*my_list)






Sources:
PyTricks-
realpython.com


Geeksforgeeks.org


''' 
