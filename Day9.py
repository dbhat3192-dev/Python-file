# FILE HANDLING IN PYTHON

#1) Opening a File 

open("filename","mode")

# 2) Reading Files 
# A) read() → reads whole file 

file=open("data.txt","r")
content=file.read()
print(content)
file.close()

# B) read(n) → read first n characters 
file=open("data.txt","r")
print(file.read(10))
file.close() 


# C) readline() → read one line 
file = open("data.txt", "r") 
print(file.readline()) 
file.close() 


# D) readlines() → returns list of lines 
file = open("data.txt", "r") 
lines = file.readlines() 
print(lines) 
file.close() 


# 3) Writing to Files 
#  A) write() (creates OR replaces) 

file=open("data.txt","w")
file.write("this is my first line.\n")
file.write("Hello Python!")
file.close()

file=open("requrement.txt","w")
file.write("My name is deepak")
file.write("\n This is my second line")
file.close()

# B) Append Mode ("a") — add data without deleting old data 
file=open("data.txt","a")
file.write("\n New Line Added.")
file.close()

# 4) Using with open() (No Need to Close) 

with open("requrement.txt","r") as f:
    data=f.read()
    print(data)

# 5) Writing Binary Files (Images, PDFs, Keys)

file=open("image.jpg","w")

with open("image.jpg","rb") as f:
    data=f.read()

# 6) Checking If File Exists 
import os
if os.path.exists("dat.txt"):
    print("File Found")
else:
    print("File not found")

# 7) Deleting Files 
import os
os.remove("data.txt")

# 8) Real-Life Style Examples 
#  A) Save User Logs 

with open("log.txt","a") as log:
    log.write("user logged in \n")

# B) Save Student Marks in a File 
name=input("name:")
marks=input("marks:")
with open("students.txt","a")as f:
    f.write(f"Name:{name}\n Marks:{marks}\n")

# C) Read Configuration Data 
with open("students.txt")as f:
    for line in f:
        print("config:",line.strip())

# D) Copy File Content 
with open("data.txt")as f1:
    data=f1.read()
with open("students.txt","w")as f2:
    f2.write(data)

