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

* Mixing Positional and Keywords Arguments:
-> We can mix postional and keywords arguments but positional arguments must come first before keywords arguments.

* Passing different datatypes:
-> We can send any datatype as an argument to a function but data type will be preserved inside the function

* Return Values:
-> Functions can return values using the return statement:

* Returning Different Data Types:
-> Functions can return any data type, including lists, tuples, dictionaries, and more.

* Positional only Arguments:
-> We can specify that a function can have only positinal arguments.
-> To specify positional-only arguments, add ", /" after the arguments.
-> Without the ", /" we are actually allowed to use keyword arguments even if the function expects positional arguments.
-> With ", /" we will get an error if we try to use keyword arguments.

* Keywords only Arguments:
-> To specify that a function can have only keyword arguments, add "*," before the arguments.
-> Without "*," we are allowed to use positional arguments even if the function expects keyword arguments.
-> With "*," we will get an error if we try to use positional arguments.

* Mixing Postional-Only and keyword-Only
-> We can combine both argument types in the same function.
-> Arguments before "/" are positional-only, and arguments after "*" are keyword-only.

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

# Example of Mixing Positional and Keywords Arguments:
def func(animal, name, age):
   print("I have a", age, "year old", animal, "named", name)

func("dog", name = "Tommy", age = 5)

# Example of Passing different datatypes:
def func(fruits):
   for fruit in fruits:
      print(fruit)

all_fruits = ["apple","orange"]   # Sending a list as an argument
func(all_fruits)

# Example of Return values:
def func(x,y):
   return(x+y)

result = func(3,5)
print(result)

# Example of Different datatypes:

def func():          # A function that returns a list
   return["apple", "orange", "cherry"]

fruits = func()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Example of Positional only Arguments:

# Calling only postional arguments
def calculate_area(length, width, /):
    return length * width
result = calculate_area(5, 10)
print(result)          # o/p: 50
'''
# Trying to use keyword arguments. It will show type error
 result = calculate_area(length=5, width=10)   
 o/p: TypeError: calculate_area() got some positional-only arguments passed as keyword arguments
'''
# Calling Keywords without using "/" 
def calculate_area_no_slash(length, width):
    return length * width
calculate_area_no_slash(5, 10)               # positional
calculate_area_no_slash(length=5, width=10)  # keyword


# Example of Keywords only Arguments:
# Calling function correctly
def create_user(*, username, email):
    print(f"Username: {username}")
    print(f"Email: {email}")
create_user(username="alice", email="alice@gmail.com")

''' 
# Trying to use positional arguments
create_user("alice", "alice@gmail.com")
o/p: TypeError: create_user() takes 0 positional arguments but 2 were given
'''
# Calling fucntion without using * (Positional allowed)
def create_user_no_star(username, email):
    print(f"Username: {username}")
    print(f"Email: {email}")
create_user_no_star("alice", "alice@gmail.com")                 # positional
create_user_no_star(username="alice", email="alice@gmail.com")  # keyword


# Example of Mixing positional and keyword-only arguments:

def book_ticket(train_no, *, seat_type, date):
    print(train_no, seat_type, date)
book_ticket(12345, seat_type="Sleeper", date="2026-01-15")

''' book_ticket(12345, "Sleeper", "2026-01-15") 
o/p: Invalid Call
'''
