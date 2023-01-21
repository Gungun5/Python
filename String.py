#string
a='hello world'
b="hello"
print(a[1])
#looping through string 
for x in b:
    print(x)
#string length
print(len(a))
#check string
print('hello' in a) 
#if not in string
print('my' not in a)
#slicing in string
c='Gungun Gaiyu'
print(c[1:9])
#slice from the start
print(c[:5])
#slice from end
print(c[3:])
#slice by steps
print(c[1:8:2])
#modify strings
#uppercase
print(a.upper())
#lowercase
print(c.lower())
#remove Whitespace with strip()
print(c.strip())
#replace string with replace()
print(c.replace('G','m'))
#split() is used to split and turn into list
print(c.split( ))
#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
name='Gungun'
print("my name is {}".format(name))
print(f'my name is {name}')
#return string in center 
print(a.center())
#return first string  Capitalize
print(a.capitalize)
#return string into lowercase with casefold
print(c.casefold())
#count the string that how many time 
print(a.count('l'))

