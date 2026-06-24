# 18-06-2026
# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
# using for loop
for a in range(0,11):
    print(a)

# while loop
b = 0
print("Using while loop")

while b < 11:
    print(b)
    b += 1

# 2. reverse loop using for and while from 0 to 10
print("using for loop reverse.")
for c in range(10, -1, -1):
    print(c)

d = 10 
print("reverse loop using while loop.")

while d > -1:
    print(d)
    d -= 1

#3. print star 
star = 7

for i in range(0, star+1): # 0,8 --> 7 row print
    for j in range(0, i+1): #
        print("*", end=" ")
    print()

#4. print star 
hash = 8

for k in range(0, hash+1):
    for l in range(0, hash+1):
        print("#", end=" ")
    print()

#5 print the following pattern 
for g in range(0,11):
    print(f"{g} x {g} = {g * g}")

#6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
python_technologies = ['Python', 'Numpy','Pandas','Django', 'Flask'] 

for python_tech in python_technologies:
    print(python_tech)

#7 Use for loop to iterate from 0 to 100 and print only even numbers
for put_even in range(0,101):
    if put_even % 2 == 0:
        print(f"Even number : {put_even}")

#8 Use for loop to iterate from 0 to 100 and print only odd numbers
for put_odd in range(0, 101):
    if put_odd % 2!= 0:
        print(f"Odd number: {put_odd}") 
                   
# #9 Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
tracker = 0

for count in range(0,101):
    tracker += count

print(f"The sum of number is: {tracker}")

# 10 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_sum = 0
odd_sum = 0

for counter in range(0, 101):
    if counter % 2 == 0:
        even_sum += counter

    else:
        odd_sum += counter

print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")

# This ques not part of exercise but for practice 
reverse_hash = 7

for m in range(0, reverse_hash + 1):
    for n in range(0, reverse_hash - i):
        print("#", end=" ")
    print()

