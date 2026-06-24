# # 15-jun-2026
# # if, else and elif statements
# # if statement
# age = 8
# if age >= 10:
#     print("person is 10 years old.")

# # The above block of code executes due to our condition is true if the condition is falsy then the block of code doesn't executes.
# # So to overcome this we have a solution is : else statement
# else : 
#     print("Person is less than 10 years old.")

# # if we have more than one condition therefore we use elif statement

# marks = int(input("Enter marks here: "))

# if marks >= 90:
#     print("You are topper..")

# elif marks >= 50:
#     print("You are average student..")

# else:
#     print("You are below average..")


# # shorthand 
# # code if condition else code
# a = 0
# print("A is positive") if a >= 0  else print("A is negative")

# # Nested conditions
# #  syntax
# # if condition:
# #     code
# #     if condition:
# #     code

# # check positive negative and even number
# num = -3

# if num > 0 : 
#     if num % 2 == 0 :
#         print("Num is positive and even number..")
#     else:
#         print("Num is positive")   

# elif num == 0 : 
#     print("Num is zero.")

# else :
#     print("Num is negative.") 

# # Not using nested if elif else in logical operators.
# # # syntax
# # if condition and condition:
# #     code

# And logical operator
# check_even_odd = int(input("Enter number here: "))

# if check_even_odd > 0 and check_even_odd % 2 == 0 : 
#     print("Number is positive and even. ⚖️")

# elif check_even_odd > 0 and check_even_odd % 2 != 0 :
#     print("Number is positive and odd. 🔀")

# elif check_even_odd == 0:
#     print("Number is zero. 0️⃣")

# else :
#     print("Number is negative. ➖")

# # Or logical operator
like = int(input("Enter how many likes you have: "))
subscribers = int(input("Enter number of subscribers: "))

if like >= 4000 or subscribers >= 5000:
    print("You are eligible for silver play button. ▶️")

else: 
    print("Keep it up. 💪")