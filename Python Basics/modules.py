"""
Modules:

A module is a file containing code written by somebody else (usually) which can be imported and used in our programs.

→ pip is the package manager for python. You can use pip to install a module on your system.

→ Types of Modules

1. Built-in modules: It come with Python by default.

Examples:

import math.        # mathematical functions
import random.      # random numbers.
import sys          # system-specific parameters.


2. User-defined modules: Written by user.

Example:

In one file: #mymodule.py

def greet (name);
    return f"Hello, {name}!"

Then, in another file:

import my module.
print (my module greet ("Neha"))

3. External modules (thired panty): It's installed using pip.

Example:

pip install requests.

Then use it:

import requests
response requests.get("https://api.github.")
print (response. status_cade)

→ How to see all modules which are installed:

help ("modules")

"""
"""
Modules:

A module is a file containing code written by somebody else (usually) which can be imported and used in our programs.

→ pip is the package manager for python. You can use pip to install a module on your system.

→ Types of Modules

1. Built-in modules: It come with Python by default.

Examples:

import math.        # mathematical functions
import random.      # random numbers.
import sys          # system-specific parameters.


2. User-defined modules: Written by user.

Example:

In one file: #mymodule.py

def greet (name);
    return f"Hello, {name}!"

Then, in another file:

import my module.
print (my module greet ("Neha"))

3. External modules (thired panty): It's installed using pip.

Example:

pip install requests.

Then use it:

import requests
response requests.get("https://api.github.")
print (response. status_cade)

→ How to see all modules which are installed:

help ("modules")
Naming a Module
You can name the module file whatever you like, but it must have the file extension .py

Re-naming a Module
You can create an alias when you import a module, by using the as keyword:

Example
Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)
Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.

Example
Import and use the platform module:

import platform

x = platform.system()
print(x)
Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

Example
List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)
Note: The dir() function can be used on all modules, also the ones you create yourself.

Import From Module
You can choose to import only parts from a module, by using the from keyword.

Example
The module named mymodule has one function and one dictionary:

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
Example
Import only the person1 dictionary from the module:

from mymodule import person1

print (person1["age"])
Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]
"""

