# 18-06-2026
# Function 
# syntax
# # Declaring a function
# def function_name():
#     codes
#     codes
# # Calling a function
# function_name()

# Function without Parameters
def spiderman_movie():
    first_movie = "Spider Man : Homecoming"
    last_movie = "Spider Man : Brand New Day"
    complete_list = first_movie + " " + last_movie
    print(f"Spider-Man first movie =  {first_movie}, & Spider-Man last movie = {last_movie}")

spiderman_movie()

# def divide_two_num():
#     first_num = 18
#     second_num = 2
#     divide_num = first_num // 2
#     print(f"first num divide by second num = {divide_num}")

# x = divide_two_num()
# print(x)
# above programs python give None for no return statement

# Return statement 
def divide_two_num():
    first_num = 18
    second_num = 2
    divide_num = first_num // 2
    return divide_num

print(divide_two_num())

# function with parameter
# single parameter
  # syntax
#   # Declaring a function
#   def function_name(parameter):
#     codes
#     codes
#   # Calling function
#   print(function_name(argument))

def greeting(name):
    message = "Hello everyone, I'm " + name + " Rock."
    return message

print(greeting("Arslan"))

def sum_numbers(n):
    tracker = 0
    for i in range(n+1):
        tracker += i
    return tracker

print(sum_numbers(12))

# two parameter
def person_detail(name, age):
    line = "My name is " + name + " and my age is " + str(age)
    return line

print(person_detail("Arslan", 23))

def calculate_percent(marks_obtain, total_marks):
    percentage = (marks_obtain / total_marks) * 100
    return percentage

print(calculate_percent(45, 50))

#Passing Arguments with Key and Value
# If we pass the arguments with key and value, the order of the arguments does not matter.
def my_fav_place(country, city):
    sentence = "I want to visit " + city + " which is located in " + country
    return sentence

print(my_fav_place(country= "Saudi Arabia", city= "Mecca"))

# # Function Returning a Value - Part 2
# If we do not return a value with a function, then our function is returning None by default. To return a value with a function we use the keyword return followed by the variable we are returning. We can return any kind of data types from a function.
# Returning a string: Example:

def fifa_stars(star_1, star_2):
    player_1 = star_1.title() + " is famous for his nickname CR7"
    player_2 = star_2.title() + " is the most loving football player in our country."
    full_honour = player_1 + " and " + player_2
    return full_honour

print(fifa_stars(star_2= "lionel messi", star_1="ronaldo"))

# # Returning a number: Example:
def multiply(num_1, num_2):
    multiplication = num_1 * num_2
    return multiplication

print(multiply(num_1= 5, num_2= 9))

# Returning a boolean: Example:
def even(n):
    if n % 2 == 0:
        return True
    return False

print(even(4))
print(even(3))

# returning  a list
def check_even(h):
    even = []
    for i in range(h+1):
        if i % 2 == 0:
            even.append(i)
    return even

print(check_even(10))    

# # Function with default parameters:
# Sometimes we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling the function, their default values will be used.
# syntax
# # Declaring a function
# def function_name(param = value):
#     codes
#     codes
# # Calling function
# function_name()
# function_name(arg)
def welcome(name = "Arslan", prog_lang = "Python"):
    sentence_2 = "Hey " + name + " Welcome to " + prog_lang + " programming language."
    return sentence_2

print(welcome()) # Default
print(welcome("Anas", "Java")) 

def weight_of_object(mass, gravity = 9.81):
    weight = mass * gravity
    return f"Weight of object is {weight} N"

print(weight_of_object(100)) # 9.81 for average gravity on earth surface
print(f"Weight of object on moon surface: {weight_of_object(100, 1.62)}") # 1.62 gravity on moon surface

# Arbitrary Number of Arguments
# If we don't know the no. of argumet so we just placed *args before the argument so it can take bunch of arguments
def uefa(*team):
    sentence_3 = "".join(team) + " are UEFA teams" 
    return sentence_3

print(uefa("AS Monaco, ", "Arsenal, ", " Atalanta, ", "Athletic Club"))

# Default and # Arbitrary Number of Arguments
def ipl(*team, touranment):
    print(touranment + " teams :")
    for i in team:
        print(i)
    return team

print(ipl("RCB", "CSK", "KKR", "GT", "MI", touranment="IPL"))

# Dictionary unpacking
# Dictionary unpacking (**) takes key-value pairs from a dictionary and passes them as keyword arguments to a function.
def greet(name, location):
    new_sentence = "Hey, there my name is " + name + " and I live in " + location
    return new_sentence

details = {
    "name" : "Arslan",
    "location" : "India"
}

print(greet(**details))

# but if key not match it raise an error so your key must be match with parameter and value can be anything

# Arbitrary Number of Named Arguments
# You can also define a function to accept an arbitrary number of named arguments.
def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)
    
    return args

employee = {
    "name" : "Arslan",
    "Age" : 23,
    "City" : "India"
}

print(arbitrary_named_args(**employee))

# Function as a Parameter of Another Function
def square_num(n):
    return n * n

def do_something(f, x):
    return f(x)

print(do_something(square_num, 9))
