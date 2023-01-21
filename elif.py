'''
The elif statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE.

Similar to the else, the elif statement is optional. However, unlike else, for which there can be at most one statement, there can be an arbitrary number of elif statements following an if.

syntax :- 
if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)
'''
#example :-
a=int(input('enter no.:-'))   #input() is used for take input from user
if a==5:
    print(a,'is 5')
elif a==10:
    print(a,'is 10')
elif a==15:
    print(a,'is 15')
elif a==20:
    print(a,'is 20')
else:
    print('choose another no.')