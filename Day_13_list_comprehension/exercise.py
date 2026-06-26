# Exercises: Day 13
# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_and_zeros = [i for i in numbers if i < 0 or i == 0]
print(neg_and_zeros)

# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_list = [num for row in list_of_lists for num in row]
print(flatten_list)

#3 Using list comprehension create the following list of tuples:
lst_tuples = [(i, 1, i, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(1,11)]
print(*lst_tuples, sep="\n")

#4 Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list = [ [country.upper(), country[:3].upper(), capital.upper()]for i in countries for country, capital in i]
print(new_list)

#5 Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dictionary = [[{"country" : country,  "city" : city}] for value in countries for country, city in value]
print(dictionary)

# 6 Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_names = [[first_name  + " " + last_name ]for title in names for first_name, last_name in title]
print(new_names)

# Write a lambda function which can solve a slope or y-intercept of linear functions.
# y2 - y1 / x2- x1 

# y_intercept
y_intercept = lambda x, y, m:  f"Y- intercept: {y - (m * x)}"
print(y_intercept(x= 3, y= 7, m= 2))

# slope 
# y2- y1 / x2- x1
slope = lambda x1, x2, y1, y2: f"Slope : {(y2 - y1) // (x2 - x1)}"
print(slope(x1= 1 , y1= 2, x2= 3, y2= 6))
