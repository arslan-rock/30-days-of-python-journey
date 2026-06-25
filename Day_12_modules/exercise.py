# # 25-Jun-2026
# Exercises: Level 1
# Write a function which generates a six digit/character random_user_id
import random

def random_user_id():
    return random.randint(1,20)

print(random_user_id())

# 2 Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
import string

def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters: "))
    num_ids = int(input("Enter number of IDs: "))

    characters = string.ascii_letters + string.digits

    for _ in range(num_ids):
        user_id = ''.join(random.choice(characters) for _ in range(num_chars))
        print(user_id)

user_id_gen_by_user()

# 3 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f"rgb({r}, {g}, {b})"

print(rgb_color_gen())

# level: 2
# 1 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
#2 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
#3 Write a function generate_colors which can generate any number of hexa or rgb colors.
def list_of_hexa_colors(n):
    hex_chars = '0123456789abcdef'

    colors = []
    for _ in range(n):
        color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
        colors.append(color)

    return colors

# 2 
def list_of_rgb_colors(n):
    colors = []

    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        colors.append(f'rgb({r}, {g}, {b})')

    return colors

# 3 def generate_colors(color_type, n):

def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)

    elif color_type == 'rgb':
        return list_of_rgb_colors(n)

    else:
        return 'Invalid color type'


# Test
print(list_of_hexa_colors(3))
print(list_of_rgb_colors(3))

print(generate_colors('hexa', 5))
print(generate_colors('rgb', 5))


# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def shuffle_list(lst):
    shuffled = lst[:]  # create a copy
    random.shuffle(shuffled)
    return shuffled

# Example
print(shuffle_list([1, 2, 3, 4, 5]))

# 2 import random

def unique_random_numbers():
    return random.sample(range(10), 7)

# Example
print(unique_random_numbers())