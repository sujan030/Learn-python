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

list1 = [ "apples", "banana", "peach", "cherry"]
new_list = [x for x in list1 if "a" in x]
print (list1)
print (new_list)

