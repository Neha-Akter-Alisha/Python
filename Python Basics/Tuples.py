'''
1) What is Tuple ?

-> Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary,
all with different qualities and usage. Tuples are written with round brackets.
A tuple is a collection which is ordered and unchangeable.
Tuple items are ordered, unchangeable, and allow duplicate values.

-> Ordered: When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
-> Immutable (❗cannot change after creation): Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
-> Indexed: Tuple items are indexed. 
-> Allows duplicate values: The first item has index [0], the second item has index [1] etc.
-> Can store mixed data types
'''
# How to create a Tuple: 

# Basic Tuple: 
fruits = ("apple", "banana", "mango")
print(fruits)

# Simple Tuple:
x = ("apple",)     # must use comma # O/P: ('apple',)
print(type(x))     # O/P: <class 'tuple'>
print(x)           # O/P: ('apple',)

# Tuple without parenthesis:
my_tuple = 1, 2, 3
print(my_tuple)    # O/P: (1, 2, 3)

# Access Tuple Items (Indexing):
fruits = ("apple", "banana", "mango", "orange")
print(fruits[0])    # O/P: apple
print(fruits[-1])   # O/P: orange  (last item)

# Slicing Tuples:
fruits = ("apple", "banana", "mango", "orange")
print(fruits[1:3])     # O/P: ('banana', 'mango')
print(fruits[:2])      # O/P: ('apple', 'banana')
print(fruits[2:])      # O/P: ('mango', 'orange')
print(fruits[:])       # O/P: whole tuple

# How to Edit a Tuple (Indirect Way)
# Since tuples are immutable, convert to list → edit → convert back.
a =(1, 2, "apple")
temp = list(a)
temp[0] = "mango"
a = tuple(temp)        # O/P: ('mango', 2, 'apple')
print(a)

# Add Items to Tuple
# Method 1: Convert to list → append → back to tuple
a = (1, 2, 3)
x = list(a)
x.append(4)
a = tuple(x)

# Method 2: Tuple Concatenation
a = (1, 2, 3)
a = a + (4,)
print(a)

# Delete Tuple
a = (1, 2, 3)
del a           # Delete entire tuple. You cannot delete single elements.

# Tuple Operations
a = (1,2)
b = (3,4)
# Concatenation
print(a + b)      # (1,2,3,4)
# Repetition
print(a * 3)      # (1,2,1,2,1,2)
# Membership test
fruits = ("apple", "banana", "mango")
print("apple" in fruits)   # True
print("apple" not in fruits)   # True

#Tuple Functions
# length-> len()
print(len(fruits))
# count() -> Returns the number of times a specified value occurs in a tuple
numbers = (1,2,2,3)
print(numbers.count(2))   # O/P: 2
# index() -> Searches the tuple for a specified value and returns the position of where it was found
print(numbers.index(3))   # O/P: 3rd position → index 3
# max()/min()(only smae-type items)
nums = (4, 1, 8, 2)
print(max(nums))
print(min(nums))
# sum
print(sum(nums))


# Tuple Packing & Unpacking
# Packing
student = ("Neha", 21, "Python")
# Unpacking
student = ("Neha", 21, "Python")
name, age, course = student
print(name)                        # O/P: Neha
print(age)                         # O/P: 21
print(course)                      # O/P: Python
# Unpacking using (Asterisk '*' operator)
#index      [0]      [1]      [2]         [2]         [2]
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#[0]  [1]    [2]
(x,    y,    *z) = fruits

print(x)                # O/P: apple
print(y)                # O/P: banana
print(z)                # O/P: ['cherry', 'strawberry', 'raspberry']
#index      [0]      [1]      [1]         [1]         [2]
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# [0]     [1]    [2]
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


# Python Constructor
thistuple = tuple(("Neha", 21, "Python"))    # note the double round-brackets
print(thistuple)                             # O/P: ("Neha", 21, "Python")

# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

# Loops in Tuples
''' Tuples are iterable, so you can use for loops and while loops exactly like lists.
1. For Loop with Tuple. The most common way.'''


# -> Example 1: Print all items
fruits = ("apple", "banana", "mango")

for item in fruits:
    print(item)


# Example 2: Loop with index
# -> Use range() + len():
fruits = ("apple", "banana", "mango")

for i in range(len(fruits)):
    print(i, fruits[i])


# 2. While Loop with Tuple
# -> We use an index counter.
fruits = ("apple", "banana", "mango")
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1


# 3. Loop with Conditions
nums = (1, 2, 3, 4, 5)

for n in nums:
    if n % 2 == 0:
        print(n, "is even")


# 4. Loop for Searching an Item
fruits = ("apple", "banana", "mango")

search = "banana"

for f in fruits:
    if f == search:
        print("Found:", f)


# 5. Loop with enumerate() (index + value together — best!)
fruits = ("apple", "banana", "mango")

for index, value in enumerate(fruits):
    print(index, "=", value)


# 6. Nested Loops with Tuple
colors = ("red", "blue")
fruits = ("apple", "banana")


for c in colors:
    for f in fruits:
        print(c, f)


# 7. Loop in Tuple of Tuples
students = (
    ("Neha", 21),
    ("Alisha", 22),
    ("Eva", 20)
)

for name, age in students:
    print(name, "is", age, "years old")


# 8. Loop + Tuple Unpacking
points = ((1,2), (3,4), (5,6))

for x, y in points:
    print("x =", x, ", y =", y)


# 9. Loop + Sum / Max / Min (Manual)
nums = (3, 5, 7, 2)

total = 0
for n in nums:
    total += n

print(total)


'''Python Collections (Arrays)
There are four collection data types in the Python programming language:
-> List is a collection which is ordered and changeable. Allows duplicate members.
-> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
-> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
-> Dictionary is a collection which is ordered** and changeable. No duplicate members.'''


'''
Note:
-> Set items are unchangeable, but you can remove and/or add items whenever you like.
-> As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.'''