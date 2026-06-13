# 13-Jun-2026
# Set : Set is a collection of unique unordered and un-indexed distinct elements
# empty set
game_set = set()
print(type(game_set))

# set with inital values
games = {"god of war", "gta 5", "amazing spiderman", "clash of clans", "pub g"}

# find the length or count no of games using len() method
print(f"There are no. of {len(games)} games.")

# accessing values as per specific index in set use loops we will se later 
# check an item 
print(f"Amazing spiderman is in list or not: ", "amazing spiderman" in games)

# add item
games.add("tekken 7")
print(games)

# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
games.update(["gta6", "avatar", "call of duty"])
print(games)

# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
games.remove("clash of clans")
print(games)

# The pop() methods remove a random item from a list and it returns the removed item.
print(games.pop())
print(games)

# clear item from the set using clear()
games.clear()
print(games)

# completely destroy set using del
# del games
# print(games) # NameError means set completely destroyed

ice_cream_flavour = ["vanilla", "pistachio", "butterscotch", "chocobar", "redberry", "pistachio", "chocobar"]
ice_cream_flavour = set(ice_cream_flavour) # set object is not callable 
print(ice_cream_flavour)

# # Joining Sets
# We can join two sets using the union() or update() method or | symbol .
# Union This method returns a new set
players = {"virat kohli", "david beckham", "pele", "usain bolt", "sania mirza"}
sports = {"cricket", "football", "wrestling", "baseball", "chess"}
sports_world = players.union(sports)
print(sports_world)

# Update This method inserts a set into a given set
sports.update(players)
print(sports) # players content are added to sports

# Finding Intersection Items
# Intersection returns a set of items which are in both the sets or using & symbol. See the example
item_1 = {1, 2, 4, 5, 8}
item_2 = {9, 4, 5, 7, 13}
print(item_1.intersection(item_2))

# # Checking Subset and Super Set using method:
# Subset: issubset()
# Subset: Set A is a subset of Set B if every single item in Set A also exists inside Set B.

# Super set: issuperset
# Superset: Set B is a superset of Set A if it contains all items of Set A, plus potentially some extra ones.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))

# Checking the Difference Between Two Sets using .difference() and minus operator -
# simply what is in first set that is not in second set
# # what is in whole number that is not in even number
print(whole_numbers - even_numbers)

# Finding Symmetric Difference Between Two Sets
# It returns the symmetric difference between two sets. It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
# basically it gives all item from both set except the item present in both set
st_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
st_2 = {1, 2, 3, 4}
print(st_1.symmetric_difference(st_2)) 

# # Joining Sets
# If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.
print(st_1.isdisjoint(st_2)) # they have common item

st_3 = {44, 55, 77, 88}
st_4 = {78, 13, 15, 27}
print(st_4.isdisjoint(st_3)) # True : both doesn't have common item