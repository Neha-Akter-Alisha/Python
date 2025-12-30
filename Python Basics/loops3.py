# Nested loop using while loop 
# 1
num = int(input("Enter your number: "))
i = 1
while i<= num:
    j = 1
    while j<= i :
        print("*", end = "")
        j+=1
    print("")
    i+=1

# O/P:
# Enter your number: 4
# *
# **
# ***
# ****
#2
num = int((input("Enter your name: ")))
i = 1 
while i<= num:
    j = 1
    while j<=num:
        print("*", end = "")
        j+=1        
    print("")
    i+=1 

# O/P:
# Enter your name: 5
# *****
# *****
# *****
# *****
# *****

# 3
i = int(input("Enter your number: "))
while i >= 1:
    j = 1
    while j<= i :
        print("*", end = "")
        j += 1
    print()
    i-=1
# O/P:
# Enter your number: 5
# *****
# ****
# ***
# **
# *

#4
num = int(input("Enter your number: "))
i = 1
while i <= num:
    j = 1
    while j <= i:
        print(j, end = "")
        j+=1
    print()
    i+=1

# O/P:
# Enter your number: 5
# 1
# 12
# 123
# 1234
# 12345

    
# 5
num = int(input("Enter the number: "))
i = 1
while i<=num:
    j=1
    while j <= i:
        print(i, end = "")
        j+=1
    print()
    i+=1
# O/P:
# Enter the number: 5
# 1
# 22
# 333
# 4444
# 55555


#6
num = int(input("Enter your num: "))
i = 1
while i <= num:
    j = 1
    while j <= num:
        if i == 1 or i == num or j == 1 or j == num:
                print("*", end = " ")
        else:
                print(" ", end = " ")

        j+=1
    print()
    i+=1

# O/P:
# Enter your num: 5
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 

#7
num = int(input("Enter your number: "))
i = 1
while i <= num:
      j = num
      while j > i:
            print(" ", end = "")
            j-=1
      k = 1
      while k <= (2*i - 1):
            print("*", end = "")
            k+=1
      print()
      i+=1
 # O/P:
#  Enter your number: 4
#    *
#   ***
#  *****
# *******

#8
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

i = 1
while i <= cols:
    j = 1
    while j <= rows:
        print("*", end=" ")
        j += 1
    print()
    i += 1
# O/P:
# Enter number of rows: 4
# Enter number of columns: 4
# * * * * 
# * * * * 
# * * * * 
# * * * * 