# 14-06-2026
# Dictionary
# Empty dictionary
empty_dict = {}
print(empty_dict)

person = {
    "first_name" : "Arslan",
    "last_name" : "Gaur", 
    "DOB" : "23-Aug-2002",
    "is_married" : "False",
    "skills" : ["English", "Python", "JS", "Web Development"],
    "address" : {
        "pincode" : 247667,
        "city" : "Roorkee"
    }
}

print(person)

# find length of dictionary
print(len(person))

# access dictionary items
print(person["skills"]) # dict["key"]

# if we find a key that we don't have it raises some error to overcome we use .get()
# print(person["qualification"]) #KeyError

# with .get()
print(person.get("is_book_lover")) # None 
print(person.get("first_name"))

# adding new key and value pairs
person["qualification"] = ["10th", "12th", "B.Sc(Computer Science)"]
print(person)

person["skills"].append("HTml")
print(person)

# Modifying Items in a Dictionary
person["first_name"] = "Ali"
print(person)

# checkk keys in dictionary
print("last_name" in person) # True because last_name key present in person dictionary

"""Removing Key and Value Pairs from a Dictionary
pop(key): removes the item with the specified key name:
popitem(): removes the last item
del: removes an item with specified key name"""

person.pop("is_married")
print(person)

person.popitem() # remove the complete last key with value
print(person) 

# del person["DOB"]
# print(person)

# change dict to list
person = person.items()
print(person)

# copy 
person_copy = person.copy()
print(person_copy)

# get dictionary key and values as a list
print(person.keys())
print(person.values())

# clear just clear out item don't delete dictionary
person.clear()
print(person)
print(person_copy)

del person
print(person)