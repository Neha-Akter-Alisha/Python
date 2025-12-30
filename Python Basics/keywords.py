"""
Keywords:
* Python is a case sensitivve programming language
In programming, a keyword is a word that is reserved by a program because the word has a special meaning.
Keywords can be commands or parameters. Every programming language has a set of keywords that cannot be used as variable as variable names.
"""
# python has 33 keywords
import keyword
print(keyword.kwlist)  # To print all the python keywords
# O/P:  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

"""
Identifiers:
A Python identifier is a name used to identify a variable,function,class,module or other object.
* Rules for setting Identifiers
-> Can only start with an alphabet or _
-> Followed by 0 or more letter, _ and digits
-> Keywords cannot be used as identifiers

"""
_ = "neha"
print(_)  # O/P: neha