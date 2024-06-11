dict1 = {
    "name": "sujan",
    "age": 20,
    "city": "kathmandu",
    "pincode": 44600,
    "email": "sujan.simkhada",
    "phone": 9876543210,
    "gender": "male",
    "hobbies": ["cricket", "football", "badminton"],
    "skills": ["python", "java", "c++"],
    "address": {
        "house_no": 123,
        "road_no": 456,
        "city": "kathmandu",
        "pincode": 44600}
}
for x in dict1.values():
    print(x)

for x in dict1.items():
    print(x)

for x in dict1["address"].items():
    print(x)

key1 = dict1.keys()
print(key1)

dict1.update({"age" : 22})
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

