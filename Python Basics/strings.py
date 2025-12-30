"""
String is a sequence of charecters
In python specifucally, string are a sequence of Unicode Charecters
* Creating strings
* Accessing strings
* Adding Chars to strings
* Edditing strings
* Deleting strings
* Operation strings
* String Functions

"""

# Creating String
# When we make application programm for user we can use  
print('Hello')      # o/p: Hello
print("Hello")      # o/p: Hello
print('''Hello''')  # o/p: Hello # multiline Strings
print("""Hello""")  # o/p: Hello # multiline Strings
c = str("Hello")
print(c)            # o/p: Hello

# Accessing Substring from a String
# Concept of Indexing 
# H E L L O 
# 0 1 2 3 4
c = "Hello"
print(c[0], c[1], c[2], c[3], c[4]) # Positive Indexing # O/P: H e l l o """
# Types of Indexing 
# -> Positive Indexing   # H E L L O 
                         # 0 1 2 3 4
# -> Negative Indexing   # H  E  L  L  O 
                         # 0 -4 -3 -2 -1
c = "Hello"
print(c[0], c[-1], c[-2], c[-3], c[-4]) # Negative Indexing  # O/P : H o l l e
