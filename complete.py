#is the list even 
#is there all the number between minimum and maximum

def is_complete(list):
    if len(list) % 2 == 0:
        minimum = min(list)
        maximum = max(list)
        if minimum != maximum:
            return False
        required = set(range(minimum, maximum))
        return required.issubset(list)
    else:
        return False
list1 = [1,2,9,10,3,4,5,6,7,8]
if is_complete(list1):
    print("list is even")
else:
    print("list is not even")