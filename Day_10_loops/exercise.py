# # 17-06-2026
# # # 💻 Exercises: Day 10
# # Exercises: Level 1
# # #1. Iterate 0 to 10 using for loop, do the same using while loop.
# # # using for loop
# # print("Using for loop")

# # for number in range(0,11):
# #     print(number)

# # # # using while loop
# # # num = 0
# # # print("Using while loop")

# # # while num < 11:
# # #     print(num)
# # #     num += 1

# # #2 Iterate 10 to 0 using for loop, do the same using while loop.
# # print("Reverse loop using for loop.")

# # for counter in range(10, -1, -1):
# #     print(counter)

# # # using while loop reversse
# # counter_new = 10
# # print("Reverse loop using while loop.")

# # while counter_new > -1:
# #     print(counter_new)
# #     counter_new -= 1

# # 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# r = 7
# for a in range(1, r+1):
#     for b in range(1, a+1):
#         print("#", end=" ")
#     print()

# # #4 Use nested loops to create the following:
# # for i in range(1,9):
# #     for j in range(1,8):
# #         print("#", end=" ")
# #     print()

# #5 print following pattern
# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in lst:
#     print(i, "x", i, "=", i * i )

# # 6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# python_tech = ['Python', 'Numpy','Pandas','Django', 'Flask']

# for tech in python_tech:
#     print(tech)

# #7 Use for loop to iterate from 0 to 100 and print only even numbers
# for even in range(0,101):
#     if even % 2 == 0:
#         print(even)

# print("loop stop")

# #8 Use for loop to iterate from 0 to 100 and print only odd numbers
# for odd in range(0,101):
#     if odd % 2 != 0:
#         print(odd)

# print("loop stop")

# # Exercises: Level 2
# # Use for loop to iterate from 0 to 100 and print the sum of all numbers.
value_store = 0

for value in range(0,101):
    value_store += value

print(f"The sum of all numbers is {value_store}")

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_sum = 0
odd_sum = 0

for track in range(0,101):
    if track % 2 == 0:
        even_sum += track
    
    else:
        odd_sum += track

print(f"The sum of all even numbers is: {even_sum}")
print(f"The sum of all odd numbers is: {odd_sum}")

# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

# if no country found with "land"
found_match = False

for country in countries:
    if "land" in country:
        print(country)
        found_match = True
    
if found_match == False:
    print("There is no country has land string.")


# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']

for index in range(len(fruits) -1, -1, -1):
    print(fruits[index])

# #3. Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world
from ast import literal_eval
from pathlib import Path

data_path = Path(__file__).with_name("countries-data.py")
c_data = literal_eval(data_path.read_text(encoding="utf-8"))

    # What are the total number of languages in the data
n_lang = 0
for i in c_data:
    n_lang += len(i["languages"])
print(n_lang)

    # Find the ten most spoken languages from the data
    # I used AI assistance for this one
# 1. Count languages
language_counts = {}
for country in c_data:
    for language in country["languages"]:
        if language in language_counts:
            language_counts[language] += 1
        else:
            language_counts[language] = 1

# 2. Sort languages by count (descending)
sorted_languages = sorted(language_counts.items(), key=lambda item: item[1], reverse=True)
# Used this opportunity to learn about Lambda functions. In this case the lambda function takes one argument {item} (e.g., ("English", 91)) and returns {item[1]} (91).

# 3. Get top 10 & Print results
for language, count in sorted_languages[:10]: # Here I am unpacking the tuple. Equivalent to doing:
    print(f"{language}: {count} countries")   # for item in sorted_languages[:10]: 
                                              #     language, count = item[0], item[1] 
    # Find the 10 most populated countries in the world
population_counts = {}
for country in c_data:
    population_counts[country["name"]] = country["population"]

sorted_pops = sorted(population_counts.items(), key=lambda item: item[1], reverse=True)

for k, v in sorted_pops[:10]:
    print(f"{k}: {v} inhabitants")

