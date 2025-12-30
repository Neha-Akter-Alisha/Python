'''
List:
* What is List?
-> Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary,
all with different qualities and usage.
Lists are created using square brackets.
Example:  a = ["apple", "banana", "cherry"]
          print(a)

* List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
If you add new items to a list, the new items will be placed at the end of the list.
Python has a set of built-in methods that we can use on lists. There are some list methods that will change the order,
but in general: the order of the items will not change. The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
Since lists are indexed, lists can have items with the same value

* List Methods:
<--------------------------------------------------------------------------------------------------->
| Method	       |              Description                                                          |
|---------------------------------------------------------------------------------------------------|
|append()       |   	 Adds an element at the end of the list                                        |
|---------------------------------------------------------------------------------------------------|
|clear()        |  	 Removes all the elements from the list                                        |
|---------------------------------------------------------------------------------------------------|
|copy()         |   	 Returns a copy of the list                                                    |
|---------------------------------------------------------------------------------------------------|
|count()        |     Returns the number of elements with the specified value                       |
|---------------------------------------------------------------------------------------------------|
|extend()       |  	 Add the elements of a list (or any iterable), to the end of the current list  |
|---------------------------------------------------------------------------------------------------|
|index()	       |     Returns the index of the first element with the specified value               |
|---------------------------------------------------------------------------------------------------|
|insert()       |     Adds an element at the specified position                                     |
|---------------------------------------------------------------------------------------------------|
|pop()          |     Removes the element at the specified position                                 |
|---------------------------------------------------------------------------------------------------|
|remove()       |     Removes the item with the specified value                                     |
|---------------------------------------------------------------------------------------------------|
|reverse()      |  	 Reverses the order of the list                                                |
|---------------------------------------------------------------------------------------------------|
|sort()	       |     Sorts the list                                                                |
<--------------------------------------------------------------------------------------------------->

* List vs Array
---------------->

->       Lists                                  Array
1) Lists are hetrogenous.             1) Arrays are Homogenous.

2) Can store multiple data types      2) Stores elements of one data type only.
   (int, str, float, etc.).

3) Uses more memory.                  3) Uses less memory, especially NumPy arrays.

4) No import required.                4) array or numpy module required.

5) Supports indexing and slicing.     5) NumPy arrays support hundreds of math functions.

6) General-purpose                    6) Optimized for vectorized operations, matrix math.
(insert, append, delete, slicing).  

7) lst = [1, "hello", 3.5]            7) arr = np.array([1, 2, 3]) 

* Create
* Acess
* Edit
* Add
* Delete
* Operations
* Functions
List Length: To determine how many items a list has, use the len() function.
List items can be of any data type. Since lists are indexed, lists can have items with the same value
'''
# From Python's perspective, lists are defined as objects with the data type 'list':
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # O/P: <class 'list'>

# We can also crate list by using list() constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) # O/P: ['apple', 'banana', 'cherry']'''

# Create
# empty list 
a = []

# list with values
fruits = ["apple", "banana", "mango", "orange"]

# list with mixed data types
mixed = ["neha", 21, 5.4, True]

# Access List Elements
# positive index:    [0]      [1]        [2]     [3]
fruits =           ["apple", "banana", "mango", "orange"]
# negative index:    [0]      [-3]        [-2]     [-1]

print(fruits[0])   # apple  (positive indexing)
print(fruits[-1])  # orange (negative indexing)
# Slicing
print(fruits[1:3])   # o/p: ['banana', 'mango']
print(fruits[:2])    # o/p: ['apple', 'banana']
print(fruits[2:])    # o/p: ['mango', 'orange']  -----> how?

# Edit / Update Elements
fruits = ["apple", "banana", "mango"]
# For single item
fruits[1] = "kiwi"
print(fruits)   # o/p: ['apple', 'kiwi', 'mango']
# Update multiple items
fruits[0:2] = ["berry", "grapes"]
print(fruits)   # o/p: ['berry', 'grapes', 'mango']

# Add Elements:
a = [1, 2, 3]
# append()	Add at end
a.append(4)           #  o/p: [1, 2, 3, 4] 
# insert()	Add at specific index 
a.insert(1, 10)       #  o/p: [1, 10, 2, 3, 4]
# extend()	Add multiple items
a.extend([5, 6])      #  o/p: [1, 10, 2, 3, 4, 5, 6]

# Delete elements:
a = [1, 2, 3, 4]
# remove() Delete by value
print(a.remove(2))       #  o/p: [1, 3, 4] 
# pop() Delete by index (default last)
print(a.pop(1))          #  o/p: [1, 4]
# del keyword Delete by index or entire list
del a[0]          
print(a)                 #  o/p: [4]
# clear() Empty list
print(a.clear())         #  o/p: [] / None


# Operations on Lists
# Concatenation
a = [1, 2]
b = [3, 4]
print(a + b)     #  o/p: [1, 2, 3, 4]
# Repetition
print(a * 3)     #  o/p:  [1, 2, 1, 2, 1, 2]
# Membership
print(3 in [1, 2, 3])       #  o/p:  True
print(5 not in [1, 2, 3])   #  o/p:  True
# Iteration
for item in ["a", "b", "c"]:
    print(item)

# List Functions & Methods (Must Know)
a = [1,9,3,4,5,7,8,6,2]
print(len(a))    #  o/p: 9
print(min(a))    #  o/p: 1
print(max(a))    #  o/p: 9
print(sum(a))    #  o/p: 45
print(sorted(a)) #  o/p: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Common Methods
numbers = [3, 1, 9, 1]

numbers.sort()      # ascending
numbers.reverse()   # reverse list
numbers.count(1)    # count occurrences
numbers.index(9)    # position of value

# Copy List (Important!)
a = [1,2,3]
b = a.copy()

b.append(4)
print(a)  #  o/p: [1,2,3]
print(b)  #  o/p: [1,2,3,4]

# Nested Lists
matrix = [[1,2,3], [4,5,6], [7,8,9]]

print(matrix[1][2])   #  o/p:  6

# List Comprehension (Advanced but useful)
numbers = [1,2,3,4,5]
squares = [x*x for x in numbers]
print(squares)   #  o/p:  [1, 4, 9, 16, 25]
