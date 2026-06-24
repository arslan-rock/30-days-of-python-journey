# 17-06-2026
# range() : gives u a list of numbers and it has three parameters (start, stop, step). Default start from 0 and increment is 1 and you must have insert atleast one argument(end position).
# # # syntax
# for iterator in range(start, end, step):
for number in range(11):
    print(number)   # prints 0 to 10, not including 11

lst = list(range(8)) # 0 to 7 not include 8
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7]

# for set
st = set(range(9))
print(st)

# we can also define start, stop, step here
lst_new = list(range(3,11,2))

st_new = set(range(0,9,2))
print(st_new)

# for start from end
lst_3 = list(range(20,13,-2))
print(lst_3) # [20, 18, 16, 14]

# nested loop 
# # syntax
# for x in y:
#     for t in x:
#         print(t)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == "skills":
        for skill in person['skills'] :
            print(skill)

# # For Else
# If we want to execute some message when the loop ends, we use else.
# # syntax
# for iterator in range(start, end, step):
#     do something
# else:
#     print('The loop ended')

for number in range(11):
    print(number)

else:
    print(f"The loop stops at {number}")

# Pass : pass is a do-nothing placeholder used to keep empty blocks from crashing.
for counter in range(12,18):
    pass # avoid empty block error and placeholder for future use

