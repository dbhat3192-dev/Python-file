#Operators in Python

#1 Arithmatic #Operator (Math Calculations) 

print(3+2) #Addition
print(3-2) #Subtraction
print(3*3)  #Multiply
print(3/3)  #division
print(3%3)  #modulus
print(3//3)  #floor division
print(3**3)  #exponent

#2 Comperition operator  (Check Conditions) 

a=20
b=20
print(a==b)  #Equal to
print(a!=b)  #Not Equal

a=7
b=3
print(a>b)  #Greater than
print(a<b)  #Less than

a=5
b=5
print(a>=b) #Greater or Equal
print(a<=b) #Less or Equal#

#3 Assignment Operator  (Store & Update Values) 

a = 5     # simple assignment 
a += 3    # a = a + 3 → 8 
a -= 2    # a = a - 2 → 6 
a *= 4    # a = a * 4 → 24 
a /= 4    # a = a / 4 
a %= 5    # a = a % 5 
a //= 5   # a = a // 5 
a **= 2   # a = a ** 2 
print(a)

#4 Logical Operators  (True/False)

age = 25 
print(age > 18 and age < 60) # True if both true  
print(age < 18 or age > 100) # True if any is true 
a=10
b=10
print (not a!=b) # Reverses result 


#6 Membership Operators 
#Used for checking if a value exists. 
name = "python" 
print("p" in name) # True 
print("z" not in name) # True

#  7 Identity Operators 
# Used to check if two variables refer to the same object. 

a = [1, 2, 3] 
b = a 
c = [1, 2, 3] 
print(a is b) # True (same memory) 
print(a is c) # False (same value, different memory) 
print(a is not c) # True
