#day 2
#string
a = "ram"
b = '   sita is good girl'
c = '''hari'''
#string indexing
print(a[0])
print(a[-3:-1])#negative indexing
print(a[0:2])#from 0 to less than 2 
print(a[-3:])
for i in a:
    print(i)
print(type(a))
print(b.strip())
print(b)
print(b.split())
print(a + "," + c + "," + b.strip()) 

#string format
age = 23
str1 = f"I am {age} years old"
print(str1)

#Exercise for reversing the string 

def revstring(stri):
   z = stri.split()
   for i in range(len(z),0): 
     rev = " ".join(z[i])

   return rev
    

     
 
print(revstring("asian college"))    
anagram
def anagram(stra,strb):
    stra = stra.replace(" ","").lower()
    strb = strb.replace(" ","").lower()
    if sorted(stra) == sorted(strb):
        return True
    else:
        return False
 

print(anagram("abc xyz","bcaxyz"))

#bool
x = 1
print(bool(x))
print(isinstance(x,int))
