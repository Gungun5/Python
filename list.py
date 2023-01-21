#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:
#List Items
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#Ordered
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list
#create list
a =['banana','cherry','mango','apple']
print(a)
print(a[0])
print(a[2])
print(a[2])

for x in a:
    print(x)
#find the length of list
print(len(a))
#find the type of list
print(type(a))
#list constructor
a=list(('a','b','c','d','e'))
print(a)
#accessing list items
b=['a','b','c','d','e']
print(b[2])
print(b[0:3])
print(b[:4])
print(b[2:])
print(b[1:4:2])
#change item from list
b[0]='A'
print(b)
#add item in list
#append is used to add item in last of list
print(b.append('f'))
print(b.insert(3,'D'))
#extend two list in one list
print(a.extend(b))
#The extend() method does not have to append lists,
#  you can add any iterable object (tuples, sets, dictionaries etc.).
list1 =['mango','banana','cherry']
tuple1=('A','B','C','D','E')
print(list1.extend(tuple1))
#remove list item from list
print(list1.remove('mango'))
print(list1.pop())
del list1[1]
print(list1)
del a
list1.clear()
print(list1)
#loops through list
list2=['a','b','a','g','g']
for x in list2:
    print(x)
for i in range(len(list2)):
    print(list2[i])
#list comprehension
ls =[1,2,3,6,4,5,6]
ls1 =[ x for x in ls if x==6]
print(ls1)
#sorting in list with sort()
ls.sort()
print(ls)
#sort the list with 'reverse true'
ls.sort( reverse = True) 
print(ls)
#case insensitive sorting
list1.sort( key = str.lower)
print(list1)
#reverse a list
ls.reverse()
print(ls)
#copy a list with copy()
ls2=[2,36,5,8,98,5,5,5]
ls3 = ls2.copy()
print(ls3)
#join list
ls4 = ls2 + ls1
print(ls4)
#join with loop
for x in ls2:
    ls.append(x)
print(ls)
#with extend()
ls.extend(ls2)
print(ls)
