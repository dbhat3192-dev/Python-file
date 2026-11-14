# DICTIONARIES IN PYTHON 

#  1) What Is a Dictionary? 
#  A dictionary is a collection of key : value pairs. 
#  Keys = unique 
#  Values = can be anything 

#Syntax

mydict={
    "name":"Aman",
    "age":18,
    "city":"Delhi"
} 
# print(mydict["name"])
# print(mydict["age"])
# print(mydict["city"])

# 2) Using get() 

print(mydict.get("age")) 
# If the key does not exist: 
# get() returns None instead of error.


#  3) Adding New Key–Value Pair 

mydict={
    "name":"Deepak",
    "age":18,
    "city":"Rajasthan"
} 
mydict["country"] = "India"   #ADD 
print(mydict)

# 4) Updating Value

{
    "name":"Aman",
    "age":18,
    "city":"Delhi"
} 
mydict["age"]=20   #Update 
print(mydict)

# 6) Dictionary Inside Dictionary (Nested Dict) 

student={
    "name":"Deepak",
    "marks":[90,95,99],
    "info":{
        "city":"Delhi",
        "class":"12th"
    }
}
print(student["info"]["city"])


#7) Useful Dictionary Functions 

dict={
    "name":"Aman",
    "age":18,
    "city":"Delhi"
}
#mydict.keys()
#mydict.values()
#mydict.items()
mydict.update({"age": 30}) 
print(dict)



#  8) Real-Life Style Examples 
#  A) Student Marksheet 

student = { 
    "name": "Ravi", 
    "math": 90, 
    "science": 85, 
    "english": 88 
} 
total = student["math"] + student["science"] + student["english"] 
print("Total =", total)

#B) Product Details 

product={
    "id":101,
    "name":"Laptop",
    "price":45000
}
print("price:",product["price"])


