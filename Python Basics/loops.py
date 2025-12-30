"""
Python has two loops.
-> while loop
-> for loop 
-> Syntax of while loop:
while condition:
     code
Example:
"""
num = int(input("Enter your number: "))

i = 1
while i<5:
    print(num*i)
    i+=1

num = int(input("Enter your number: "))
i = 1
while i <= 10:
  print(num,"x",i,"=",num*i)
  i += 1

num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Number of digits:", count)


