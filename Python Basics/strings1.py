# Slicing string : You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Note: The first character has index 0.
b = "Hello, World!"

# Get the characters from position 0 and position 12
print(b[0:13])   # O/P: Hello, World!

# Get the characters from position 2 to position 5 (not included):
print(b[2:5])    # O/P: llo

# Get the characters from the start to position 5 (not included):
print(b[:5])     # O/P: Hello

# Get the characters from position 2, and all the way to the end:
print(b[2:])     # O/P: llo, World!

# Get the characters: From: "o" in "World!" (position -5). To: but not included: "d" in "World!" (position -2):
print(b[-5:-2])  # O/P: orl

# Get the characters from position 2 and position 6 by skipping steps 2
print(b[2:6:2])  # O/P: lo

# Get the characters from position 0 and position 6 by skipping steps -1
print(b[0:6:-1])  # O/P: nothing as u can't take steps negative with positive indexing

# Get the characters from position -5 and position -1 by skipping steps 2
print(b[-5:-1:2])  # O/P: ol

# Get the string in reverse position
print(b[::-1])  # O/P: !dlroW ,olleH

# Get the characters from position -1 and position -5 by skipping steps -1
print(b[-1:-5:-2])  # O/P: ol