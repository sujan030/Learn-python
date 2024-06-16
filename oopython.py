class dog:
    breed = "labrador"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print("woof woof")
        print(self.name)
        print(self.age)

dog1 = dog("nima",22)
dog1.bark()
print(dog1.name)