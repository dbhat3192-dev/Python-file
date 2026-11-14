#LISTS, TUPLES & SETS IN PYTHON 
# 1) LISTS (Most Used Collection Type) 

mylist=[10,20,"Hello",3.5,True]
print(mylist[0])
print(mylist[-1])
print(mylist[1:4])
mylist[1]=50    #Add 50 Except 20
print(mylist)


list=[10,50,"Hello",True,1.9]
list.append(5)          #Add item at end 
list.insert(2,"hi")     #Add item at index
list.remove(1)          #removes first matching value
list.pop(1)             #Removes By Index
list.clear()            #Removes All Items
list.sort()             #sorts list
list.extend("5")        #joins lists 
new=list.copy()          #Copies list
print(list)

# 2) TUPLES (Fixed / Unchangeable Lists) 

mytuple=(10,20,30)
print(mytuple[0])  #print 10
print(mytuple[1])   #print 20
print(mytuple[1:3])   #print 20,30


fruits=("Apple","Banana","Cherry")
a,b,c=fruits
print(a)    #Apple


# 3) SETS (Unique, Unordered Collection) 

myset={10,20,30}  #Example

# Adding Items
myset={10,20,30}
myset.add(50)
myset.update([1,2,3])

#Removing Items
myset={10,20,30}
myset.remove(10)         #error if not found 
myset.discard(20)        # no error if not found 
myset.pop()              # removes random item 
myset.clear()             #Remove All Items
print(myset)

#Set Operations (Important) 
set1={1,2,3}
set2={4,5,6}
print(set2.union(set1))             #All Items
print(set1.intersection(set2))      #Common
print(set1.difference(set2))        # in set1 not i set2


# 4) Real-Life Style Examples 
#  A) Store student marks 
marks=[78,80,90,67]
print("Highest:",max(marks))
print("Highest:",min(marks))


#B) Store list of cities 
cities=["Delhi","Mumbai","Chennai"]
cities.append("Kolkata")
print(cities)


# C) Coordinates example (tuple)
location=(28.62,77.20)
print("Laditude:",location[0])


#D) Track unique visitors (set) 
visitors={"ram","shyam","ram"}
print(visitors)                   # Automatically Removes Duplicate



#Create a set of 5 numbers and add two more numbers. 
set={10,30,7,5,4}
set.add(50)
set.add(90)
print(set)



#Find the common elements between two sets. 
set1={1,2,3,}
set2={3,4,5}
print(set1.intersection(set2))