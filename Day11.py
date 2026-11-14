# OOP PART 2: 
#  INHERITANCE, POLYMORPHISM, ENCAPSULATION, 
# ABSTRACTION 

# 1) INHERITANCE (Reusing Code)
class parent:
    def show(self):
        print("Parent Function")
class child(parent):
    pass
obj=child()
obj.show()

# 2) super() — Call Parent Class Methods/Constructor

class A:
    def __init__(self):
        print("Parent Control")
class B(A):
    def __init__(self):
        super().__init__()
        print("Child COntruction")
b=B()

# 3) METHOD OVERRIDING (Important) 
class A:
    def show(self):
        print("Parent show")
class B(A):
    def show(self):
        print("Child Show")
b=B()
b.show()

# 4) POLYMORPHISM (Many Forms) 

class Dog:
    def sound(self):
        print("Bark")
class Cat(Dog):
    def sound(self):
        print("Meow")
for animal in (Dog(),Cat()):
    animal.sound()

# 5) ENCAPSULATION (Protecting Data) 
#  Public 
# # normal 
# self.name = "Aman" 
# #  Protected ( _ ) 
# self._marks = 90 
# #  Private ( __ ) 
# self.__password = "1234" 
# Private variables cannot be accessed directly. 

 #6) @classmethod 

class Employee:
    company="google"
    @classmethod
    def change_company(cls,new):
        cls.company=new
Employee.change_company("Microsoft")

# 7) @staticmethod 

class Math:
    @staticmethod
    def add(a,b):
        return a+b
print(Math.add(5,3))

#  Real-Life Style Examples 
#  A) User Login System with Encapsulation

class user:
    def __init__(self,user,password):
        self.user=user
        self.__password=password
    def login(self,p):
        if p==self.__password:
            print("Access Granted")
        else:
            print("Wrong Passwrod")
u=user("admin","1234")
u.login("1234")

#  B) Inheritance Example (Bank Accounts) 
class Bank: 
    def deposit(self): 
        print("Deposit Money") 
class SavingAccount(Bank): 
    def interest(self): 
        print("Interest Added") 

# C) Polymorphism Example (Shapes) 
class shape:
    def area(self):
        pass
class square(shape):
    def area(self):
        print(5*5)
class circle(shape):
    def area(self):
        print(3.14*4*4)
shapelist=[square(),circle()]
for s in shapelist:
    s.area()