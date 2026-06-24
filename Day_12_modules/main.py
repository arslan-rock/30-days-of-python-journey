# Importing a Module
# To import the file we use the import keyword and the name of the file only.
# import my_module

# print(my_module.generate(first_name= "Arslan", last_name= "Gaur"))

# Import Functions from a Module
# We can have many functions in a file and we can import all the functions differently.
# from my_module import generate, sum_two_nums, person, gravity
# print(generate(first_name= "Arslan", last_name="Gaur"))
# print(sum_two_nums(1, 3))
# print(person["first_name"])
# mass = 100 
# weight = mass * gravity
# print(weight)

# Import Functions from a Module and Renaming
# During importing we can rename the name of the module.
from my_module import generate as full_name, sum_two_nums as add_nums, person as p, gravity as g
print(full_name(first_name="Arslan", last_name="Gaur"))
print(add_nums(4,9))
print(p["first_name"])
mass = 90 
weight = mass * g
print(f"{weight:.2f}")

"""Import Built-in Modules
Like other programming languages we can also import modules by importing the file/function using the key word import. Let's import the common module we will use most of the time. Some of the common built-in modules: math, datetime, os,sys, random, statistics, collections, json"""

"""OS Module
Using python os module it is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating, changing current working directory, and removing a directory (folder), fetching its contents, changing and identifying the current directory."""
# # import the module
# import os
# # Creating a directory
# os.mkdir('directory_name')
# # Changing the current directory
# os.chdir('path')
# # Getting current working directory
# os.getcwd()
# # Removing directory
# os.rmdir()

