#there should be odd num in odd index and even number in even index
def balanced(list1):
    for i in range(len(list1)):
        if i % 2 == 0:
            if list1[i] % 2 != 0:
                return False
        else:
            if list1[i] % 2 == 0:
                return False
    return True
list1 = [2,3,4,5,6]
if balanced(list1):
    print("balanced")
else:
    print("not balanced")

