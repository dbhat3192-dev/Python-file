# CONTROL FLOW & CONDITIONAL STATEMENTS 

#1 If ELSE Statement 
# Runs one block when condition is True, and another when condition is False,
age=int(input("Enter Age:"))
if age>=18:
    print("Eligible")
else:
    print("Not Eligible")



#2  If–Elif–Else 
# Used when we have multiple conditions.
marks=int(input("Enter Number:"))
if marks>=90:
    print("A Grade")
elif marks>=75:
    print("B Grade")
elif marks>=33:
    print("pass")
else:
    print("Fail")


#  Using len(), %, and > in Conditions 
#  Length Check 
name=input("Enter Name:")
if len(name)>4:
    print("Valid Name")
else:
    print("Too Short")



# Even/Odd Check 
num=int(input("Enter Name:"))
if num%2==0:
    print("Even")
else:
    print("Odd")


num=int(input("Enter Number:"))
if num//3==0:
    print("Odd")
else:
    print("Even")


#Nested If (if inside another if) 
age=int(input("Enter Age:"))
if age>=18:
    print("Adult")
    if age>=50:
        print("Senior Citizen")
    else:
        print("Working Age")
else:
    print("Minor")


# One-Line If Statement 
a= 10 
if a > 5: print("a is greater than 5") 

# One-Line If–Else (Ternary) 
num = 7 
result = "Even" if num % 2 == 0 else "Odd" 
print(result)


#Using Conditions With Operators 
a=int(input("Enter Number:"))
if a%3==0 and a%5==0:
    print("Division By Both 3 and 5")
if a%3==0:
    print("Division By 3")
if a%5==0:
    print("Division By 5")
else:
    print("Not Division")



# Real-Life Style Examples 
#  A) Basic Login Check 
username=input("Enter Username:")
password=input("Enter Password:")
if username=="Admin" and password=="1234":
    print("Succesful Login")
else:
    print("Invalid Login")


# B) Tempreture Message
temp=float(input("Enter Tempreture:"))
if temp>30:
    print("Hot Weather")
elif temp>20:
    print("Normal Weather")
else:
    print("Cold Weather")


# c) Check Votin Eligibility
age=int(input("Age:"))
if age>18:
    print("Eligible")
else:
    print("Not Eligible")


# D) Number Comparision
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
if a>b:
    print("A is Larger")
elif b>a:
    print("B is Larger")
else:
    print("Both are equal")

# E) Percentage Check
num=int(input("Enter Marks:"))
if num>=90:
    print("A Grade")
elif num>=75:
    print("B Grade")
elif num>=33:
    print("C Grade")
else:
    print("Fail")