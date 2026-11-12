#FUNCTIONS IN PYTHON 

# 1)  Creating a Function

def greet():
    print("Hello world!")
greet()

# 2) Function With Parameters (Inputs) 

def welcome(name):
    print("Hello",name)
welcome("Deepak")

# 3) Function With Multiple Parameters 

def add(a,b):
    print("sum=",a+b)
add(5,3)

# 4) Function With Return Value 

def multiple(a,b):
    return a*b
result=multiple(5,4)
print("Answer=",result)

# 4) Default Parameters 

def hello(name="Guest"):
    print("Hello",name)
hello()
hello("Deepak")


# 5) Keyword Arguments 
def student(name,age):
    print(name,age)
student(name="aman",age=18)

# 6) Lambda (One-Line Function) 

square=lambda x:x*x
print(square(25))

add=lambda a,b:a+b
print(add(3,7))

sub=lambda a,b:a-b
print(sub(10,5))

multiply=lambda a,b:a*b
print(multiply(6,6))

division=lambda a,b:a/b
print(division(10,5))

# 7)Function Inside Function 

def outer():
    print("outer function")
def inner():
    print("Inner function")
outer()
inner()



#  8) Real-Life Style Examples 
#  A) Grade Calculator 

def grade(marks):
    if marks>=90:
        return "A Grade"
    elif marks>=75:
        return "B Grade"
    elif marks>=33:
        return "C Grade"
    else:
        return "Fall"

print(grade(90))

#  B) ATM Withdrawal Simulation 

def withdraw(balance,amount):
    if amount>balance:
        return "Incufficient balance"
    return balance-amount
print(withdraw(5000,1200))

# C) Login System 

def login(user,password):
    if user=="Admin" and password=="1234":
        return "Login Succesful"
    return "Invalid Details"
print(login("Admin","1234"))

