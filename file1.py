f = open("read.txt",'r')
print(f.read())

print(f.read(5))
print(f.readline())
f.close()
 
# import os
# os.remove("read.txt")

#with read in python

with open("read.txt",'r') as f: #the file closes after indentation  
    data = f.read()
print(data)