'''
Docstring for Lanbda:
-> A lambda function is a small anonymous function.
-> A lambda function can take any number of arguments, but can only have one expression.
-> Syntax:  lambda arguments : expression
-> Lambda functions can take any number of arguments:

* Why Use Lambda Functions?
-> The power of lambda is better shown when you use them as an anonymous function inside another function.
-> Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
-> Note: Use lambda functions when an anonymous function is required for a short period of time.

* Lambda with Built-in Functions
-> Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().
-> Using Lambda with map(): The map() function applies a function to every item in an iterable.
-> Using Lambda with filter(): The filter() function creates a list of items for which a function returns True.
-> Using Lambda with sorted(): The sorted() function can use a lambda as a key for custom sorting

'''


# Example of Lambda
# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

# Multiply argument a with argument b and return the result:
# Lambda functions can take any number of arguments
x = lambda a, b : a * b 
print(x(5, 6))

# Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Examplle of why we use lambda functions
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# Example of Using Lambda with map():
# Double all numbers in a list:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Example of Using Lambda with filter():
# Filter out even numbers from a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# Example of Using Lambda with sorted():
# Sort a list of tuples by the second element:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
