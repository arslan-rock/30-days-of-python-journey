# # # # # # 15-June-2026
# # # # # # # 💻 Exercises: Day 9
# # # # # # Exercises: Level 1
# # # # #1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age: "))

if age >= 18:
     print("You are old enough to drive.")

else : 
     diff = 18 - age

     if diff == 1:
          print(f"Wait for the next {diff} year.")
        
     else :
          print(f"Wait for the next {diff} years.")

# # # #2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))

if my_age > your_age :
    diff = my_age - your_age 

    if diff == 1: 
        print(f"I'm {my_age - your_age} year older than you.")
    
    else :
        print(f"I'm {my_age - your_age} years older than you.")

elif your_age > my_age : 
    diff = your_age - my_age 

    if diff == 1 :
        print(f"You're {your_age - my_age} year older than me.")
    
    else :
        print(f"You're {your_age - my_age} years older than me.")

else : 
    print("We are equal.")

# # #3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if a > b: 
    print("a is greater than b")

elif b > a: 
    print("b is greater than a")

else:
    print("both are equal.")

# # # # Exercises: Level 2
# # 1. Write a code which gives grade to students according to theirs scores:
marks = int(input("What is your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade 🅰️.")

elif marks >= 70 and marks <= 89:
    print("Grade 🅱️.")

elif marks >= 40 and marks <= 69:
    print("Grade 🅲.")

else: 
     print("Fail.")

# # #2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter you favourite month: ").title()

if month == "September" or month == "October" or month == "November" :
    print("Autumn Season.")

elif month == "December" or month == "January" or month == "February" :
    print("Winter Season.")

elif month == "March" or month == "April" or month == "May" :
    print("Spring Season.")

elif month == "June" or month == "July" or month == "August" :
    print("Summer Season.")

else : 
    print("Invalid input.")

# # # 3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
check = input("Enter favourite fruits: ").lower()

if check not in fruits:
    fruits.append(check)
    print(fruits)

else:
    print("fruit exist in the list")

# # Exercises: Level 3
# # Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ["JavaScript", "React", "Node", "MongoDB", "Python"],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# #  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if "skills" in person:
    middle_index = len(person["skills"]) // 2
    middle_skill = person["skills"][middle_index]
    print(middle_skill)

else:
    print("No skill in it.")


# # #  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if "JavaScript" in person["skills"] and "React" in person["skills"] and len(person["skills"]) == 2:
    print("Frontend developer.")

elif "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"] and len(person["skills"]) == 3:
    print("Backend developer.")

elif "JavaScript" in person["skills"] and "React" in person["skills"] and "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"] and len(person["skills"]) == 5:
    print("Fullstack developer")

else: 
    print("Invalid role.")

# # * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
    if "Python" in person['skills']:
        print("Person has python skills.")
    
    else: 
        print("Person has only skills.")

else:
    print("Person has no skills.")

# #  * If the person is married and if he lives in Finland, print the information in the following format:
if person["is_married"] and person["country"]:
    print(f"Asabeneh Yetayeh lives in {person['country']} and he is married.")

else: 
    print(f"Person is not lives in finland and he's single.")