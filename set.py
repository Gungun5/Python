'''Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.
* Note: Set items are unchangeable, but you can remove items and add new items.
Sets are written with curly brackets.'''
set1 ={'apple','banana','cherry','kiwi'}
print(set1)
#find length of set
print(len(set1))
#check type 
print(type(set1))
#access set
for x in set1:
    print(x)
print('apple' in set1)
print('guava' in set1)
#add item in set with add()
print(set1.add('mango'))
#update item in set with update()
set2={'car','house','light','fan'}
set1.update(set2)
print(set1)
#remove items from set with remove() and discard()
set1.remove('fan')
set1.discard('car')
set1.clear()
print(set1)
set3={1,23,5,4,7,8,5}
del set3
print(set3)
