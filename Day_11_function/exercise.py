# 20-June_2026
# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    total = a + b
    return f"The sum of a and b is : {total}"

print(add_two_numbers(4,5))

#2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_circle(r):
    PI = 3.14
    area = PI * r * r
    return f"Area of circle: {area}"

print(area_circle(r= 5))

# 3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0 
    for num in nums:
        if not isinstance(num, (int, float)):
            return f"{num} is not a number"
        
        total += num  
    return total 
    
print(add_all_nums(44, 55, 9, 12))

# 4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit
def celsius_to_farenheit(celsius):
    farenheit = (celsius * (9 / 5)) + 32
    return f"Temperature is: {farenheit} °F"

print(celsius_to_farenheit(40))

# 5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()

    if month in ("february", "march"):
        return "Spring Season"

    elif month in ("april", "may"):
        return "Summer Season"

    elif month in ("june", "july"):
        return "Monsoon Season"

    elif month in ("august", "september"):
        return "Autumn Season"

    elif month in ("october", "november", "december", "january"):
        return "Winter Season"

    else:
        return "Invalid Month"

print(check_season("June"))