# #more on list,tuples and dictionary
# list1 = [ "ram", "hari", "gita", "sita"]
# print (list1)
# list1.insert(2,"ramcharan")
# print (list1)
# list2 = ["apples", "banana", "peach", "cherry"]
# print (list2)
# list1.extend(list2)
# print (list1)
# #removing items
# list1.remove("ramcharan")
# print (list1)
# list1.pop(5)
# print (list1)

#list comprehension

# list1 = [ "apples", "banana", "peach", "cherry"]
# new_list = [x for x in list1 if "a" in x]
# print (list1)
# print (new_list)
# list1.sort()

# print (list1)

# list1.reverse()
# print (list1)
# list1.sort(reverse=True)
# print (list1)

# list3 = list1.copy()
# print(list3)

# #tupple
# tuple1 = ("a","b","c","d","e","f","g","h","i",)
# print (tuple1)
# list1 = list(tuple1)
# list1.remove("a")
# tuple1 = tuple(list1)
# print (tuple1)

#unpack tuple

tup5 = ("ram", "hari", "shyam")
a,b,c = tup5
print (a,b,c)
a,*b = tup5
print (a)
print (b)