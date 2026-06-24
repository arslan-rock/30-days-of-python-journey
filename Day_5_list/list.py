# 09-june-2026
# list
# create list using list() built functn
lst =  list()
print(len(lst))

# also create like this
empty_list = []
print(len(empty_list))

# we are creating our favourite movies list
fav_movies = ["Jawan", "Dhurandhar", "RRR", "Titanic", "Avatar"]
print(f"Favourite movies of Arslan: {fav_movies}")

# we can give different type of data in a same list
employee_details = ["Arslan", 25000, 23, "True", "Male", "Roorkee, India"]
print(employee_details)

# Acess list items 
print(f"Pick the first movie: {fav_movies[0]} and {len(fav_movies[0])} characters in it.")
print(f"Pick the last movie: {fav_movies[-1]} and {len(fav_movies[-1])} characters in it.")

# unpacking items in list 
name, money, age, *rest = employee_details
print(name) # Arslan
print(money) # 25000
print(age) # 23
print(rest) # ['True', 'Male', 'Roorkee, India']

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *dn = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(dn) # ['Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']

# positive and negative indexing
print(countries[3:4]) # positive index
print(countries[-3:-5:-1]) # neg index
print(countries[3:7:2]) # start stop step
print(countries[::-1]) # reverse the list

# modify list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[2] = "litchi"
print(fruits) # ['banana', 'orange', 'litchi', 'lemon']

# check items in list 
print("litchi" in fruits) # True

# add items in list
# append() : adds items in the last in a given list
fruits.append("mango")
print(fruits)

#inserting items in a list
fruits.insert(3, "watermelon")
print(fruits)

# remove items from a list : only remove 1 item at a time and you have to specify the item name
fruits.remove("litchi")
print(fruits)

# pop() : by default remove last item from a list and you have to specify the index of a list only takes 1 argument
fruits.pop(0) # default remove the last item
print(fruits)

# # Removing Items Using Del
# The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely
del fruits[0:4]
print(fruits)

# # clearing List Items
# The clear() method empties the list:
cars = ["toyota", "mahindra", "suzuki", "tata", "ferrari"]
# cars.clear()
print(cars)

# # Copying a List
# It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1. But there are lots of case in which we do not like to modify the original instead we like to have a different copy. One of way of avoiding the problem above is using copy().
cars_copy = cars.copy()
print(cars_copy)

# Joining Lists
# There are several ways to join, or concatenate, two or more lists in Python.

# Plus Operator (+)
new_list = cars + countries
print(new_list)

# Joining using extend() method The extend() method allows to append list in a list. See the example below.
positive_integers = [1, 2, 3, 4, 5]
negative_integers = [-5, -4, -3, -2, -1]
zero = [0]

negative_integers.extend(zero)
negative_integers.extend(positive_integers)
print(negative_integers)

# count() : The count() method returns the number of times an item appears in a list:
words = ["because", "because", "wood", "in", "at", "at", "at"]
print(words.count("at"))

# index() : The index() method returns the index of an item in the list:
print(words.index("at"))

# The reverse() method reverses the order of a list.
print(cars)
cars.reverse()
print(cars)

# To sort lists we can use sort() method or sorted() built-in functions. The sort() method reorders the list items in ascending order and modifies the original list. If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.
numbers = [22, 19, 24, 25, 26, 24, 25, 24]
numbers.sort()
print(numbers) # ascending order
numbers.sort(reverse=True)
print(numbers) # descending order

print(sorted(numbers)) # it doesn't modify the original list just give you a new list 
print(numbers)



