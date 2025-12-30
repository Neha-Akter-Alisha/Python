""" Built-in functions in Python are a set of predefined functions that are readily available for use within the Python interpreter without requiring any explicit import statements. 
# 1- print()
# 2- input()
# 3- type()
# 4- int() #typeconversion function
# 5- abs()
# 6- pow(2,3)
# 7- min()/max()
# 8- round()
# 9- divmod()
# 10- bin()/oct()/hex()
# 11- id()
# 12- ord()
# 13- len()
# 14- sum()
# 15- help()
"""
# Examples of built in funtions: 

name = input("Enter your name: ")

# Tuple of numbers
num = (12.3, 11.5, 13.4)

num1 = 12.3445
power_result = pow(2, 3)       # Calculates 2³ = 8
result = divmod(10, 3)         # Returns (quotient, remainder)
a = 6

print("Type of num:", type(num))
print("Min value:", min(num))
print("Max value:", max(num))
print("Rounded value:", round(num1))
print("Length of your name:", len(name))
print("Sum of num:", sum(num))

print("Name:", name)
print("Power result:", power_result)
print("Divmod result:", result)

print("Binary:", bin(a))
print("Octal:", oct(a))
print("Hexadecimal:", hex(a))
print("Memory ID of a:", id(a))
print("ASCII of 'a':", ord('a'))

help(print)

"""
Enter your name: neha
Type of num: <class 'tuple'>
Min value: 11.5
Max value: 13.4
Rounded value: 12
Length of your name: 4
Sum of num: 37.2
Name: neha
Power result: 8
Divmod result: (3, 1)
Binary: 0b110
Octal: 0o6
Hexadecimal: 0x6
Memory ID of a: 140711437562952     
ASCII of 'a': 97
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
Help on built-in function print in module builtins:

Help on built-in function print in module builtins:
Help on built-in function print in mHelp on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

-- More  --
"""
