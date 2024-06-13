lis1 = [1,2,3,4]
lis2 = []
for x in lis1:
    lis2.append(x*x)

print(lis2) 

lis3 = [(lambda x:x**2)(x) for x in lis1]
print(lis3)