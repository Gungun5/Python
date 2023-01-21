#Tuple
'''Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable allow duplicate values.
Tuples are written with round brackets.
'''
#create tuple
a = (1,2,3,654,6)
print(a)
#find length with len()
print(len(a))
#find type with type()
print(type(a))
print(a[0])
print(a[1:4])
if 2 in a:
    print(a)
else:
    print('false')
#update the value in tuple
a=(1,2,3,5,12)
b=list(a)
b[3]=4
a=tuple(b)
print(a)
#add item in tuple tuple is immutable so there is no built-in append()
c=list(b)
c.append(25)
a=tuple(c)
print(a)
#second method to add item in tuple
d=(5,)
a+=d
print(a)
#remove item from tuple
re = list(a)
re.remove(5)
a = tuple(re)
print(a)
#del keyword is uesd to delete all items from tuple
#del a
#print(a)
#looping with tuple
for x in a:
    print(x)
for x in range(len(a)):
    print(a[x])

