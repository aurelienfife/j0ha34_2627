# This is the first demo in class
# By Aurélien
# Date: 28/08/2026
# Basic I/O and variables

# Some example of print
print("Hello, World!")
print('I "like" writing code early on a Friday...')
print('It\'s "easy" to code on a Friday')
print('How to show backslash: \\')

# Some user input
# name = input("What is your name?")
name = "Aurélien"

# Output a variable
print(name)
# behaviour 1, using commas
print("Hello,",name,", how are you?")
# behaviour 2, concatenate
print("Hello, " + name + ", how are you?")
# behaviour 3, formatted strings
print(f"Hello, {name}, how are you?")

# Input some numbers
# Input always generates strings, so you need to 
# Typecast as appropriate
age = input("How old are you?")
age = int(age)

gap = int(input("How many years do you want to add?"))
total_age = age + gap
print(f"In {gap} years you will be {total_age}")

# Operators
print(age+gap) # Will add
print(age-gap) # Will subtract
print(age*gap) # Multiply
print(age/10) # Divide
print(age**gap) # Exponent 

