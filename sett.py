set1 = {'a','b','c','d','a'}
print(set1)
print(type(set1))
set2 = set(('abb','bba','cdd'))

print(set2)
for x in set2:
    print(x)
    print(type(x))
if "abb" in set2:
    print("yes")
set1.add("abba")
print(set1)
set2.update(set1)
print(set2)
set2.remove("a")
print(set2)
#union
set3 = {'a','b','c','d',1,2}
set4 = {1,2,3,4,'a',"b"}
set5 = set3.union(set4)
print(set5)
#intersection
set6 = set3.intersection(set4)
print(set6)
#difference
set7 = set3.difference(set4)

print(set7)
set8 = set3.symmetric_difference(set4)
print(set8)
set3.difference_update(set4)
print(set3)