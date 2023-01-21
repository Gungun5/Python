'''Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Dictionaries are written with curly brackets, and have keys and values:
Dictionary items are ordered, changeable, and does not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
'''
#create dictionary
dict1 ={'a':52,'b':25 ,'C':65}
print(dict1)
#find length
print(len(dict1))
#check type
print(type(dict1))
print(dict1.keys())
print(dict1.values())
#change items
dict1['a']=89
print(dict1)
dict1.update({'b':36})
print(dict1)
#add item in dict
dict1['e']=84
print(dict1)
#remove item from dict
dict1.pop('a')
dict1.popitem()
del dict1['C']
print(dict1)
dict1.clear()
print(dict1)
for x in dict1:
    print(x)
    print(dict1[x])
for x in dict1.values():
    print(x)
for x in dict1.keys():
    print(x)
for x,y in dict1.items():
    print(x,y)
#copy dict 
dict2=dict1.copy()
print(dict2)
#copy with dict()
dict3 = dict(dict1)
print(dict3)
#nested dictionary
student_detail ={'st1':{'name':'gungun','class':'CSE','RollNo.':413},'st2':{'name':'raj','class':'CSE','RollNo.':414}}
print(student_detail['st1'])
