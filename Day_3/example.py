# # # # Arithmetic Operations in Python
# # # # Integers

# # # print('Addition: ', 1 + 2)        # 3
# # # print('Subtraction: ', 2 - 1)     # 1
# # # print('Multiplication: ', 2 * 3)  # 6
# # # print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
# # # print('Division: ', 6 / 2)        # 3.0         
# # # print('Division: ', 7 / 2)        # 3.5
# # # print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
# # # print ('Division without the remainder: ',7 // 3)   # 2
# # # print('Modulus: ', 3 % 2)         # 1, Gives the remainder
# # # print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2

# # # Floating numbers
# # print('Floating Point Number, PI', 3.14)
# # print('Floating Point Number, gravity', 9.81)

# # # Complex numbers
# # print('Complex number: ', 1 + 1j)
# # print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# # Declaring the variable at the top first

# a = 3 # a is a variable name and 3 is an integer data type
# b = 2 # b is a variable name and 3 is an integer data type

# # Arithmetic operations and assigning the result to a variable
# total = a + b
# diff = a - b
# product = a * b
# division = a / b
# remainder = a % b
# floor_division = a // b
# exponential = a ** b

# # I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
# print(total) # if you do not label your print with some string, you never know where the result is coming from
# print('a + b = ', total)
# print('a - b = ', diff)
# print('a * b = ', product)
# print('a / b = ', division)
# print('a % b = ', remainder)
# print('a // b = ', floor_division)
# print('a ** b = ', exponential)

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('False == True : ', False == True)


