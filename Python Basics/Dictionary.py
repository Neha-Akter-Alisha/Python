'''
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates. Dictionaries are written with curly brackets, and have keys and values:
-> Note: As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
A dictionary is:
-> Unordered (Python 3.7+ keeps insertion order, but conceptually unordered)
-> Mutable
-> Key-Value pairs
-> Keys must be unique
-> Values can be duplicated
-> Keys must be immutable (str, int, tuple)
-> A dictionary cannot have two keys with the same name.
'''

# 1. How to Create a Dictionary
# Basic
student = {"name": "Neha", "age": 21, "course": "Python"}

# Using dict() constructor
info = dict(name="Eva", age=20)

# Empty dictionary
a = {}
a = dict()
print(a)

# 2. Access Dictionary Items
# Using key
print(student["name"])

# Using get() (safe)
print(student.get("age")) # If key not found → returns None, no error.


# 3. Change / Edit Dictionary Items
student["age"] = 22

# Adding new key-value
student["city"] = "Kolkata"



# 4. Dictionary Methods for Update
# update() — add or modify multiple keys
student.update({"city": "Delhi", "course": "Advanced Python"})


# 5. Remove Items
# pop() — remove using key
student.pop("age")

# popitem() — removes last inserted item
student.popitem()

# del — remove specific key
del student["name"]

# del dictionary completely
del student

# clear() — empty dictionary
student.clear()


# 6. Check if Key Exists
if "name" in student:
    print("Exists")


# 7. Looping in Dictionary
student = {"name": "Neha", "age": 21, "course": "Python"}

# Loop through keys (default)
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key–value pairs
for key, value in student.items():
    print(key, "=", value)

# Loop using enumerate()
for i, (k, v) in enumerate(student.items()):
    print(i, k, v)


# 8. Dictionary Length
print(len(student))


# 9. Dictionary Copy
# copy()
new_dict = student.copy()

# dict() method
new_dict = dict(student)


# 10. Nested Dictionaries
students = {
    "student1": {"name": "Neha", "age": 21},
    "student2": {"name": "Eva", "age": 20}
}

# Access:
print(students["student1"]["name"])


# 11. Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)


# 12. Keys must be immutable

# Valid keys:
{1: "int", "name": "string", (1,2): "tuple"}

# Invalid:
{[1,2]: "list"}   # It will give error (unhashable)


# 13. Built-in Dictionary Methods (Most Important)
'''
<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
|  Method      |	Description         		    |  	       	       Example Code	          	    |  	            Output                                                           |
|keys()	       | Returns all keys	       	        |	       student.keys()		     	        |	       dict_keys(['name', 'age', 'course'])                                  |                   
|values()      | Returns all values    	   	        |	       student.values()	       		        | 	       dict_values(['Neha', 21, 'Python'])                                   |
|items()       | Returns key-value pairs 	        |	       student.items()	       		        |	       dict_items([('name','Neha'), ('age',21), ('course','Python')])        |
|get()	       | Returns value of key	 	        |	       student.get("name")		    	    | 	       Neha                                                                  |
|fromkeys()    | Creates dict with keys & same value|	       dict.fromkeys(["a","b","c"], 0)	    | 	       {'a': 0, 'b': 0, 'c': 0}                                              |
|setdefault()  | Adds key if not exists	            |	       student.setdefault("city","Delhi")	|          DelhiOnly adds if the key doesn’t exist)                              |
|update()	   | Updates dictionary	                |	       student.update({"age": 22})		    |          {'name':'Neha','age':22,'course':'Python'}                            |
|pop()	       | Removes key	                    |	       student.pop("age")	                | 	       21                                                                    |
|popitem()	   | Removes last item 	       	        |	       student.popitem()	                |	       ('course','Python')                                                   |
|copy()	       | Returns copy		       	        |	       student.copy()	                    |	       New dictionary                                                        |
|clear()       | Removes all items	       	       	|	       student.clear()	                    | 	       {}                                                                    |
<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
'''
# 14. Convert Between Data Types
# List of tuples → dict
pairs = [("name", "Neha"), ("age", 21)]
d = dict(pairs)
