#OBJECT-ORIENTED PROGRAMMING (OOP) 

# 1) What Is a Class? 

class student:
    name="Aman"
    age:20
s1=student()
print(s1.name)

# 2) Methods in a Class 
class student():
    def greet(self):
        print("Hello Student")
s=student()
s.greet()

# # 3) What Is self?  
# self represents the current object. 
# You must write self inside methods. 
# Example: 
def greet(self): 
    print("Hello") 

# 4) Constructor (init) 
class students:
    def __init__(self):
        print("New Object Created!")
s=student()

# 5) Constructor With Parameters 

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=student("Aman",85)
print(s1.name,s1.marks)

# 6) Method That Uses Attributes 
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
s=student("Riya",90)
s.display()

# 7) Real-Life Style Examples 
#  Example A — Bank Account 

class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
    def show(self):
        print("Name:",self.name)
        print("Balance:",self.balance)
acc=Bank("Deepak",10000)
acc.deposite(5000)
acc.show()

#Example B — Car Object 
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def info(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
c=Car("BMW","X5")
c.info()

# Example C — Login System 
class user:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def login(self,u,p):
        if u==self.username and p==self.password:
            print("Login succesful")
        else:
            print("Invalid")
obj=user("admin","1234")
obj.login("admin","1234")
