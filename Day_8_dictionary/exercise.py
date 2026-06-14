# Exercises: Day 8
#1. Create an empty dictionary called dog
dog = {}

#2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "Leo", 
    "color": "White", 
    "breed": "Golden Retriever", 
    "legs": 4, 
    "age": 6
}

#3. Create a student dictionary
student = {
    "first_name": "Arslan",
    "last_name": "Gaur", 
    "gender": "Male", 
    "age": 23, 
    "marital_status": "Single",  # Fixed: Added underscore
    "skills": ["Communication", "Python Programming", "Web technology", "CS Fundamentals"],
    "country": "India", 
    "city": "Roorkee", 
    "address": {
        "pincode": 247667, 
        "area": "Satti Street"
    }
}

#4 Get length of student dictionary
print("Length:", len(student))

#5 Get the value of skills and check the data type
print("Skills Type:", type(student["skills"]))

#6 Modify the skills values by adding one or two skills
student["skills"].append("Hindi")
student["skills"].append("Tamil")

#7 Get the dictionary keys as a list
keys_list = list(student.keys())

#8 Get the dictionary values as a list
values_list = list(student.values())

#9 Change the dictionary to a list of tuples using items() method
# (Kept commented out so #10 doesn't break!)
# student_tuples = list(student.items()) 

#10 Delete one of the items in the dictionary
student.pop("city")
print("After Pop:", student)

#11 Delete one of the dictionaries 
# del student
# print(student)  # comment out it gives NameError it means this dictionary not present.
# so carefully use this method it completely destroyed dictionary