# A loop in a loop known as nested loop
# Nested loop using for loop
rows = int(input("Enter the number of rows: "))

for i in range (1,rows+1):
    for j in range(0,i):
        print("*",end = "")
    print("")

# O/P: 
# Enter the number of rows: 4
# *
# **
# ***
# ****

# Nested loop using while loop 
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
