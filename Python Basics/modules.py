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
