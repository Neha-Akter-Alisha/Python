'''
Python supports the usual logical conditions from mathematics:

* Equals: a == b
* Not Equals: a != b
* Less than: a < b
* Less than or equal to: a <= b
* Greater than: a > b
* Greater than or equal to: a >= b
* These conditions can be used in several ways, most commonly in "if statements" and loops.
An "if statement" is written by using the if keyword.'''

# correct email -> neha@gmail.com
# password -> 123

email = input("Enter your email: ")
if "@" in email:
 password = input("Enter your password: ")

 if email == "neha@gmail.com" and password == "123":
    print("Welcome")
    
 elif email == "neha@gmail.com" and password != "123":
    print("Password Incorrect")
    password = input("Enter your password again: ")
    if password == "123":
        print("Finally Correct password")
    else:
        print("Again incorrect password:")

 elif email != "neha@gmail.com" and password == "123":
    print("Email is incorrect")
    email = input("Enter your email again: ")
    if email == "neha@gmail.com":
       print("Finally correct email")
    else:
        print("Still incorrect email")

 else:
     print("Incorrect email or password")
else: 
     print("Email format is not correct")
