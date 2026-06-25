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

# 6 Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    slope = (x2 - x1) / (y2 - y1)
    return slope

print(calculate_slope(x2= 8, x1= 4, y2= 10, y1= 5))

# 7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def calculate_quadratic(a, b, c, x):
    quadratic = (a * x ** 2) + (b * x) + c
    return quadratic

print(calculate_quadratic(a= 4, x= 2, b= 3, c= 5)) 

# 8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(nums):
    for num in nums:
        print(num)

print(print_list([10, 20, 30]))   

# 9 reverse list 
def reverse_list(start_num):
    total = []

    for num in range(start_num -1, -1, -1):
        total.append(num)
    return total

print(reverse_list(11))

# 10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(items):
    new_total = []

    for item in items:
        capitalized_item = item.title()
        new_total.append(capitalized_item)
    
    return new_total

print(capitalize_list_items(["arslan", "muneeb", "arsh", "suresh jain"]))

# 11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
characters = ["ahmed", "anuj", "karan", "jatin"]

def add_item(lst, item):
   lst.append(item)
   return lst

print(add_item(characters, "sapru"))

# 12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(new_lst, new_item):
    new_lst.remove(new_item)
    return new_lst

marvel_movie = ["Avengers", "Captain America", "Iron Man", "Black Widow"]
print(remove_item(marvel_movie, "Iron Man"))

# 13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(nums):
    total = 0
    
    for num in range(1, nums + 1):
      total += num
    return total
  
print(sum_of_numbers(9))

#14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(odd_nums):
    total_odds = 0

    for odd_num in range(1, odd_nums + 1):
        if odd_num % 2 != 0 :
            total_odds += odd_num
    return total_odds
    
print(sum_of_odds(10))

#15 # Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_even(even_nums):
    total_even = 0 

    for even_num in range(1, even_nums + 1):
        if even_num % 2 == 0 :
            total_even += even_num
    return total_even

print(sum_of_even(10))

# 23-Jun-2026
# # Exercises: Level 2
#1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def count_range_evens_odds(max_limit):
    even = 0
    odd = 0

    # Starting from 0 instead of 1
    for num in range(0, max_limit + 1):
        if num % 2 == 0:  
            even += 1
        else:  
            odd += 1

    print("Even numbers:", even)
    print("Odd numbers:", odd)

# Call the function with 100 as the single parameter
count_range_evens_odds(100)

# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

# Test cases
print(factorial(5))  # Output: 120 (5 * 4 * 3 * 2 * 1)
print(factorial(0))  # Output: 1

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    return not value

print(is_empty(""))
print(is_empty([]))
print(is_empty("Hello"))

#4 Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
 
import math

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]


def calculate_mode(numbers):
    counts = {}

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    max_count = max(counts.values())

    return [num for num, count in counts.items() if count == max_count]


def calculate_range(numbers):
    return max(numbers) - min(numbers)


def calculate_variance(numbers):
    mean = calculate_mean(numbers)

    squared_diffs = []
    for num in numbers:
        squared_diffs.append((num - mean) ** 2)

    return sum(squared_diffs) / len(numbers)


def calculate_std(numbers):
    variance = calculate_variance(numbers)
    return math.sqrt(variance)


# Example
data = [1, 2, 2, 3, 4, 5]

print("Mean:", calculate_mean(data))
print("Median:", calculate_median(data))
print("Mode:", calculate_mode(data))
print("Range:", calculate_range(data))
print("Variance:", calculate_variance(data))
print("Standard Deviation:", calculate_std(data))

#5 Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
def greet(name = "Guest"):
    return f'"Hello, {name}!"'

print(greet())
print(greet("Anas"))

#6 Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
def show_args(**kwargs):
    for name, value in kwargs.items():
        print(f"{name}: {value}")

print(show_args(name = "Arslan", age = 23, city = "Delhi"))

# # Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

# Example
print(is_prime(7))   # True
print(is_prime(10))  # False

# 2 Write a functions which checks if all items are unique in the list.
def all_unique(lst):
    return len(lst) == len(set(lst))

# Example
print(all_unique([1, 2, 3, 4]))      # True
print(all_unique([1, 2, 2, 3, 4]))   # False

# 3 Write a function which checks if all the items of the list are of the same data type.
def same_data_type(lst):
    if not lst:
        return True

    first_type = type(lst[0])

    for item in lst:
        if type(item) != first_type:
            return False

    return True

# Example
print(same_data_type([1, 2, 3, 4]))      # True
print(same_data_type([1, "2", 3]))       # False

# 4 Write a function which check if provided variable is a valid python variable
def is_valid_variable(var_name):
    return var_name.isidentifier()

# Example
print(is_valid_variable("my_var"))   # True
print(is_valid_variable("2name"))    # False
print(is_valid_variable("class"))    # True (identifier, but keyword)

# # 5 Go to the data folder and access the countries-data.py file.
# 5a. Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
