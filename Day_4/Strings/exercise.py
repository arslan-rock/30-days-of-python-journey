# # 08-Jun-2026
# # Exercise - Strings
#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
#3. Declare a variable named company and assign it to an initial value "Coding For All".
#4. Print the variable company using print().
#5. Print the length of the company string using len() method and print().
#6. Change all the characters to uppercase letters using upper() method.
#7. Change all the characters to lowercase letters using lower() method.
#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
#9. Cut(slice) out the first word of Coding For All string.
#10. Check if Coding For All string contains a word Coding using the method index, find or other methods

#1
string_1, string_2, string_3, string_4 = "Thirty", "Days", "Of", "Python"
merge_string = string_1 + " " + string_2 + " " + string_3 + " " + string_4

#2
string_5, string_6, string_7 = "Coding", "For", "All"
merge_string_new = string_5 + " " + string_6 + " " + string_7
print(merge_string_new)

#3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4 Print the variable company using print().
print(company)

#5 Print the length of the company string using len() method and print().
print(len(company))

#6 Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7 Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9 Cut(slice) out the first word of Coding For All string.
print(company[0:1])

# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods if the substring not found it raise a value error.
print(company.index("Coding"))

# 11 Replace the word coding in the string 'Coding For All' to Python.
new_company = company.replace("Coding", "Python")
print(new_company)

# 12 Change "Python for Everyone" to "Python for All" using the replace method or other methods.
second_new_company = new_company.replace("All", "Everyone")
print(second_new_company)

# 13 Split the string 'Coding For All' using space as the separator (split()) .
company = "Coding For All"
print(company.split(" "))

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech_giants = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_giants.split(", "))

# 15 What is the character at index 0 in the string Coding For All.
print(company[0])

# 16 What is the last index of the string Coding For All.
print(company[-1])

# 17 What character is at index 10 in "Coding For All" string.
print(company[10]) # at 10 index is space python also counts space as a part of string

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym = second_new_company[0:18:8]
print(acronym)

# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
new_acronym = company[0:14:11]
print(new_acronym)

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
print(company.find("C"))

# 21 Use index to determine the position of the first occurrence of F in Coding For All.
print(company.find("F"))

# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind("l"))

# 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

# 24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind("because"))

# 25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])

# 26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index("because"))

# 27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])

# 28 Does 'Coding For All' start with a substring Coding?
print(company.startswith("Coding"))

# 29 Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))

# 30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
third_new_company = '   Coding For All      '
print(third_new_company.strip())

# 31 Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# 32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = "#Django "  " #Flask" " #Bottle" " #Pyramid" " #Falcon"
print(python_libraries)

# 33 Use the new line escape sequence to separate the following sentences.
new_sentence = "I am enjoying this challenge. \nI just wonder what is next."
print(new_sentence)

# 34 Use a tab escape sequence to write the following lines.
items = "Name\tAge\tCountry\tCity\nAsabeneh 250\tFinland\tHelsinki"
print(items)

# 35 Use the string formatting method to display the following:
radius = 10
area = int(3.14 * radius ** 2)
print(f"The area of a circle with a radius {radius} is {area} meter square.")

# # 36 Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 % 6 = {8 % 6}")
print(f"8 ** 6 = {8 ** 6}")