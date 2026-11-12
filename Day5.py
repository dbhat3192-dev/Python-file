#LOOPS IN PYTHON 

#1) for Loop (Most Used Loop) 
for i in range(5):
    print("Hello World!")

# 2) Print a Multiplication Table
num=int(input("Enter Number:"))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")


#3) break → Stop the loop completely 
for i in range(1,10):
    if i==5:
        break
    print(i)        

# 4) Continue → Skip one loop cycle 
for i in range(1,11):
    if i==6:
        continue
    print(i)

# 5) pass → Do nothing (placeholder) 
for i in range(5): 
    pass 
#Used when you want to write code later. 


# 6) While Loop
i=1
while i<=5:
    print(i)
    i+=1

# 7) Infinit Loop
i=1
while i<=5:
    print("Hello World!")

# 8) Loop With Else
for i in range(5):
    print(i)
else:
    print("Loop Complete")

# Real-Life Style Examples 
#  A) Sum of First 10 Numbers 
total=0
for i in range(1,11):
    total+=i
print("Sum=",total)

# B) Count Even & Odd Number

even=0
odd=0
for i in range(1,21):
    if i%2==0:
        even+=1
    else:
        odd+1
print("Even:",even)
print("Odd:",odd)


# C) Password Retry System 
password="hello123"
for i in range(3):
    user=input("Enter Username:")
    if user==password:
        print("Access Granted")
        break
    else:
        print("Account Locked")


# D) Countdown program
i=10
while i>0:
    print(i)
    i-=1
    print("Time Up!")


#Print numbers 1 to 50. 
for i in range(1,51):
    print(i)

    
# Take input from user and print table in range 1 to 100.
num=int(input("Enter Number:"))
for i in range(1,101):
    print(f"{num} x {i} = {num*i}")

