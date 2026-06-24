# 12-06-26 I was not studying in the last two days because of not  feel better
# Tuples are immutable
# empty tuples
# first method
empty_tuple = tuple()

# second method
second_empt_tupl = ()

# tuple with inital values
fruits = ("mango", "orange", "papaya", "banana", "dragon fruit", "strawberry")
# fruits[0] = "kiwi" # gives typeerror tuple are immutable
print(fruits) 

# tuple length
print(len(fruits))

# accessing tuple items
# positive index
print(fruits[1])

# negative index
print(fruits[-1]) # gives the last item of the tuple

# slicing
# middle fruit
middle_index = len(fruits) // 2
middle_fruit = fruits[middle_index]
print(middle_fruit)

# slice out specific part
print(fruits[-3:-1])

# change tuple to list
cars = ("Ferrari", "BMW", "Honda", "Maruti", "Volkswagen")
new_cars = list(cars)
print(new_cars)

new_cars.append("Morris Garage")
print(new_cars)

# change list to tuple
again_new_cars = tuple(new_cars)
print(again_new_cars)

# chec an item in tuple
print("Maruti"in again_new_cars)
print("Mercedes" in again_new_cars)

# join tuples
companies = ("Apple", "Google", "Facebook")
new_companies = again_new_cars + companies
print(new_companies)

# delete tuples
del new_companies
print(new_companies) # gives NameEror because it completely destroyed 
