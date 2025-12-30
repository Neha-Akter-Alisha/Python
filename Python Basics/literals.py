"""
Literals 
* Literals is a raw data given in a variable. In Python, there are various types of literals they are as follows:
-> Numeric Literals
-> String Literals
-> Boolean Literals 
-> Special Literals

"""
# Numeric Literals
a = 0b1010 # Binary literal
b = 100    # Decimal literal
c = 0o310  # Octal literal
d = 0x12c  # Hexadecimal literal

# Float Literals
float_1 = 10.31
float_2 = 1.5e2
float_3 = 1.5e-3

# Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2, float_3)
print(x, x.imag, x.real)


# String Literals
string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code"""
unicode = u"\U0001f600\U0001F606\U0001F923" # O/P: 😀😆🤣
raw_str = r"raw \n string"
print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# Boolean Literal
a = True + 4 
b = False + 10

print("a:",a)
print("b:",b)

# Special Literal
a = None
print(a)