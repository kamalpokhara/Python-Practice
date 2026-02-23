fruits = ["apple", "banana", "cherry", "dates", "fig", "grape"]

"""'


if fruits:
    print("The list is not empty")

if "Apple" in fruits:
    print("Yes, apple is in the fruits")


regex= "123456789-+"
user_input = input("Entre your no: ")

for char in user_input:
    if char not in regex:
        print("Invalid ph no")
        break
else: 
    print("Valid number")

"""

# zip

names = ['alice', 'in', 'boredland']
ages = [25,16,55]
x=5
y=6

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

count = 1
while count:
    print(count)
    count += 1

