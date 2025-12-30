"""
Operators
* Operators are used to perform operations on variables and values. Python has the following operators
-> Arithmetic Operators
-> Comparison Operators
-> Logical Operators
-> Bitwise Operators
-> Assignment Operators
-> Identify Operators
-> Membership Operators
"""
# Arithmetic Operators
x = 5
y = 2
# Addition
print(x+y)
# Subtraction
print(x-y)
# Multiplecation
print(x*y)
# Division
print(x/y)
# Modulus
print(x%y)
# power of operator
print(x ** y)
# Integer Division
print(x // 2)

# Comparison Operators
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

# Logical Operators
x = True
y = False
print(x or y)
print(x and y)
print(not y)
print(not x)

# Bitwise Operators
x = 2
y = 3
print(x & y)
print(x | y)
print(x >> 2)
print(y << 3)
print( ~y)
print( ~x)

# Assignment
a = 3
print(a)

a += 3
# a = a + 3
print(a)
"""
We can also do this
a -= 3
a *= 3
a &= 3 

We can't do this
a++
++a
"""
# Identify Operators

a = 3
b = 3
print (a is b) #O/P : True

a = [1, 2, 3]
b = [1, 2, 3]
print (a is b) #O/P : False

a = "Hello-world"
b = "Hello-world"
print (a is b) #O/P : True
print (a is not b) #O/P : False

# Membership Operator
x = "Delhi"
print("D" not in x) # O/P: False
print("D" in x) # O/P: True
x = (1,2,3)
print("5" in x) # O/P: False
