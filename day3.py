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
# list1 = [1,2,3,6,7,8,9]
# for i in list1 :
#     if i % 2 != 0 :
#         print(i)

# for x in range(1,10):
#     print(x)

# fibonnacci series
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(1,10):
#      c = a + b
#      print(c)
#      a = b
#      b = c

#arbitary argument
def subject(*sub):
    print(sub)
fab = ["history","socioscience","python"]
subject(fab,"science","hindi")
def name(**nam):
  
     print(nam['first_name'])
name(first_name="sujan",last_name="simkhada")