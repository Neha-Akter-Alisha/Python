"""
There are two types of typing:
-> Dynamic Typing: where we don't have to spacify the datatypes name before writing a variable name. Ex: Python,PHP
-> Static Typing: where we have to specify the datatypes name before writing a variables name. Ex: C,C++,Java
"""
# In C lang--> int a = 5;
# In Python
name = "Hello World"
print(name)
name = 5
print(name)
# A varaiable that can store multiple data is called Dynamic binding
# -> Here we can change a variable datatype
# But in C,C++,Java we use static Binding
# special syntax

#1
a = 2; b = 3; c = 4
print(a)
print(b)
print(c)
#2
a,b,c = 2,3,4
print(a)
print(b)
print(c)
#3
a = b = c = 7
print(a)
print(b)
print(c)
#4 
a=b=c=5
print(a,b,c)