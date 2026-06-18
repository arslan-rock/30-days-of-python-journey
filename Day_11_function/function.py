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

# Function with default parameters:


