# # # 16-06-2026
# # # Tuesday
# # # Loops : In the programming we do repetitive tasks with the help of loop until a certain condition is True.
# # # 1. For loop
# # # 2. While loop

# # # while loop 
# # # while condition :
# # #   code goes here
# # count = 1

# # while count < 5: 
# #     print(count)
# #     count += 1 # update the value upto 1

# # # we can use else here 
# # else :
# #     print(f"loop is stop and it's runs {count - 1} times." )

# # # # Break and Continue - Part 1
# # # Break: We use break when we like to get out of or stop the loop.
# # # # syntax
# # # while condition:
# # #     code goes here
# # #     if another_condition:
# # #         break

# # digit = 0

# # while digit < 7:
# #     print(digit)
# #     digit += 1

# #     if digit == 4:
# #         break

# # # in above program prints 0 1 2 3 but when it reaches to 4 loop stops.

# # # Continue: With the continue statement we can skip the current iteration, and continue with the next:
# # number = 11

# # while number < 17:
# #     if number == 14:
# #         number += 1
# #         continue
# #     print(number)
# #     number += 1

# # # for loop : same as while loop but with some syntax differences. Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# # # syntax
# # # # syntax
# # # use for loop on a list
# # # for iterator in lst:
# # #     code goes here

# # rupees = [23, 44, 55, 66, 77, 88]

# # for rupee in rupees:
# #     print(rupees)

# # using for loop in string
# # # # syntax
# # for iterator in tpl:
# #     code goes here
# language = "Python"

# for letter in language:
#     print(letter)

# for i in range(len(language)):
#     print(i)

# # range() : give the sequence of number line by line and we can do more things with it. We will se later

# # using for loop in tuple
# # # # syntax
# # for iterator in tpl:
# #     code goes here
# odd_numbers = (3, 5, 7, 9, 11)

# for odd_number in odd_numbers:
#     print(odd_number)

# # using for loop in dictionary
# # #   # syntax
# # for iterator in dct:
# #     code goes here
# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }

# for key in person:
#     print(key)

# for key, value in person.items():
#     print(key, value)

# # using for loop in set
# # syntax
# # for iterator in st:
# #     code goes here
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# for company in it_companies:
#     print(company)

# Break and Continue - Part 2
# # # syntax
# for iterator in sequence:
#     code goes here
#     if condition:
#         break
# counters = (0,1,2,3,4,5)

# for counter in counters:
#     print(counter)

#     if counter == 3:
#         break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')






