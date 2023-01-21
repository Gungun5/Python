#Operators are used to perform operations on variables and values.
'''
Python divides the operators in the following groups:
----------------------------------------------------
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
'''
#Arithmetic operators are used with numeric values to perform common mathematical operations:
#In simple words, arithmetic operator used to perform arithmetic operations
#Operator	Name	Example	Try it
'''+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
'''
# here are some arithmetic operators :-
# Addition '+'
a = 5
b = a+5
print(b)
#subtraction '-'
c = 10
d = c-2
print(d)
#multiplication '*'
e = 2 *10
print(e)
#division '/'
f = 8/2
print(f)
#modulus '%' it gives us remainder
n=2%2
print(n)
#exponentiation '**' it gives us power
m=2**5
print(m)
#floor division '//'  rounds the result down to the nearest whole number
o = 15//4
print(o)
# Python Assignment Operator : Assignment operators are used to assign values to variables:
'''
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3
'''
# Python Comparison Operator  :- Comparison operators are used to compare two values:
'''
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y	
'''
# Python Identity operator :- Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

'''
'is' 	Returns True if both variables are the same object	x is y	
'is not'	Returns True if both variables are not the same object	x is not y	

'''
#Python Membership Operators :- Membership operators are used to test if a sequence is presented in an object:

'''
'in' 	Returns True if a sequence with the specified value is present in the object	x in y	
'not in'	Returns True if a sequence with the specified value is not present in the object	x not in y	

'''
#Python Bitwise Operators :- Bitwise operators are used to compare (binary) numbers:
'''
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
^	XOR	Sets each bit to 1 if only one of two bits is 1
~	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

'''
