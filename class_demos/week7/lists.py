# Example of Python lists

# Lists of a single type (aka. arrays)
lottery = [4, 13, 25, 5, 36, 41]
lecturers = ["Aurélien", "Mark", "Derek"]

# Lists can also mix types
various = ["Jim", True, 2.4, 67]

print(lottery)

print("-----")
# Traverse a list to display elements
print("Last night's lottery draw:")
for num in lottery:
    print(num)


print("-----")

print("Here is a list of lecturers with their staff numbers:")
for i in range(len(lecturers)):
    print(f"Index {i}: {lecturers[i]}")

# Add to a list
lecturers.append("Lorna")
print(lecturers)

# Overwrite an elements
lecturers[2] = "Jim"

print("Here is a list of lecturers with their staff numbers:")
for i in range(len(lecturers)):
    print(f"Index {i}: {lecturers[i]}")

lecturers.remove("Mark")
print(lecturers)

# Convert range to list
zero_nine = range(10)
list_zero_nine = list(zero_nine)
readonly_zero_nine = tuple(list_zero_nine)

print(zero_nine, list_zero_nine, readonly_zero_nine)



# Strings work similarly
name = "Mark Ogg"

# Access a single index:
print(lecturers[1])
print(name[1])

for c in "Lucia":
    print(c)

# Slicing a string
# Works also with a list
print(name[1:4])
print(lottery[1:4])

# Change direction of travel
print(name[4:0:-1])
print(lottery[4:0:-1])

# Reverse
print(name[::-1])

# Change case
print(name.upper())
print(name.lower())

# Concatenate
first = "Mark"
second = "Ogg"
full = first[0] + " " + second
print(full)

print(name*10)