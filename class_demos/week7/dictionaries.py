# Dictionaries are defined by key-value pairs

person1 = {
    "name": "Mark Ogg",
    "age" : 76,
    "job" : "purveyor of bad jokes"
}

person2 = {
    "name": "Lewis",
    "age" : 28,
    "job" : "guessing Mark's age wrong"
}

# Raw data
print(person1)

# Display content of dictionary:
for key_name in person1.keys():
    print(f"key: {key_name}, value: {person1[key_name]}")

# List of dictionaries
list_of_people = []
list_of_people.append(person1)
list_of_people.append(person2)
print(list_of_people)

for d in list_of_people:
    for k in d.keys():
        print(k, ": ", d[k])
        