"""
For loop iterate on either range or sequence.
* Range
range(stop) -> range object
range(start, stop[, step]) -> range object
step is used to give Gap between twon numbers. For example : o variables output.

* Sequence: A sequence of charecters
* String
* For loop Syntax:
for variable in iterable:
    # Code block to be executed in each iteration
    # This code must be indented

"""
# Range examples:

m = list(range(1,11)) # O/P: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
n = list(range(5)) # O/P: [0, 1, 2, 3, 4]
o = list(range(1,11,3)) # O/P: [1, 4, 7, 10] , here step is being used and the gap between two numbers are 3.

# Sequence example:
p = ["Kolkata", "Delhi", "Mumbai"] # O/P: ['Kolkata', 'Delhi', 'Mumbai']

print(m)
print(n)
print(o)
print(p)


# For loops examples are given below
# Range
for i in range (1,5):
    print(i)
# Sequencce
#1
for i in ["Kolkata","Delhi","Mumbai"]:
    print(i)

#2
for i in ["2","3","4"]:
    print(i)


