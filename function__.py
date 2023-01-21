'''A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''
def my():
    print('hello')
my()#calling a fun
'''Arguments
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
'''
def name(fname):
    print("my name is :-",fname)
name('gungun')
name('gaiyu')
name('naitik')
name('ashu')
name('rajan')
def name1(*kids):
    print('hello :',kids)
    print('hello :',kids[1]) #In this, index 1 item will print
name1('good','better','excellent')
def name2(**kids):
    print('my name is : ',kids)
name2(4)