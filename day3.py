# #while loop
# a = 1
# while a < 10:
#     print(a)
#     a = a + 1
# else:
#     print("done")

# #guess the  number 

# import random
# number = random.randint(1,10)
# guess = 0
# count = 0
# while count<3 :
#     guess = int(input("guess the number: "))
#     count = count + 1
#     if guess < number:
#         print("too low")
#         continue
#     elif guess > number:
#         print("too high")
#         continue
#     else:
#         print("you guessed it")
#         break

# #for loop
list1 = [1,2,3,6,7,8,9]
for i in list1 :
    if i % 2 != 0 :
        print(i)


