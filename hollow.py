def hollow(list1):
    f0 = -1
    l0 = -1
    for i in range(len(list1)):
       if list1[i] == 0:
        if f0 == -1:
         f0 = i
        l0 = i
    
    if (l0 - f0 + 1) < 3:
        return False
    else:
        bef = f0
        aft = len(list1) - l0 -1
        if bef == aft  == (l0 - f0 +1) :
            return True
        else:
            return False
list1 = [1,2,3,0,0,0,6,4,5]
if hollow(list1):
    print("hollow")
else:
    print("not hollow")
