# 09-06-2026
#Exercises: Level 1
#1. Declare an empty list
lst = []

# 2. Declare a list with more than 5 items
items = ["bottle", "cup", "pencil", "eraser", "scissor", "knife"]

# 3. Find the length of your list
print(len(items))

# 4. Get the first item, the middle item and the last item of the list
first_item = items[0]

#middle item
middle_index = len(items) // 2
middle_item  = items[middle_index]

# last item
last_item = items[-1]

print(f"first item: {first_item}")
print(f"Middle item: {middle_item}")
print(f"Last item: {last_item}")

#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Arslan", 23, 5.5, "unmarried", "Roorkee, Uttarakhand,India"]
print(mixed_data_types)

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7 Print the list using print()
print(it_companies)

#8 Print the number of companies in the list
print(len(it_companies))

#9 Print the first, middle and last company
# first company
first_company = it_companies[0]

# middle company
middle_index_new = len(it_companies) // 2
middle_company = it_companies[middle_index_new]

# last company
last_company = it_companies[-1]

print(f"First company: {first_company}")
print(f"Middle company: {middle_company}")
print(f"Last company: {last_company}")

#10 Print the list after modifying one of the companies
it_companies[0] = "Open AI"
print(it_companies)

# 11 Add an IT company to it_companies
it_companies.append("Intel")
print(it_companies)

# 12 Insert an IT company in the middle of the companies list
it_companies.insert(4, "Infosys")
print(it_companies)

# 13 Change one of the it_companies names to uppercase (IBM excluded!)
company_uppercase = it_companies[2].upper()
print(company_uppercase)

# 14 Join the it_companies with a string '#;  '
it_companies[0] = it_companies[0] + "#; "
it_companies[1] = it_companies[1] + "#; "
it_companies[2] = it_companies[2] + "#; "
it_companies[3] = it_companies[3] + "#; "
it_companies[4] = it_companies[4] + "#; "
it_companies[5] = it_companies[5] + "#; "
it_companies[6] = it_companies[6] + "#; "
it_companies[7] = it_companies[7] + "#; "
it_companies[8] = it_companies[8] + "#; "

print(it_companies)

# 15 Check if a certain company exists in the it_companies list.
print("IBM#; " in it_companies)

# 16 Sort the list using sort() method 
# .sort() change the original while .sorted don't affect the original list
it_companies.sort()
print(it_companies)

# 17 Reverse the list in descending order using reverse() method
it_companies.sort(reverse= True)
print(it_companies)

# 18 Slice out the first 3 companies from the list
print(it_companies[0:3])

# 19 Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20 Slice out the middle IT company or companies from the list
print(it_companies[4])

# 21 Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# 22 Remove the middle IT company from the list
del it_companies[4]
print(it_companies)

# 23 Remove the last IT company from the list
del it_companies[-1] # del removes item from specific index and list also.
print(it_companies)

#24 Remove all IT companies from the list
it_companies.clear() # this method removes the item not list
print(it_companies)

# 25 Destroy the IT companies list
# del it_companies
# print(it_companies) # it raises NameError it means list is completely destroyed

# 26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

# 27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end.copy()
print(full_stack)

# level - 2
# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method
ages.sort()
print(ages)

min_age = min(ages)
max_age = max(ages)
print(min_age)
print(max_age)

# # Add the min age and the max age again to the list
ages.extend([19, 26])
print(ages)

# find median age 
median_index = len(ages) // 2
median_age = ages[median_index]
print(median_age)

# average age 
average_age = sum(ages) // len(ages)
print(average_age)

# find the range of ages 
range_ages = max_age - min_age
print(range_ages)

# Compare the value of (min - average) and (max - average), use abs() method
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print(min_diff)
print(max_diff)
print(f"Min_difference > Max_difference : {min_diff > max_diff}")

# 1. Find the middle country(ies) in the [countries list]
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_index_3 = len(countries) // 2
middle_country = countries[middle_index_3]
print(middle_country)

# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
check_even = len(countries) % 2 
print(f"It's not even given result: {check_even}")

first_half = countries[0:2]
print(f"First Half Countries: {first_half}")

second_half = countries[2:]
print(f"Second Half Countries: {second_half}")

# 3.  1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
ch, ru, us, *sc = countries
print(f"{ch}, {ru}, {us}, {sc}")
