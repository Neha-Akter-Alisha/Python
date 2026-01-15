'''
Docstring for Functions:

A function is a block of code which only runs when it is called. A function helps avoiding code repetition.
# Creating a function: In Python, a function is defined using the def keyword, followed by a function name and parentheses:
# Calling a function: To call a function, write down it's name with parentheses. Example:
def neha():
    print("Hello my name is Neha")
neha()      # O/P: Hello my name is Neha


# Rules for function names:
-> A function name must start with a letter or underscore. Example: calculate_sum() # Valid function names
-> A function name can only contain letters, numbers, and underscores.  Example: _neha_function() # Valid function names
-> Function names are case-sensitive (myFunction and myfunction are different).  Example: myFunction2() # Valid function names

* Return Values:
When a function reaches a return statement, it stops executing and sends the result back

* Pass Statement:
The pass statement is often used when developing, allowing you to define the structure first and implement details later.
'''
# Example:

name = ("Neha","Akter")
def name_function():
    return(name)          # return statement
message = name_function()
print(message)

def my_func():
    pass                  # pass statement
