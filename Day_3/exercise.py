# # # # # # # date - 07/06/25
# # # # # # # 💻 Exercises - Day 3
# # # # # # # Declare your age as integer variable
# # # # # # # Declare your height as a float variable
# # # # # # # Declare a variable that store a complex number
# # # # # # # Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

# # # # # # # declare age as a int variable, height as a float variable and a complex number variable.
# # # # # # my_age = 23
# # # # # # my_height = 5.5
# # # # # # complex_digit = 3 + 2j

# # # # # # # give prompt for user to enter base and height to calculate the area of triangle
# # # # # # triangle_base = float(input("Enter the base of triangle: "))
# # # # # # triangle_height = float(input("Enter the height of triangle: "))
# # # # # # area_triangle = 0.5 * triangle_base * triangle_height

# # # # # # print(f"Area of triangle: {area_triangle:.2f} cm")

# # # # # # # Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

# # # # # # # declare three variables as a side of triangle
# # # # # # a = float(input("Enter side a : "))
# # # # # # b = float(input("Enter side b : "))
# # # # # # c = float(input("Enter side c : "))

# # # # # # # now store these in a variable to calculate perimeter = a + b + c
# # # # # # perimeter_triangle = a + b + c
# # # # # # print(f"Perimeter of Triangle: {perimeter_triangle}")

# # # # # # 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# # # # # length_rectangle = float(input("Enter length : "))
# # # # # breadth_rectangle = float(input("Enter breadth : "))

# # # # # # area of rectangle 
# # # # # area_rectangle = length_rectangle *  breadth_rectangle
# # # # # print(f"Area of rectangle: {area_rectangle:.2f} cm.")

# # # # # # perimeter of rectangle 
# # # # # perimeter_rectangle = 2 * (length_rectangle + breadth_rectangle)
# # # # # print(f"Perimeter of rectangle: {perimeter_rectangle:.2f} cm.")

# # # # # 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# # # # radius_circle = float(input("Enter radius of circle: "))
# # # # PI = 3.14

# # # # area_circle = PI * radius_circle ** 2
# # # # print(f"Area of circle: {area_circle:.2f}")

# # # # circumference_circle = 2 * PI * radius_circle
# # # # print(f"Circumference of circle: {circumference_circle:.2f}")

# # # # 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# # # # y = mx + c 
# # # # for y intercept x = 0

# # # m = 2 # slope 
# # # c = -2 # constant

# # # slope = float(m)

# # # # y-intercept set x = 0
# # # y_intercept = c

# # # # x-intercept set y = 0 ---> y = mx + c ---> x = -c / m
# # # x_intercept = -c / m

# # # print(f"Slope: {slope}")
# # # print(f"Y-intercept: {y_intercept}")
# # # print(f"X-intercept: {x_intercept}")

# # # # 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# # # x1, y1 = 2, 2
# # # x2, y2 = 6, 10

# # # # slope
# # # m2 = float((y2 - y1) / (x2 - x1))

# # # # euclidena distance 
# # # d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# # # print(f"Slope: {m2:.2f}")
# # # print(f"Euclidean distance: {d:.2f}")

# # # # 10. Compare the slopes in tasks 8 and 9.
# # # print(f"Slope1 is equal to Slope2: {slope == m2}")
# # # print(f"Slope1 is less than or equal to Slope2: {slope >= m2}")
# # # print(f"Slope1 is greater than or equal to Slope2: {slope <= m2}")

# # # 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# # x = - 3

# # y = (((-3) ** 2) + (6 * (-3)) + 9)

# # print(f"Y = {y}")

# # 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# prog_lang = "python"
# animal = "dragon"

# print(len(prog_lang))
# print(len(animal))
# print(len(prog_lang) != len(animal))

# # 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
# print("on" in prog_lang and "on" in animal)

# # 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# sentence = "I hope this course is not full of jargon"

# print("jargon" in sentence)

# # 15. There is no 'on' in both dragon and python
# print("on" not in prog_lang and animal)

# # 16. Find the length of the text python and convert the value to float and convert it to string
# len_str = len(prog_lang)
# convert_len_float = float(len(prog_lang))
# convert_len_string = str(len(prog_lang))

# print("Length of string: ", len_str)
# print("Converted length to float: ", convert_len_float, type(convert_len_float))
# print("Converted length to string: ", convert_len_string, type(convert_len_string))

# # 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# number = int(input("Enter a number: "))
# result = number % 2

# print("number is: ", result)
# # result = 0 is even otherwise odd

# # 18.. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# floor_division = 7 // 3 # cut the decimal part gives only 2
# converted_int = int(2.7) # 2 

# print("Numbers are equal or not: ", floor_division == converted_int) # 2 == 2 gives True

# # 19. Check if type of '10' is equal to type of 10
# string_num = "10"
# original_num = 10

# print("Equal or not: ", string_num == original_num) # "10" is string and 10 is integer it gives false

# # 20. Check if int('9.8') is equal to 10
print("Equal or not: ", int(float("9.8")) == 10)

#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours: "))
rate_per_hours = int(input("Enter rate per hours: "))
pay_of_person = hours * rate_per_hours

print("Pay of person: ", pay_of_person)

#23. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
num_of_years = int(input("Enter the number of years: "))

days = num_of_years * 365
hours = days * 24
minutes = hours * 60 
seconds = minutes * 60 

print("You have lived ", seconds, " seconds in a ", num_of_years)

# #24. Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
a = 1
print(a, 1, a, a**2, a**3)

b = 2
print(b, 1, b, b**2, b**3)

c = 3
print(c, 1, c, c**2, c**3)

d = 4
print(d, 1, d, d**2, d**3)

e = 5
print(e, 1, e, e**2, e**3)
