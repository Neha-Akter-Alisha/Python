# Editing and Deleting in Strings
'''There is no editing in string. You can't edit a string but you can reassign it but you can't add a new charecter into a assigned strings.
Example: a[5] = 'W' # O/P: TypeError: 'str' object does not support item assignment
Strings are a Immutable Data Type''' 
a = 'Hello World'
a = 'World'
print(a)  # O/P: World 
# Same goes for deleting
# del c[0] # O/P: TypeError: 'str object does not support item deletion
# del c[:3:2] # O/P: TypeError: 'str' object does not support item deletion 
