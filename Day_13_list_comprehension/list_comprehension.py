#26-Jun-2026
# #List Comprehension
# List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop.

# # syntax
# [expression for i in iterable if condition]
language = "Jumbo"
lst = list(language)
print(type(lst))
print(lst)

#  Second way: list comprehension
personality = "Lionel Messi"
new_list = [i for i in personality]
print(new_list)
print(len(new_list))

# generat list of numbers 
numbers = [i for i in range(1,11)]
print(numbers)

# # It is possible to do mathematical operations during iteration
squares = [i * i for i in range(1,11)]
print(squares)

# # It is also possible to make a list of tuples
lst_tpls = [(i, i * i)for i in range(1,11)]
print(lst_tpls)

# List comprehension can be combined with if expression
# calculate even numbers 
even_num = [i for i in range(1,11) if i % 2 == 0]
print(even_num)

# calculate odd numbers 
even_num = [i for i in range(1,11) if i % 2 != 0]
print(even_num)

# # Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
positv_even_num = [i for i in numbers if i % 2 == 0 and i > 0]
print(positv_even_num)

# flattening a 2d array 
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattening_lst = [number for row in nested_list for number in row]
print(flattening_lst)

# A lambda function is a small anonymous function (a function without a name). It's mainly used when you need a simple function for a short time.
# syntax
# lambda argument: expression

# simple function
def squares(x):
    return x ** 3

print(squares(4))

# using lambda function 
square_of_num = lambda b: b ** 4
print(square_of_num(5))

# Self invoking lambda function
 # 5 - need to encapsulate it in print() to see the result in the console
print((lambda a, b: a + b)(2,3))

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22

# lambda function inside another function 
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32