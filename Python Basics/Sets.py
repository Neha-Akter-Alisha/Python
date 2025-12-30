'''
Set:
-> Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed. Sets are written with curly brackets.
-> Set items are unchangeable, but you can remove items and add new items.
-> Set items are unordered, unchangeable, and do not allow duplicate values.
-> Unordered means that the items in a set do not have a defined order.
   Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
-> Set items are unchangeable, meaning that we cannot change the items after the set has been created.
   (Once a set is created, you cannot change its items, but you can remove items and add new items)
-> Sets cannot have two items with the same value.
   (Note: 1) The values True and 1 are considered the same value in sets, and are treated as duplicates.
          2) The values False and 0 are considered the same value in sets, and are treated as duplicates.)
-> A set in Python is:

* Unordered
* Unindexed
* Mutable
* Does NOT allow duplicate values
* Stores only unique items
* Very fast for searching (because it uses hashing)

''' 
# 1) How to Create a Set

# Basic set
fruits = {"apple", "banana", "mango"}
print(fruits)


# Set automatically removes duplicates
x = {1, 2, 2, 3}
print(x)      # {1, 2, 3}


# Empty set (IMPORTANT!)
a = set()
# NOT this:
a = {}   # this is a dictionary, not a set 



# 2) Access Items in a Set. You cannot access using index because sets are unordered. But you can loop:
fruits = {"apple", "banana", "mango"}

for item in fruits:
    print(item)



# 3) Add Items to Set
# add()
fruits.add("orange")

#  update() — add multiple items
fruits.update(["papaya", "grapes"])

#  update() also works with tuples, lists, etc
fruits.update(("kiwi", "pear"))


#  4. Remove Items
# remove(): (Removes item — throws error if not found)
fruits.remove("banana")

#  discard(): (No error even if item not found)
fruits.discard("banana")

#  pop(): Removes a random item. Because set has no order.
fruits.pop()

#  clear() — removes all
fruits.clear()

#  del — delete set entirely
del fruits

# 5) Set Operations (VERY IMPORTANT). These are the main power of sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

#  Union (all unique items)
a | b
# or
a.union(b) # O/P: `{1, 2, 3, 4, 5, 6}`

#  Intersection (common items)
a & b
# or
a.intersection(b) # O/P: `{3, 4}`

#  Difference. Items belong to `a` but NOT `b`
a - b
# or
a.difference(b) # O/P: `{1, 2}`

#  Symmetric Difference. Items NOT common in both
a ^ b
# or
a.symmetric_difference(b) # O/P: `{1, 2, 5, 6}`

#  6) Set Comparison Operations
a = {1, 2, 3}
b = {1, 2}


#  issubset()
b.issubset(a)   # True

#  issuperset()
a.issuperset(b)  # True

#  isdisjoint(). No common elements
{1,2}.isdisjoint({3,4})   # True


# 7) Looping in Sets

#  Simple loop
for x in fruits:
    print(x)

#  Using enumerate() with manual index
for i, v in enumerate(fruits):
    print(i, v)

# 8) Set Comprehension (like list comprehension)
squares = {x*x for x in range(1, 6)}
print(squares) # O/P: `{1, 4, 9, 16, 25}` (But order can vary)

# 9) Convert List → Set (remove duplicates)
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)

# 10)
#  Copy Set
#  copy()
b = a.copy()

# 11) Frozen Set (Immutable Set). A `frozenset` cannot be changed.
fs = frozenset([1, 2, 3]) # You cannot add or remove anything from it.

'''
<--------------------------------------------------------------------------------------------------------------------------------------->
|Method	                 |        Shortcut	                 |                       Description                                        | 
|copy()	 	             |  Returns a shallow copy	         |                                                                          |
|difference()	         |          -		                 |          Returns a new frozenset with the difference	                    | 
|intersection()	         |          &		                 |          Returns a new frozenset with the intersection	                |
|isdisjoint()	 		 |                                   |          Returns whether two frozensets have an intersection	            |
|issubset()	             |        <= / <	 	             |          Returns True if this frozenset is a (proper) subset of another  |	
|issuperset()		     |        >= / >	                 |          Returns True if this frozenset is a (proper) superset of another|	
|symmetric_difference()	 |          ^	                     |          Returns a new frozenset with the symmetric differences	        |
|union()	             |          |	                     |          Returns a new frozenset containing the union	                |
<--------------------------------------------------------------------------------------------------------------------------------------->
'''

# 12) Built-in Functions for Sets
# (Works only if set contains numbers)
len(a)          # number of items
max(a)          # largest value
min(a)          # smallest value
sum(a)          # sum of values 


# 13) Joining Sets
#  update() — adds items of another set in place
a.update(b)

#  union() — returns new set
c = a.union(b)


# 14) Important Set Properties

'''
* No indexing
* No duplicates
* Fast lookup
* Order not fixed
* Mutable
* Elements must be immutable (tuple allowed, list NOT allowed)'''
valid_set = {(1,2), 3, "apple"}
invalid_set = {[1,2], 3}   # list is unhashable

# 15) Common Set Use Cases
'''
 Removing duplicates
 Checking membership
 Fast searching
 Mathematical set operations
 Finding unique items
 '''