# #  Exercises: Day 6
# Exercises: Level 1
#1. Create an empty tuple
empty_tuple = ()
print(empty_tuple)

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Saifullah", "Ahmed", "Muneeb")
sisters = ("Foziya", "Aliya", "Zaineb")

# 3 Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# 4 How many siblings do you have?
print(len(siblings))

# 5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_list = list(siblings) 
family_members = ["Abid", "Fatima"]
family_members.extend(family_list)
family_members = tuple(family_members)
print(family_members)

# Exercises: Level 2
# 1. Unpack siblings and parents from family_members 
father, mother, *my_siblings = family_members
parents = (father, mother)
my_siblings = tuple(my_siblings)

print(parents)
print(my_siblings)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("avocado", "strawberry", "litchi")
vegetables = ("cauliflower", "carrot", "onion")
animals = ("lion", "rat", "leopard")

food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_tp) // 2
middle_food_item = food_stuff_tp[middle_index]
print(middle_food_item)

#5. Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-3:]
print(first_three)
print(last_three)

#6. Delete the food_stuff_tp tuple completely
del food_stuff_tp
# print(food_stuff_tp) # it shoows NameError it means it completely deleted or destroyed

# #7 . Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country

# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("estonia" in nordic_countries)
print("Iceland" in nordic_countries)