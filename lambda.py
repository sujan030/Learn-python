#lambda function use and benifits

#normal function
def add(a,b):
    return a+b
print(add(10,20))

#lambda function

add = lambda a,b:a+b
print(add(10,20))

#function inside function

def add(a,b):
    return lambda a,b:a+b
x = add(10,20)
print(x)
#a function cannot returun a function defined in def

# def add(a,b):
#     def sub(a,b):
#         return a-b
#     
# x = add(10,20)
# print(x)

