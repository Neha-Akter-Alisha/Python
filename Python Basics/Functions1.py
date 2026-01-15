'''
Docstring for Function Arguments:

Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

* From a fnction perspective Parameters vs Arguments are given below:
-> A parameter is the variable listed inside the parentheses in the function definition.
-> An argument is the actual value that is sent to the function when it is called.

* Number of arguments:
-> By default a function must be call with the correct number of argumets. Like if u have 2 arguments, you have to call 2 arguments.
   or else it will show error.

* Default Parameter values:
-> If the function is called without an arguments, we can assign default values to parameters.

* keyword arguments:
-> We can send arguments with the key = value syntax.
-> Note: The phrase Keyword Arguments is often shortened to kwargs in Python documentation.

* Positioonal Arguments
-> When you call a function with arguments without using keywords, they are called positional arguments.
-> Note: Postional arguments must be in correct order.
'''

# Example of Arguments:
def my_function(info):
    print("Neha", "Alisha's" + info )

my_function(" Email Address ")  # o/p: Neha Alisha's Email Address
my_function(" Phone no. ")      # o/p: Neha Alisha's Phone no.
my_function(" Linus ")          # o/p: Neha Alisha's Linus

# Example of Parameter vs Arguments:
def my_func(name): # name is a parameter
    print("Hello", name)

my_func("Email")   # "Email" is an argument

# Example of Number of Arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil of", "Neha")

# Example of Default Parameter values:
def func(country = "Norway"):
   print("I am from", country)

func("India")        # o/p: I am from India
func("Bangladesh")   # o/p: I am from Bangladesh
func()               # o/p: I am from Norway


# Example of keyword Arguments: 
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# Example of Positional Arguments:
def func(animal, name):
   print("I have a ", animal)
   print("My", animal + "'s name is", name)

func("cat", "Elsa")
