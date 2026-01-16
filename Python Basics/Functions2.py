'''
Docstring for Decorators:
-> Decorators let you add extra behavior to a function, without changing the function's code.
-> A decorator is a function that takes another function as input and returns a new function.

* Basic Decorators:
-> A decorator is a function that modifies the behavior of another function without changing its source code.

* Multiple decorators:
-> A decorator can be applied to multiple functions, and it will run separately for each function call.

* Arguments in the Decorator Function:
-> When a decorated function accepts arguments, the decorator must handle those arguments.

* *args and **kwargs in Decorators:
-> *args and **kwargs allow a decorator to work with any number of positional and keyword arguments.

* Decorator with Arguments (Decorator itself takes parameters):
-> A decorator with arguments requires three levels of functions:
-> Decorator arguments
-> Actual decorator
-> Wrapper function

*  Multiple Decorators (Stacked Decorators):
-> Multiple decorators can be applied to a function and are executed from bottom to top.

* Preserving Function Metadata (functools.wraps):
-> Decorators hide the original function’s metadata (__name__, __doc__). functools.wraps preserves it.
'''

# Example of Basic decorators:
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

# Example of Basic decorators:
def log(func):
    def wrapper():
        print("Function called")
        func()
    return wrapper

@log
def task1():
    print("Task 1")

@log
def task2():
    print("Task 2")

task1()
task2()

# Example of Basic decorators:
def decorator(func):
    def wrapper(name):
        print("Before function")
        func(name)
        print("After function")
    return wrapper

@decorator
def greet(name):
    print(f"Hello {name}")

greet("Alisha")

# Example of Basic decorators:
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        func(*args, **kwargs)
        print("After function")
    return wrapper

@decorator
def add(a, b):
    print(a + b)

add(3, 5)

# Example of Basic decorators:
def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")

hello()

# Example of Basic decorators:
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def show():
    print("Inside function")

show()

# Example of Basic decorators:
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def demo():
    """This is a demo function"""
    print("Hello")

print(demo.__name__)
print(demo.__doc__)

