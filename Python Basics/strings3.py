''' Operations on Strings
* Arithmatic Operations
* Relational Operations
* Logical Operations 
* Loops on Strings
* Membership Operations
'''
# String Concatenation(Arithmatic Operations):
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
print(a +'-'+ b) # O/P: Hello-World
# To add a space between them, add a " ":
print(a + ' ' + b) # O/P: Hello World
print(a*4) # O/P: HelloHelloHelloHello

# Relational Operation
a = "Hello"
b = "World"
print(a != b) # O/P: True
print(a == b) # O/P: False
'''Lexiographically: The letter which come first in dictionary is smaller and the letter comes later in dictionary is bigger'''
print(a > b)  # O/P: False
c = 'Apple'
d = 'Banana'
print(c < d)  # O/P: True
e = 'apple'
f = 'Apple'
# Capitals comes first so it's smaller than small letters as small letters comes later. And we know which come first is smaller and which come later is bigger
print(e > f) # O/P: True
print(e < f) # O/P: False

# Logical Operation
''' 
Any Empty string is known as False in python
Any non-empty string is known as True in python 
'''
#For python empty strings are false and non-empty strings are true
print("" and "hello") # Here '' means 0 and "hello" means 1 also and means *(Multiply) so 0*1=0. So O/P: ''
print("world" and "hello")
print("" or "hello") # Here '' means 0 and "hello" means 1 also or means *(addition) so 0+1=1. So O/P: 'hello'
print("world" or "hello")
print(not "hello") # O/P: False
print(not '') # O/P: True

# Loops Operators
c = "HI"
for i in c:
    print(i) # O/P: H
             #      I
c = "Hello World"
for i in c[2:3:1]:
    print(i) # O/P: l

# Membership Operators. It has two types'in'/'not in'
print('H' in c) # O/P: True            -> As H is in     c = "Hello World"
print('h' in c) # O/P: False           -> As h is in     c = "Hello World"
print('World' not in c) # O/P: False   -> As World is in c = "Hello World"